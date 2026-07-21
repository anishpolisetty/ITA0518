import cv2
from google.colab.patches import cv2_imshow # Import for Colab display

# Correcting the SyntaxError: unmatched ')' by removing the extra parenthesis.
# Also, cv2.VideoCapture is for video files, and the path was a local Windows path
# pointing to an image. We will use an available video file for demonstration.

video_path = '/content/demonslayer.mp4' # Using an available video file in Colab
cap = cv2.VideoCapture(video_path) # Corrected: removed extra ')'

if not cap.isOpened():
    print(f"Error: Could not open video file {video_path}. Please ensure the file exists and is accessible.")
else:
    slow_factor = 0.5 # Factor for visual 'slow motion' effect (smaller frames)
    fast_factor = 2.0 # Factor for visual 'fast motion' effect (larger frames)
    frame_count = 0
    max_frames_to_display = 3 # Display a limited number of frames in Colab output

    print(f"Processing video: {video_path}")
    while True:
        ret, frame = cap.read()
        if not ret:
            break # Break the loop if no more frames are available

        # Only display a few frames to prevent overwhelming the Colab output
        if frame_count < max_frames_to_display:
            # Resize the frame for 'slow motion' effect (visually smaller frame)
            slow_motion_frame = cv2.resize(frame, None, fx=slow_factor, fy=slow_factor)
            # Resize the frame for 'fast motion' effect (visually larger frame)
            fast_motion_frame = cv2.resize(frame, None, fx=fast_factor, fy=fast_factor)

            print(f"--- Frame {frame_count} ---")
            print("Original Frame:")
            cv2_imshow(frame)
            print("Slow Motion Effect Frame (scaled down):")
            cv2_imshow(slow_motion_frame)
            print("Fast Motion Effect Frame (scaled up):")
            cv2_imshow(fast_motion_frame)
            print("---------------------")

        frame_count += 1
        # In Colab, cv2.waitKey does not function for real-time interaction
        # as it would in a local application. Breaking after a few frames
        # to demonstrate the effect without producing excessive output.
        if frame_count >= max_frames_to_display:
            break

    cap.release()
    # cv2.destroyAllWindows() is not necessary/effective in a Colab environment.

print("Video processing finished.")
