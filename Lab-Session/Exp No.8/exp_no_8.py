import cv2
from google.colab.patches import cv2_imshow

# The error 'AttributeError: 'NoneType' object has no attribute 'shape''
# occurred because the image file 'image1.jpg' was not found at the specified path.
# Based on the available files in the Colab environment, '/content/PICTURE.png' exists.
# We will use this image for now.
# If you wish to use 'image1.jpg', please upload it to the Colab environment.

image = cv2.imread('/content/PICTURE.png') # Using an available image file

if image is None:
    print("Error: Could not load the image from the specified path. Please ensure the file exists and is accessible.")
else:
    height, width = image.shape[:2]

    scale_factor = 3.0
    bigger_image = cv2.resize(image,(int(width*scale_factor),
    int(height*scale_factor)))

    scale_factor = 0.5
    smaller_image = cv2.resize(image,(int(width*scale_factor),
    int(height*scale_factor)))

    # Use cv2_imshow for displaying images in Google Colab, as cv2.imshow does not work in this environment.
    print("Original Image:")
    cv2_imshow(image)
    print("Bigger Image:")
    cv2_imshow(bigger_image)
    print("Smaller Image:")
    cv2_imshow(smaller_image)

    # These lines save the resized images to files.
    cv2.imwrite("Bigger_image.jpg",bigger_image)
    cv2.imwrite("smaller_image.jpg",smaller_image)
