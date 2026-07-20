import cv2
from google.colab.patches import cv2_imshow

image = cv2.imread('/content/PICTURE.png') # Changed path to a Colab accessible file

if image is None:
    print('Error: Could not load image. Please check the path and file.')
else:
    blur = cv2.GaussianBlur(image, (5, 5), 10)
    cv2.imwrite('blurred_image.jpg', blur)
    cv2_imshow(blur) # Changed cv2.imshow to cv2_imshow
    # Removed cv2.waitKey(0) and cv2.destroyAllWindows() as they are not needed with cv2_imshow in Colab
