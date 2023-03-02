from PIL import Image

# Define the RGB values of the colours
colourBlack = (46, 47, 49)
colourCream = (240, 232, 185)
colourRed = (182, 49, 54)
colourWhite = (236, 237, 237)
colourDarkGrey = (131, 136, 138)
colour6 = (128, 0, 128)
colour7 = (255, 165, 0)
colour8 = (0, 128, 128)
colour9 = (255, 192, 203)

# Load the image
image = Image.open("inputimage.png")

# Get the dimensions of the image
width, height = image.size

# Initialize counters for each colour
countBlack = 0
countCream = 0
countRed = 0
countWhite = 0
countDarkGrey = 0
count6 = 0
count7 = 0
count8 = 0
count9 = 0

# Loop through each pixel in the image
for x in range(width):
    for y in range(height):
        # Get the RGB value of the current pixel
        pixel = image.getpixel((x, y))
        
        # Check which colour the pixel belongs to and increment the corresponding counter
        if pixel == colourBlack:
            countBlack += 1
        elif pixel == colourCream:
            countCream += 1
        elif pixel == colourRed:
          countRed += 1
        elif pixel == colourWhite:
            countWhite += 1
        elif pixel == colourDarkGrey:
            countDarkGrey += 1
        elif pixel == colour6:
            count6 += 1
        elif pixel == colour7:
            count7 += 1
        elif pixel == colour8:
            count8 += 1
        elif pixel == colour9:
            count9 += 1

if countBlack > 0:
    print("Number of Black Pixels:", countBlack)
if countCream > 0:
    print("Number of pixels of Cream Pixels:", countCream)
if countRed > 0:
    print("Number of pixels of Red Pixels:", countWhite)
if countWhite > 0:
    print("Number of pixels of White pixels:", countWhite)
if countDarkGrey > 0:
    print("Number of pixels of  Dark Grey Pixels:", countDarkGrey)
if count6 > 0:
    print("Number of pixels of colour6 (purple):", count6)
if count7 > 0:
    print("Number of pixels of colour7 (orange):", count7)
if count8 > 0:
    print("Number of pixels of colour 8 (teal):", count8)
if count9 > 0:
    print("Number of pixels of colour 9 (pink):", count9)