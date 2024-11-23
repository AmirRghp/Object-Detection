# Real-Time Object Detection with YOLOv5 and PyQt5

This repository contains a PyQt5-based application for real-time object detection using the YOLOv5 model. The application captures video frames from a camera, processes them using YOLOv5, and displays annotated frames with detected objects in a user-friendly GUI.

## Features

- Real-time object detection using YOLOv5.
- User-friendly interface created with PyQt5.
- Annotated frames displayed in the GUI with bounding boxes and labels for detected objects.

## Requirements

- Python 3.8+
- PyQt5
- OpenCV
- PyTorch
- YOLOv5 model via Ultralytics

Install the required packages using pip:
```bash
    pip install -r requirements.txt 
```

## How It Works
1. YOLOv5 Initialization:
    - The YOLOv5 model (yolov5s) is loaded using the Ultralytics Hub.
    - The model is pre-trained and ready for inference.

2. Camera Capture:
   - Video frames are captured in real-time from the default camera (or specified device).
   - For use default change this part of code on line 22:
        ```bash
        self.cap = cv2.VideoCapture(0)
        ```
   
3. Object Detection:
    - Each frame is processed by YOLOv5 for object detection.
    - Detected objects are annotated with bounding boxes and labels.

4. Display:
    - Annotated frames are resized and displayed in the GUI using a QLabel widget.

5. Frame Updates:
    - The application updates the display every 30ms (approximately 33 FPS).

## Running the Application
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/real-time-object-detection.git
   cd real-time-object-detection
   ```
2. Run the application:
   ```bash
   python main.py
   ```
   
## Project Structure
   - `main.py`: Main application script for the GUI and object detection logic.
   - `UI.ui`: GUI layout designed in Qt Designer.

## Notes
   - Ensure your camera is connected and accessible.
   - The application uses the default camera device. To use a different device, modify the cv2.VideoCapture argument in the code.
   - For better detection you can use `yolov5x` model.

## Video
   - Real-Time Detection:
      ![App Demo](screenshots/AppVideo.gif)

## Contributing
Contributions are welcome! Feel free to fork this repository and submit pull requests.