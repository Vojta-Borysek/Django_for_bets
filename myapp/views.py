from django.shortcuts import render
from .forms import UploadFileForm
from django.conf import settings
import os


def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # Remove file handling logic from here
            pass
    else:
        form = UploadFileForm()

    # Specify the full path to the file using the project's base directory
    file_path = os.path.join(settings.BASE_DIR, 'Value.txt')

    # Read the content of the file
    with open(file_path, 'r') as file:
        file_content = file.read()

    return render(request, 'myapp/index.html', {'form': form, 'file_content': file_content})



