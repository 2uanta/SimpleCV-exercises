from SimpleCV import Image
img = Image("chicago.png")
img.save()
# Now save as .jpg
img.save("chicago.jpg")
# Re-saves as .jpg
img.save()