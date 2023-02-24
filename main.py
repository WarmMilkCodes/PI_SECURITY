import cv2

# Capture video from USB webcam
cap = cv2.VideoCapture(0)

# Set display size
display_width  = 640
display_height = 480

# Set intial brightness level (between 0 and 1)
brightness = 0.5

while True:
    # Read the current frame from the video stream
    ret, frame = cap.read()

    # Adjust the brightness of the frame
    frame = cv2.addWeighted(frame, brightness, 0, 0, 0, 0)

    # Resize the frame to the selected size
    frame = cv2.resize(frame, (display_width, display_height))

    # Add a text label showing ther current brightness level
    text = f'Brightness: {brightness:.1f}'
    cv2.putText(frame, text, (10,30), cv2.FRONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

    # Show the current frame in a window
    cv2.imshow('Live Video Feed', frame)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) == ord('q'):
        break

    # Increase the brightness if the '+' key is pressed
    elif cv2.waitKey(1) == ord('+'):
        brightness += 0.1
        if brightness > 1.0:
            brightness = 1.0
        # Update text label
        text = f'Brightness: {brightness:.1f}'

    # Decrease the brightness if the '-' key is pressed
    elif cv2.waitKey(1) == ord('-'):
        brightness -= 0.1
        if brightness < 0.0:
            brightness = 0.0
        # Update text label
        text = f'Brightness: {brightness:.1f}'

# Release the capture and close the window
cap.release()
cv2.destroyAllWindows()