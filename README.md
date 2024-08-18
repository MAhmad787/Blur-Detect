# Image Blur Detection using OpenCV and Laplacian Method

## Overview

This project demonstrates how to detect blurry images using OpenCV in Python, utilizing the Laplacian variance method. The Laplacian method highlights regions of rapid intensity change in an image. By calculating the variance of these changes, you can determine whether an image is sharp or blurry. 

## Features

- **Detect Blurry Images**: Identifies whether images are blurry based on the Laplacian variance.
- **Display Results**: Visualizes blurry images and prints diagnostic information.

## Requirements

- Python 3.x
- OpenCV (`opencv-python`)

You can install the required package using pip:

```bash
pip install opencv-python

Make a directory and paste all of your images in it

```bash
mkdir image_dir

## How It Works

1. **Load Image**: 
   - The image is loaded in grayscale format to simplify the blur detection process. Grayscale images are used because color information is not necessary for detecting blur, and working with a single channel is computationally more efficient.

2. **Compute Laplacian**:
   - The Laplacian operator is applied to the grayscale image. This operator is a second-order derivative that highlights regions with rapid changes in intensity, which correspond to edges in the image.

3. **Calculate Variance**:
   - The variance of the Laplacian values is computed. Variance measures the spread of the Laplacian values. In a sharp image, there are many edges with significant intensity changes, resulting in high variance. In a blurry image, there are fewer and less pronounced edges, leading to low variance.

4. **Thresholding**:
   - The calculated variance is compared to a pre-defined threshold. This threshold determines whether the image is considered blurry. If the variance is below the threshold, the image is classified as blurry. If it is above, the image is considered sharp. Here I have used the general value as hundred, but it can also me changed as required.

5. **Display Results**:
   - For images classified as blurry, a window displaying the image can be shown, and diagnostic information such as the variance value is printed. This helps in visualizing and confirming the results of the blur detection process.

