from flask import Flask, render_template, Response
import cv2
import time
import pymongo
from pymongo import MongoClient
import gridfs

app=Flask(__name__)
client=MongoClient()
client=MongoClient("mongodb://mongo:Az9PXoD6MNZrOOe6clcV@containers-us-west-144.railway.app:7025")

db=client['eyedetection']
app.secret_key = 'password'
users=db['eyevdo']

def get_camera():
    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
    
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            detector = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
            eye_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')

            faces=detector.detectMultiScale(frame,1.1,7)
            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            for (x,y,w,h) in faces:
                cv2.rectangle (frame,(x,y),(x+w,y+h),(255,0,0),2)
                roi_gray=gray[y:y+h,x:x+w]
                roi_color=frame[y:y+h,x:x+w]
                eyes=eye_cascade.detectMultiScale(roi_gray,1.1,3)
                for (ex,ey,ew,eh) in eyes:
                    cv2.rectangle (roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            out.write(frame)
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            time.sleep(0.03)
    out.release()
    cap.release()

    

@app.route('/') 
def main():
    return render_template("main.html")

@app.route('/hello') 
def hello():
    name="output.avi"
    filedata=open(name,'rb')
    data=filedata.read()
    fs=gridfs.GridFS(db)
    fs.put(data,filename=name)
    return render_template("main.html")

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/video_feed')
def video_feed():
    return Response(get_camera(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)