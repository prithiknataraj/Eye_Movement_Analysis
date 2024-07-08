#Eye Movement Analysis
## Flask Eye Detection and Video Feed

This Flask application provides a real-time video feed with eye detection using OpenCV. It captures video from the camera, detects faces and eyes, and streams the processed video to a web interface.

## Features

- **Video Feed**: Displays real-time video from the camera.
- **Face and Eye Detection**: Uses Haar cascades for detecting faces and eyes in the video stream.
- **MongoDB Integration**: Stores processed video files in MongoDB using GridFS.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python (version 3.x)
- Flask
- OpenCV (cv2)
- pymongo
- GridFS

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. Install dependencies:

   ```bash
   pip install flask opencv-python pymongo
   ```

3. Set up MongoDB:
   - Install MongoDB and start the MongoDB service.
   - Ensure MongoDB is accessible and replace the MongoDB URI in `app.py` with your MongoDB connection string.

4. Run the application:

   ```bash
   python app.py
   ```

5. Access the application:
   - Open a web browser and go to `http://localhost:5000` to view the video feed and eye detection in action.

## Usage

- **/index**: Displays a basic HTML page.
- **/video_feed**: Streams the real-time video feed with eye detection.
- **/hello**: Stores the processed video in MongoDB using GridFS.

## Files

- **app.py**: Flask application script that sets up routes and handles video streaming and processing.
- **main.html**: Main HTML template for displaying the video feed.
- **index.html**: Index HTML template for basic page display.

## Notes

- Make sure your environment has the necessary camera access permissions.
- Adjust the Haar cascade paths (`haarcascades/haarcascade_frontalface_default.xml` and `haarcascades/haarcascade_eye.xml`) as per your setup.

## Credits

- Flask: [Flask Documentation](https://flask.palletsprojects.com/)
- OpenCV: [OpenCV Documentation](https://opencv.org/)
- MongoDB: [MongoDB Documentation](https://docs.mongodb.com/)
