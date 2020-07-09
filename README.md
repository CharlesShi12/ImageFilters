# Image Filters using Python
A Python project that uses machine learning, specifically the k-means algorithm, to filter images reducing it down to a few core colors.

A special thanks to Daniel Kluver.

# General Technical Description
This project relies on certain image formatting and the k-means machine learning algorithm. I used the plain (P3) PPM raster image format to represent inputted images and a tuple of three integers from 0 to 255 (Red, Green, Blue) to represent the colors/pixels of an inputted image. The k-means algorithm begins with randomly generated colors that represent the centers of clusters of colors (completely random colors with no relation to the inputted image). Then it takes each pixel in the image and assigns it to the most similar color cluster. After that's done, the algorithm will average out the pixels in each color cluster and set that averaged color as the new color to represent the center of the color cluster. The algorithm repeats itself until it finds a combination of color clusters that cannot be improved. Finally, after the algorithm's obtained the most accurate clusters of colors, it will take each pixel in the original image, find the closest color cluster, and set the center color of that color cluster to the pixel in a new image. This new image will be output with only the colors in the color clusters. To understand this, let's use an example.

Imagine you inputted an image full of purple, blue, and red. You set the k-means clustering to three which means you want three clusters of colors. The algorithm will begin with completely random colors that represent the centers of clusters of colors: let's say, yellow, pink, and green. Then it takes all of the pixels in the inputted image and matches it with the closest color cluster (in our case, still yellow, pink, or green). After averaging the pixels in the clusters, setting the new cluster center, and repeating the process over and over again until the clusters can't get any more accurate, the algorithm finally gets something along the lines of purple, blue, and red as the final color centers for the final cluster of colors. Then the algorithm takes each of the pixels in the original image and makes the pixel of a new image either purple, blue, or red depending on how close the original pixel was. Then it outputs the new image. So essentially, if you want k-means of three, then your final image will only consist of the three most core colors of your image.

# Demonstration
Video demonstration of this algorithm is linked here: https://drive.google.com/file/d/1HNuDzAPNlOetvbbbMU4DAZ36aqkKSqja/view?usp=sharing

# What I Learned
I learned the k-means machine learning algorithm: how to design it, when to implement it, and what it does. I also learned how to represent images in certain formats using different types of data representations. Finally, I became very familiar with some of Python's data structures and useful functions. 
