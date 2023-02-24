import cv2

# Capture video from USB webcam
cap = cv2.VideoCapture(0)

# Set display size
display_width  = 640
display_height = 480

# Set intial brightness level (between 0 and 1)
brightness = 0.5

# Load the Haar Cascade classifier for facial detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    # Read the current frame from the video stream
    ret, frame = cap.read()

    # Adjust the brightness of the frame
    frame = cv2.addWeighted(frame, brightness, 0, 0, 0, 0)

    # Resize the frame to the selected size
    frame = cv2.resize(frame, (display_width, display_height))

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detects faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Add a text label showing ther current brightness level
    text = f'Brightness: {brightness:.1f}'
    cv2.putText(frame, text, (10,30), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 2)

    # Show the current frame in a window
    cv2.imshow('Cox Security Video Feed', frame)

    # Wait for a key press
    key = cv2.waitKey(1)

    # Exit the loop if the 'q' key is pressed
    if key == ord('q'):
        break

    # Increase the brightness if the '+' key is pressed
    if key == ord('1'):
        brightness += 0.1
        if brightness > 1.0:
            brightness = 1.0
        # Update text label
        text = f'Brightness: {brightness:.1f}'

    # Decrease the brightness if the '-' key is pressed
    if key == ord('2'):
        brightness -= 0.1
        if brightness < 0.0:
            brightness = 0.0
        # Update text label
        text = f'Brightness: {brightness:.1f}'

# Release the capture and close the window
cap.release()
cv2.destroyAllWindows()