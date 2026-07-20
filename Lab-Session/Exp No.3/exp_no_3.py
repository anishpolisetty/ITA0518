import cv2
from google.colab.patches import cv2_imshow

img = cv2.imread('/content/PICTURE.png') # Corrected image path for Colab

if img is None:
    print('Error: Could not load image. Please check the path and file.')
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    cv2.imwrite('Canny_Edges_3rd.jpg', edges)
    cv2_imshow(edges) # Changed '‘Edges' to 'Edges' and cv2.imshow to cv2_imshow
    # Removed cv2.waitKey(0) and cv2.destroyAllWindows() as they are not needed with cv2_imshow in Colab
