from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)
#print(cap.isOpened())

@app.route('/')
def index():
    # rendering webpage
    return render_template('index.html')

def gen(camera):
    while True:
        #get camera frame
        ret, frame = # olvasd ki a kepet a camera objektumbol
        ret, frame = cv2.imencode('.jpg', frame)
        frame = frame.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    cap = # inicializald a camerat, ha linux alatt vagy, akkor '/dev/video0' a bemeno parameter
    cap.open(0)
    return Response(gen(cap),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    # defining server ip address and port
    app.run(host='0.0.0.0',port='5000', debug=True)
