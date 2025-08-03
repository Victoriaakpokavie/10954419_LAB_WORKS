pixel_value = 180        #grayscale image pixel value
threshold = 150          #threshold for binary thresholding

# Apply binary thresholding 
if pixel_value > threshold:
    new_pixel_value = 255
else:
    new_pixel_value = 0

print(f"Original Pixel Value: {pixel_value}")
print(f"New Pixel Value after Thresholding: {new_pixel_value}")
