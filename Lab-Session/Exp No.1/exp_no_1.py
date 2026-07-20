import cv2
from google.colab.patches import cv2_imshow

img = cv2.imread('/content/PICTURE.png') # Changed path to a Colab accessible file

if img is None:
    print('Error: Could not load image. Please check the path and file.')
else:
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2_imshow(gray_img) # Changed cv2.imshow to cv2_imshow and corrected variable name
    cv2.imwrite('gray_image.jpg', gray_img)
    # Removed cv2.waitKey(0) and cv2.destroyAllWindows() as they are not needed with cv2_imshow in Colab
