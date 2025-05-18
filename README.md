# OpenCV Hand Gesture Recognition

This project implements hand gesture recognition using OpenCV. It captures video from the webcam, processes the frames, and recognizes hand gestures in real-time.

## Project Structure

```
opencv-hand-gesture-recognition
├── src
│   ├── main.py               # Entry point of the application
│   ├── gesture_recognition.py # Contains the GestureRecognition class
│   ├── utils.py              # Utility functions for image processing
│   └── config.py             # Configuration settings
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/opencv-hand-gesture-recognition.git
   cd opencv-hand-gesture-recognition
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python src/main.py
   ```

2. Follow the on-screen instructions to perform hand gestures in front of the webcam.

## Functionality

- Real-time hand gesture recognition using OpenCV.
- Customizable gesture detection thresholds and model paths in `config.py`.
- Utility functions for preprocessing and drawing in `utils.py`.

## Contributing

Feel free to submit issues or pull requests to improve the project.