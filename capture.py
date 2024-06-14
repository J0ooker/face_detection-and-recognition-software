import cv2
import os

# Create a directory to save images if it doesn't exist
image_directory = "images"
if not os.path.exists(image_directory):
    os.makedirs(image_directory)

# Initialize the camera
cap = cv2.VideoCapture(0)

print("Press 'c' to capture an image and 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    cv2.imshow("Capture Image", frame)

    key = cv2.waitKey(1)
    if key % 256 == ord('c'):
        # Press 'c' to capture an image
        img_name = os.path.join(image_directory, "captured_image.jpg")
        cv2.imwrite(img_name, frame)
        print(f"Image saved: {img_name}")

    elif key % 256 == ord('q'):
        # Press 'q' to quit the program
        print("Quitting...")
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()
