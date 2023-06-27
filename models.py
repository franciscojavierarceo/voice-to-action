# models.py
from django.db import models

class AudioClip(models.Model):
    audio_file = models.FileField(upload_to='audio_clips/')
