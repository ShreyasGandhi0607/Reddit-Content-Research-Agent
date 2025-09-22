from django.db import models

# Create your models here.
class RedditPost(models.Model):
    # id
    post_id = models.CharField(max_length=120, db_index = True)
    url = models.URLField(db_index=True)
    title = models.CharField(max_length=250, null = True, blank = True)
    date_posted = models.DateTimeField(
        auto_now_add = False,
        auto_now = True, 
        null = True,
        blank = True
    )
