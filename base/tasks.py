import whisper
from celery import shared_task

from base.models import Recordings


@shared_task
def transcribe_video(video_id, audio_path):
    try:
        recording = Recordings.objects.get(pk=video_id)
    except Recordings.DoesNotExist:
        return

    if not recording.video:
        return

    model = whisper.load_model("base")
    result = model.transcribe(audio_path)

    recording.transcript = result["text"]
    recording.save()