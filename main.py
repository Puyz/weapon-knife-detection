import cv2
from ultralytics import YOLO

model = YOLO('Run/weights/best_g2.pt')

video_path = "gun.mp4"
cap = cv2.VideoCapture(video_path)

while cap.isOpened():
    
    success, frame = cap.read()

    if success:
        results = model(frame)
        annotated_frame = results[0].plot()
        cv2.imshow("Bicak ve atesli silah tespiti", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
