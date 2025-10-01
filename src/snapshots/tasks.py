import requests
import helpers.bright_data
from django.apps import apps
from django_qstash import stashed_task
from helpers.bright_data import BRIGHT_DATA_DATASET_ID

MAX_PROGRESS_ITERATION_COUNT = 10

@stashed_task
def perform_reddit_scrape_task(subreddit_url,num_of_posts: int = 20,progress_countdown = 300):
    BrightDataSnapshot = apps.get_model("snapshots","BrightDataSnapshot") # to avoid circular imports
    data = helpers.bright_data.perform_scrape_snapshot(subreddit_url=subreddit_url, num_of_posts= num_of_posts, raw = True)
    snapshot_id = data.get('snapshot_id')
    instance = BrightDataSnapshot.objects.create(
        snapshot_id=snapshot_id,    
        dataset_id=BRIGHT_DATA_DATASET_ID,
        url = subreddit_url,
    )
    # get_snapshot_progress_task.delay(snapshot_id)
    # start progress checking
    get_snapshot_instance_progress_task.apply_async(args=(instance.id,),countdown=300)
    return snapshot_id

@stashed_task
def get_snapshot_instance_progress_task(instance_id : str) -> bool:
    BrightDataSnapshot = apps.get_model("snapshots","BrightDataSnapshot") # to avoid circular imports
    instance = BrightDataSnapshot.objects.get(id=instance_id)
    progress_check_count = instance.progress_check_count
    new_progress_check_count = progress_check_count + 1
    snapshot_id = instance.snapshot_id
    data = helpers.bright_data.get_snapshot_progress(snapshot_id,raw= True)   
    status = data.get('status')
    records = data.get('records') or 0
    instance.records = records
    instance.status = status
    instance.progress_check_count = new_progress_check_count
    instance.save()
    instance.refresh_from_db()
    progress_complete = instance.progress_complete
    if not progress_complete and new_progress_check_count < MAX_PROGRESS_ITERATION_COUNT:
        print("Recheck how our snapshot is doing")
        delay_delta = 30 + progress_check_count
        get_snapshot_instance_progress_task.apply_async(
                args=(instance_id,), 
            countdown=delay_delta
        )
        return
    return status == "ready"
