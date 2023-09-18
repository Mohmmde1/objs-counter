from django.shortcuts import render, redirect

from image_handling.models import SubmittedFormData


def upload(request):
    if request.method == 'POST':
        uploaded_image = request.FILES.get('image')
        selected_objects = request.POST.getlist('selected_objects')

        if uploaded_image:
            # Save the uploaded image
            uploaded_image_obj = SubmittedFormData(image=uploaded_image, selected_objects=','.join(selected_objects))
            uploaded_image_obj.save()
            
        # Get the ID of the saved object
        saved_object_id = uploaded_image_obj.id

           
        return redirect('counter:count', form_id = saved_object_id)

    return render(request, 'upload/upload.html')