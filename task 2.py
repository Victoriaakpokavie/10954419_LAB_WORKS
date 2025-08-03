import cv2                     # Import the OpenCV library for image processing
import matplotlib.pyplot as plt  # Import matplotlib for image visualization
# Load the image from file
image1 = cv2.imread('c:/Users/Aku/OneDrive/Desktop/lab work/10954419_LAB_WORKS/IMG_0211.JPG')

# Convert the image from BGR (OpenCV default) to RGB (for proper color display)
image_rgb = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)

# Convert the image to grayscale (single channel intensity image)
gray_image = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

# Convert the image to HSV
hsv_image = cv2.cvtColor(image1, cv2.COLOR_BGR2HSV)

# Convert the image to LAB
lab_image = cv2.cvtColor(image1, cv2.COLOR_BGR2LAB)

# Display the grayscale image
plt.imshow(gray_image, cmap='gray')  # Use 'gray' colormap for single-channel images
plt.title("Grayscale Image")
plt.axis('off')
plt.show()

# Display the image using matplotlib
plt.imshow(hsv_image)         # Show the HSV image
plt.title("HSV Image")     # Set the image title
plt.axis('off')               # Hide axis ticks and labels
plt.show()  

# Display the image using matplotlib
plt.imshow(lab_image)         # Show the LAB image
plt.title("LAB Image")     # Set the image title
plt.axis('off')               # Hide axis ticks and labels
plt.show()  

cv2.imwrite("photo_grayscale.jpg", gray_image)
cv2.imwrite("photo_hsv.jpg", hsv_image)
cv2.imwrite("photo_lab.jpg", lab_image)

gray = cv2.imread(
    "c:/Users/Aku/OneDrive/Desktop/lab work/10954419_LAB_WORKS/photo_grayscale.jpg",
    cv2.IMREAD_GRAYSCALE
)

# Calculate and plot histogram
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
plt.figure(figsize=(8, 4))
plt.title('Grayscale Histogram')
plt.xlabel('Pixel Intensity (0–255)')
plt.ylabel('Frequency')
plt.plot(hist, color='black')
plt.xlim([0, 256])
plt.grid(True)
plt.show()