import cv2
from gesture_recognition import GestureRecognition
from utils import preprocess_frame

def main():
    # Initialize video capture
    cap = cv2.VideoCapture(0)
    
    # Check if the webcam is opened correctly
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    gesture_recognition = GestureRecognition()

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        # Preprocess the frame
        processed_frame = preprocess_frame(frame)

        # Detect gesture
        gesture = gesture_recognition.detect_gesture(processed_frame)

        # Display the resulting frame with gesture
        cv2.putText(frame, f'Gesture: {gesture}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv2.imshow('Hand Gesture Recognition', frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()