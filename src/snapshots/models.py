from django.db import models
from django.utils import timezone
# Create your models here.
class BrightDataSnapshot(models.Model):
    snapshot_id = models.CharField(max_length=120)
    dataset_id = models.CharField(max_length=120)
    status = models.CharField(max_length=120)
    _status = models.CharField(max_length=120)
    error_msg = models.TextField(null=True, blank=True)
    url = models.URLField(null=True, blank = True)
    records = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now= True)
    progress_check_count = models.IntegerField(default = 0)
    last_status_changed_at = models.DateTimeField(
        auto_now= False,
        auto_now_add = False,
        blank=True,
        null = True
    )
    finished_at = models.DateTimeField(
        auto_now= False,
        auto_now_add = False,
        blank=True,
        null = True
    )

    def save(self, *args, **kwargs):
        status_changed = self.status != self._status
        if status_changed:
            self._status = self.status
            self.last_status_changed_at = timezone.now()
        if not self.finished_at and self.progress_complete:
            self.finished_at = timezone.now()
        super().save(*args, **kwargs)

    @property
    def progress_complete(self):
        return self.status in ["ready","failed"]

    @property
    def is_downloadable(self) -> bool:
        if self.error_msg:
            return False
        return self.status == "ready" and self.records > 0
