import sys
import cv2
import torch
import numpy as np
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)


class ObjDetect(QMainWindow):
    def __init__(self):
        super(ObjDetect, self).__init__()
        uic.loadUi('./UI.ui', self)

        # Initialize YOLOv5 model
        self.model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

        # Set up the camera
        self.cap = cv2.VideoCapture(1)

        if not self.cap.isOpened():
            print("Error: Could not open camera.")
            sys.exit()

        # Set up QTimer to call the update function periodically
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)  # Update every 30ms (about 33 FPS)

    def update_frame(self):
        # Capture frame-by-frame
        ret, frame = self.cap.read()
        if not ret:
            return

        # Run YOLOv5 inference
        results = self.model(frame)
        results.render()  # Annotate detections onto the frame

        # Convert the frame (with annotations) to RGB format for Qt
        output_frame = cv2.resize(results.ims[0], (1024, 768))
        output_frame_rgb = cv2.cvtColor(output_frame, cv2.COLOR_BGR2RGB)
        height, width, channel = output_frame_rgb.shape
        bytes_per_line = 3 * width
        q_image = QImage(output_frame_rgb.data, width, height, bytes_per_line, QImage.Format_RGB888)

        # Display the QImage in the QLabel
        self.lblimage.setPixmap(QPixmap.fromImage(q_image))

    def closeEvent(self, event):
        # Release the camera when the window is closed
        self.cap.release()


def main():
    app = QApplication(sys.argv)
    window = ObjDetect()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
