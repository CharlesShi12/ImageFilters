from image import *
import math

def create_init_list(k):
    # Creates a random list of colors using random_color from image_utils based on the k parameter which
    # sets the length of the list of random colors
    initial_means_list = []
    for i in range(0, k):
        initial_means_list.append(random_color())
    return initial_means_list

def distance(c1, c2):
    # Computes the distance of two given tuples, the shorter the value return, the closer the two pixels are and vice versa
    distance = math.sqrt((((c1[0] - c2[0]) ** 2) + ((c1[1] - c2[1]) ** 2) + ((c1[2] - c2[2]) ** 2)))
    return distance

def closest_label(pixel, means_list):
    # Finds the closest label or cluster of colors in the means_list for a single pixel which is represented as a 3-tuple
    index = 0
    smallestdistance = distance(pixel, means_list[0])
    for i in range(0, len(means_list)):
        if distance(pixel, means_list[i]) < smallestdistance:
            smallestdistance = distance(pixel, means_list[i])
            index = i
    return index

def average_color(list_colors):
    # Calculates the average colors (3-tuple R G B) in a list of colors represented by tuples
    total1 = 0
    total2 = 0
    total3 = 0
    for i in range(0, len(list_colors)):
        total1 += list_colors[i][0]
        total2 += list_colors[i][1]
        total3 += list_colors[i][2]
    if len(list_colors) == 0:
        return (0,0,0)
    return (total1//len(list_colors), total2//len(list_colors), total3//len(list_colors))

def update_assignments(image, means_list):
    # Updates the label assignments based on the closest labels in means_list for each pixel of image when given the
    # means_list and image
    width, height = get_width_height(image)
    label_assignment = [[0] * height for z in range(width)]
    for i in range(0, height):
        for j in range(0, width):
            label_assignment[j][i] = closest_label(image[j][i], means_list)
    return label_assignment

def update_means_list(image, labels_list, means_list):
    # Updates the means_list based on the image, updated assignments (labels_list), and means_list and returns an
    # updated means_list
    width, height = get_width_height(image)
    lst = [[] * len(means_list) for z in range(len(means_list))]
    for i in range(0, len(means_list)):
        for j in range(0, height):
            for k in range(0, width):
                if labels_list[k][j] == i:
                    image_pixel = image[k][j]
                    lst[i].append(image_pixel)
        average_list_color = average_color(lst[i])
        means_list[i] = average_list_color
    return means_list

def k_means(image, k):
    # Performs the k_means computation on an image through image and k
    means_list = create_init_list(k)
    test_labels_list = None
    label_list = update_assignments(image, means_list)
    while test_labels_list != label_list :
        test_labels_list = update_assignments(image, means_list)
        means_list = update_means_list(image, test_labels_list, means_list)
        label_list = update_assignments(image, means_list)
    return (means_list, label_list)
