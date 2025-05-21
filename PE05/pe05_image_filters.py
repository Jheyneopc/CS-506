import matplotlib.pyplot as plt
from PIL import Image, ImageOps, ImageFilter, ImageEnhance

# Open the input image**
img = Image.open("PE05-input.jpg")

# Original image*
plt.subplot(2, 2, 1)
plt.title("Original")
plt.imshow(img, cmap="gray")
#Number of people visible: 2

# Histogram Equalization*
equalized = ImageOps.equalize(img)
plt.subplot(2, 2, 2)
plt.title("Equalized")
plt.imshow(equalized, cmap="gray")
#Trees identified: 4 trunks (they are clearly visible along the left sidewalk)

# Unsharp Mask for clarity**
sharpened = equalized.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))
plt.subplot(2, 2, 3)
plt.title("Unsharp Mask")
plt.imshow(sharpened, cmap="gray")
#Windows on the 2nd floor of building 1 (labeled "1"): 2 windows are clearly visible

# Slight contrast boost**
enhanced = ImageEnhance.Contrast(sharpened).enhance(1.2)
plt.subplot(2, 2, 4)
plt.title("Final Enhanced")
plt.imshow(enhanced, cmap="gray")
#Windows on building 2 (label 2): about 3

# Save output**
enhanced.save("PE05-output.jpg")

# Show all plots**
plt.tight_layout()
plt.show()


#Below are all the comments: 
##1. Number of people visible: 2
##2. Trees identified: 4 trunks (they are clearly visible along the left sidewalk)
##3. Windows on the 2nd floor of building 1 (labeled "1"): 2 windows are clearly visible
##4. Windows on building 2 (label 2): about 3
