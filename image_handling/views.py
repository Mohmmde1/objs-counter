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

    # List of object names
    object_names = [
        "person", "bicycle", "car", "motorcycle", "airplane", "bus", "train", "truck", "boat", "traffic light",
        "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat", "dog", "horse", "sheep", "cow",
        "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella", "handbag", "tie", "suitcase", "frisbee",
        "skis", "snowboard", "sports ball", "kite", "baseball bat", "baseball glove", "skateboard", "surfboard",
        "tennis racket", "bottle", "wine glass", "cup", "fork", "knife", "spoon", "bowl", "banana", "apple",
        "sandwich", "orange", "broccoli", "carrot", "hot dog", "pizza", "donut", "cake", "chair", "couch",
        "potted plant", "bed", "dining table", "toilet", "tv", "laptop", "mouse", "remote", "keyboard",
        "cell phone", "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
        "teddy bear", "hair dryer", "toothbrush"
    ]
    # Pass the object names to the template
    context = {
        'object_names': object_names,
    }
    
    return render(request, 'upload/upload.html', context)