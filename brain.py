# Recreating in Python

import cv2
import numpy as np

class InputSize:
    def input_one(self):
        print("Input image size: (recommended 640 by 590)")
        self.a, self.b = map(int, input().split())
        print("Updated Image size")

    def input_two(self):
        print("Input Pixel colors for contrast: (recommended 255,255,255)")
        self.e, self.f, self.g = map(int, input().split())
        print("Updated pixel colors")

def main():
    obj1 = InputSize()
    obj2 = InputSize()
    obj1.input_one()
    obj2.input_two()
    c, d, p, q, r = obj1.a, obj1.b, obj2.e, obj2.f, obj2.g
    
    # Load input image
    image = cv2.imread("C:/Users/Rishi/OneDrive/Pictures/brain.png")
    
    # Resize image
    newSize = (c, d)
    image = cv2.resize(image, newSize)
    
    # Convert image to grayscale
    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply top hat filter
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15, 15))
    topHat = cv2.morphologyEx(grayImage, cv2.MORPH_TOPHAT, kernel)
    
    # Blur image
    topHat = cv2.GaussianBlur(topHat, (5, 5), 0)
    
    # Apply thresholding for segmenting
    _, thresholded = cv2.threshold(topHat, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # Compute distance transform
    thresholded = np.uint8(thresholded)
    dist = cv2.distanceTransform(thresholded, cv2.DIST_L2, 3)
    
    # Find local maxima in distance transform
    localMaxima = cv2.dilate(thresholded, None)
    localMaxima = (thresholded == localMaxima)
    localMaxima = np.uint8(localMaxima)
    
    # Find markers for watershedding
    _, markers = cv2.connectedComponents(localMaxima)
    
    # Apply watershedding
    markers = cv2.watershed(image, markers)
    
    # Display output
    output = np.zeros(image.shape, dtype=np.uint8)
    for i in range(markers.shape[0]):
        for j in range(markers.shape[1]):
            index = markers[i, j]
            if index == -1:
                output[i, j] = [255, 255, 255]
            elif index == 1:
                output[i, j] = [p, q, r]
    
    cv2.imshow("Original Image", image)
    cv2.imshow("Thresholded Image", thresholded)
    cv2.imshow("Output", output)
    cv2.waitKey(0)
    
    originalFileName = "./output/original.png"
    cv2.imwrite(originalFileName, image)
    
    thresholdedFileName = "./output/thresholded.png"
    cv2.imwrite(thresholdedFileName, thresholded)
    
    outputFileName = "./output/output.png"
    cv2.imwrite(outputFileName, output)

if __name__ == "__main__":
    main()
