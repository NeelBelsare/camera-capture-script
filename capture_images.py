import cv2
import os
import time
from datetime import datetime

def capture_and_store_images(output_folder="captured_images", capture_interval=1):
    """Captures images from the default camera every 'capture_interval' seconds and stores them in the specified folder."""

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("Error: Could not open camera.")
        return

    try:
        while True:
            ret, frame = camera.read()

            if not ret:
                print("Error: Could not capture frame.")
                break

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = os.path.join(output_folder, f"image_{timestamp}.jpg")
            cv2.imwrite(filename, frame)
            print(f"Captured: {filename}")

            time.sleep(capture_interval)

    except KeyboardInterrupt:
        print("\nCapture interrupted by user.")

    finally:
        camera.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_and_store_images()
