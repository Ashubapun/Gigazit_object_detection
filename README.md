Object Detection and Surface Area Calculation Script

1. Overview
This script detects rectangular and circular objects in an image, calculates their surface areas, and draws bounding shapes around them. The calculated areas and the shape details are printed to the console, and the annotated image is saved.

2. Requirements
- Python 
- OpenCV (cv2)
- NumPy

3. Approach

3.1. Image Preprocessing:
   - Convert the image to grayscale.
   - Apply GaussianBlur to reduce noise.
   - Perform edge detection using the Canny edge detector.
3.2. Contour Detection:
   - Find contours in the edge-detected image to identify rectangular objects.
3.3. Circle Detection:
   - Use the Hough Circle Transform to detect circular objects in the grayscale image.
3.4. Area Calculation:
   - For rectangles: Calculate the bounding rectangle for each contour and compute the surface area.
   - For circles: Calculate the area using the radius detected by the Hough Circle Transform.
3.5. Visualization:
   - Draw bounding rectangles and circles around detected objects.
   - Display the annotated image and save it.

