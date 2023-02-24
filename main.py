#import cv2

# Capture video from USB webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    cv2.imshow('Live Video Feed', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()