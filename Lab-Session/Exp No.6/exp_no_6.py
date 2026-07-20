import cv2
from google.colab.patches import cv2_imshow # Import cv2_imshow for Colab compatibility

# IMPORTANT: Upload your video file (e.g., 'demonslayer.mp4') to the Colab environment
# and then use the correct path. For demonstration, we'll use a placeholder path.
video_path = '/content/demonslayer.mp4' # Changed path to a Colab accessible file
cap = cv2.VideoCapture(video_path)

# Check if video opened successfully
if not cap.isOpened():
    print(f"Error: Could not open video file at {video_path}. Please check the path and file.")
else:
    slow_factor = 0.5
    fast_factor = 2.0
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break # Break the loop if there are no more frames

        # Resize and display frames
        cv2_imshow(cv2.resize(frame, None, fx=slow_factor, fy=slow_factor)) # Use cv2_imshow
        # For displaying multiple windows, it's usually better to create separate 'imshow' calls or combine frames.
        # For simplicity, here we show one at a time, or if Colab supports it, both will appear in separate output blocks.

        # Note: cv2.waitKey and cv2.destroyAllWindows are not needed with cv2_imshow in Colab.
        # The display will persist until the next cell execution or kernel restart.

    cap.release()
