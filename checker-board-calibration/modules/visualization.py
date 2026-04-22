import matplotlib.pyplot as plt
import cv2
import numpy as np

def draw_3d_cube(image, pts_2d):
    """Draws a green wireframe cube based on projected 2D points."""
    edges = [
        (0,1), (1,2), (2,3), (3,0), # Bottom
        (4,5), (5,6), (6,7), (7,4), # Top
        (0,4), (1,5), (2,6), (3,7)  # Pillars
    ]
    
    img_out = image.copy()
    for (i, j) in edges:
        cv2.line(img_out, tuple(pts_2d[i]), tuple(pts_2d[j]), (0, 255, 0), 2)
    return img_out

def show_result(image, title="3D Reconstruction"):
    plt.figure(figsize=(10, 7))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()