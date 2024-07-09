import cv2
import numpy as np

# Load the image
image_path = 'C:\Users\Ashutosh Das\OneDrive\Desktop\Gigazit\image.jpg'
image = cv2.imread(image_path)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply GaussianBlur to reduce noise and improve contour detection
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Perform edge detection
edged = cv2.Canny(blurred, 50, 150)

# Find contours for rectangle detection
contours, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Function to calculate area of a rectangle
def calculate_rectangle_area(contour):
    x, y, w, h = cv2.boundingRect(contour)
    area = w * h
    return area, (x, y, w, h)

# Detect rectangles and calculate their areas
rectangle_areas = []
for contour in contours:
    area, (x, y, w, h) = calculate_rectangle_area(contour)
    rectangle_areas.append((area, (x, y, w, h)))
    # Draw rectangle around detected object
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

# # Detect circles using HoughCircles
# circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=1.2, minDist=20, param1=50, param2=30, minRadius=10, maxRadius=100)

# circle_areas = []
# if circles is not None:
#     circles = np.round(circles[0, :]).astype("int")
#     for (x, y, r) in circles:
#         area = np.pi * (r ** 2)
#         circle_areas.append((area, (x, y, r)))
#         # Draw circle around detected object
#         cv2.circle(image, (x, y), r, (255, 0, 0), 2)

# Display the result
cv2_imshow(image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Print detected rectangle areas
print("Rectangular Objects:")
for i, (area, (x, y, w, h)) in enumerate(rectangle_areas):
    print(f"Object {i + 1}:")
    print(f"  Location: (x: {x}, y: {y}, width: {w}, height: {h})")
    print(f"  Surface Area: {area} square pixels")

# # Print detected circle areas
# print("\nCircular Objects:")
# for i, (area, (x, y, r)) in enumerate(circle_areas):
#     print(f"Object {i + 1}:")
#     print(f"  Center: (x: {x}, y: {y}), Radius: {r}")
#     print(f"  Surface Area: {area:.2f} square pixels")

# Save the output image with rectangles and circles drawn
output_path = 'C:\Users\Ashutosh Das\OneDrive\Desktop\Gigazit'
cv2.imwrite(output_path, image)
print(f"Output image saved to {output_path}")