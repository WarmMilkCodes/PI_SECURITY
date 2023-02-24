import cv2

# Capture video from USB webcam
cap = cv2.VideoCapture(0)

while True:
    # Read the current frame from the video stream
    ret, frame = cap.read()

    # Show the current frame in a window
    cv2.imshow('Live Video Feed', frame)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release the capture and close the window
cap.release()
cv2.destroyAllWindows()