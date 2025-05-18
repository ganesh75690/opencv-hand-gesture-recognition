def preprocess_frame(frame):
    # Resize the frame to a fixed size
    frame = cv2.resize(frame, (640, 480))
    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Apply Gaussian blur to the frame
    blurred_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0)
    return blurred_frame

def draw_gesture(frame, gesture):
    # Define the position to draw the gesture text
    position = (10, 30)
    # Define the font and scale
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    color = (255, 0, 0)  # Red color
    thickness = 2
    # Put the gesture text on the frame
    cv2.putText(frame, gesture, position, font, font_scale, color, thickness)

def show_frame(window_name, frame):
    # Display the frame in a window
    cv2.imshow(window_name, frame)

def release_resources(capture):
    # Release the video capture object
    capture.release()
    cv2.destroyAllWindows()