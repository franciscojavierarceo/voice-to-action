# views.py
import base64
from django.core.files.base import ContentFile
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import AudioClip

@csrf_exempt
def recording(request):
    if request.method == 'POST':
        audio_data = request.POST.get('audioData')
        format, audio_str = audio_data.split(';base64,')  
        ext = format.split('/')[-1]
        audio_data = ContentFile(base64.b64decode(audio_str), name='temp.' + ext)

        clip = AudioClip(audio_file=audio_data)
        clip.save()

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'bad request'}, status=400)
