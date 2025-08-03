import cv2                     # Import the OpenCV library for image processing
import matplotlib.pyplot as plt  # Import matplotlib for image visualization

# Load the image from file
image1 = cv2.imread('c:/Users/Aku/OneDrive/Desktop/lab work/10954419_LAB_WORKS/IMG_0211.JPG')

# Convert the image from BGR (OpenCV default) to RGB (for proper color display)
image_rgb = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)

# Convert the image to grayscale (single channel intensity image)
gray_image = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2GRAY)

# Display the image using matplotlib
plt.imshow(image_rgb)         # Show the RGB image
plt.title("Loaded Image")     # Set the image title
plt.axis('off')               # Hide axis ticks and labels
plt.show()                    # Render the image window
# Display the grayscale image
plt.imshow(gray_image, cmap='gray')  # Use 'gray' colormap for single-channel images
plt.title("Grayscale Image")
plt.axis('off')
plt.show()

# Saving the grayscale image as photo_gray.jpg
cv2.imwrite('photo_gray.jpg', gray_image) 
