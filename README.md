## Image Filters using Python
A Python project that uses machine learning, specifically the k-means algorithm, to filter images reducing it down to a few core colors.

## General Technical Description
This project relies on certain image formatting and the k-means machine learning algorithm. I used the plain (P3) PPM raster image format to represent inputted images and a tuple of three integers from 0 to 255 (Red, Green, Blue) to represent the colors/pixels of an inputted image. The k-means algorithm begins with randomly generated colors that represent the centers of clusters of colors (completely random colors with no relation to the inputted image). Then it takes each pixel in the image and assigns it to the most similar color cluster. After that's done, the algorithm will average out the pixels in each color cluster and set that averaged color as the new color to represent the center of the color cluster. The algorithm repeats itself until it finds a combination of color clusters that cannot be improved. Finally, after the algorithm's obtained the most accurate clusters of colors, it will take each pixel in the original image, find the closest color cluster, and set the center color of that color cluster to the pixel in a new image. This new image will be outputted with only the center colors in the color clusters.

## Demonstration
Video demonstration of this algorithm is linked here: https://youtu.be/hubdoUQ0QmY. 

## Tech/Framework used
Built with 
* Python

## Features
* Reduces an image down to a few core colors
* Allows for users to chose the amount of colors the image is reduced to
* Outputs a new and updated .ppm image

## Installations
Run this command in your terminal:
```
git clone https://github.com/CharlesShi12/ImageFilters.git
```
Import the folder into your respected IDE and run the main.py file. 

## License
MIT © Charles Shi

