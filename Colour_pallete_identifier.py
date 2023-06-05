# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hYCuQ9sB0EuOfkY4ceK1up87e3MdTUA1
"""

import cv2
import numpy as np
from sklearn.cluster import KMeans

# Function to generate a color palette from an image
def generate_palette(image_path, num_colors):
    # Load the image using OpenCV
    image = cv2.imread("/content/ic_launcher.png")

    # Reshape the image to a 2D array of pixels
    pixels = image.reshape(-1, 3)

    # Perform k-means clustering to extract dominant colors
    kmeans = KMeans(n_clusters=num_colors)
    kmeans.fit(pixels)

    # Get the RGB values of the cluster centers
    colors = kmeans.cluster_centers_

    # Convert the colors to integer values
    colors = colors.astype(int)

    return colors

# Example usage
image_path = "path/to/your/image.jpg"  # Replace with the actual image file path
num_colors = 5

# Generate and display a color palette
palette = generate_palette(image_path, num_colors)

print("Color Palette:")
for color in palette:
    print(color)

