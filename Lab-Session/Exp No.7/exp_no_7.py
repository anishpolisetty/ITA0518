import cv2
from google.colab.patches import cv2_imshow # Import cv2_imshow for Colab compatibility

# IMPORTANT: Upload your video file (e.g., 'image1.mp4') to the Colab environment
# and then use the correct path. For demonstration, we'll use a placeholder path.
video_path = '/content/image1.mp4' # Changed path to a Colab accessible file
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
        # For displaying both slow and fast motion, you might need to combine them into one image
        # or call cv2_imshow twice if Colab supports multiple output frames simultaneously for different windows.
        # For simplicity, let's display the slow motion as an example.
        slow_motion_frame = cv2.resize(frame, None, fx=slow_factor, fy=slow_factor)
        cv2_imshow(slow_motion_frame)
        print("Displaying Slow Motion (close this window to see the next frame)") # Inform the user

        # If you want to see fast motion, you would need another cv2_imshow or combine them.
        # fast_motion_frame = cv2.resize(frame, None, fx=fast_factor, fy=fast_factor)
        # cv2_imshow(fast_motion_frame)

        # Note: cv2.waitKey and cv2.destroyAllWindows are not needed with cv2_imshow in Colab.
        # The display will persist until the next cell execution or kernel restart.

    cap.release()
