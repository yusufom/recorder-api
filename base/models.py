from django.db import models

# Create your models here.

class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at', '-updated_at']

class Recordings(TimeStamp):
    name = models.CharField(max_length=270)
    
    
    def __str__(self):
        return self.name 
    
    
class VideoRecordings(TimeStamp):
    recording = models.ForeignKey(Recordings, on_delete=models.CASCADE)
    video = models.FileField(("Video File"), upload_to='videos/', null=True)
    
    
    def __str__(self):
        return self.recordings.name + ": " + str(self.video)