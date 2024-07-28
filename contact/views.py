import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .forms import ContactForm

@csrf_exempt
@require_http_methods(["POST"])
def contact_view(request):
    try:
        data = json.loads(request.body.decode('utf-8'))
        form = ContactForm(data)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': 'Form submitted successfully'})
        else:
            print('Form errors:', form.errors)  # Add this line to debug
            return JsonResponse({'error': 'Form is not valid', 'details': form.errors}, status=400)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
