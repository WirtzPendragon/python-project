import pyautogui
import cv2
import numpy as np
import time

resolution = (1920, 1080)
codec = cv2.VideoWriter_fourcc(*"XVID")
filename = "Recording.avi"
fps = 30.0
out = cv2.VideoWriter(filename, codec, fps, resolution)
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live", 480, 270)

# prev_time = time.time()
frames = 0
start_time = time.time()

while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    x, y = pyautogui.position()
    cv2.circle(frame, (x, y), 10, (255, 255, 255), -1),
    cv2.circle(frame, (x, y), 8, (0, 0, 0), -1)
    
    out.write(frame)
    cv2.imshow("Live", frame)
    
    frames += 1
    now = time.time()
    if now - start_time >= 1:
        print("FPS: ", frames)
        frames = 0
        start_time = now
        
    if cv2.waitKey(1) == ord('q'):
        break
    
out.release()
cv2.destroyAllWindows()