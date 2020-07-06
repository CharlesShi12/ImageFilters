from image_utils import *
from k_means import *
# Charles Shi CSCI 1913: Daniel Kluver

if __name__ == "__main__":
    file = input("Image file: ")
    k = int(input("K means: "))
    output_file = input("Output File Name: ")
    image = read_ppm(file)
    means, labels = k_means(image, k)
    width, height = get_width_height(image)
    new_image = [[0] * height for z in range(width)]
    for i in range(0, width):
        for j in range(0, height):
            new_image[i][j] = means[labels[i][j]]
    save_ppm(output_file + '.ppm', new_image)







