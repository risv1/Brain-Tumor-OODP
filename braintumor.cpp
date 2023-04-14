#include <iostream>
#include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;

int main() {
    // Load input image
    Mat image = imread("C:/Users/Rishi/OneDrive/Pictures/images.png"); // Change your filepath after downloading the original_image.png file

    // Resize image to a smaller size
    Size newSize(640, 480);
    resize(image, image, newSize);

    // Convert image to grayscale
    Mat grayImage;
    cvtColor(image, grayImage, COLOR_BGR2GRAY);

    // Blur image
    GaussianBlur(grayImage, grayImage, Size(5, 5), 0);

    // Apply thresholding for segmenting
    Mat thresholded;
    threshold(grayImage, thresholded, 0, 255, THRESH_BINARY + THRESH_OTSU);

    // Show original image and the thresholded image
    imshow("Original Image", image);
    imshow("Thresholded Image", thresholded);
    waitKey(0);

    return 0;
}
