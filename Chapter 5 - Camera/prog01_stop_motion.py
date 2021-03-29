import cv2, time, subprocess
# from gpiozero import Button

cap = cv2.VideoCapture(0)
# button = Button(2)
nframe = 0

while True:
    # button.wait_for_press()
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    
    if cv2.waitKey(100) & 0xFF == ord('p'):
        nframe = nframe + 1
        print(f'snaphot {nframe:03d} done!')
        cv2.imwrite(f'animation/frame{nframe:03d}.jpg', frame)
    
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
    time.sleep(0.2)

cap.release()
# Bezarunk minden ablakot, amit a program megnyitott
cv2.destroyAllWindows()

subprocess.call('ffmpeg -r 1 -i animation/frame%03d.jpg -qscale 1 animation.mp4')
