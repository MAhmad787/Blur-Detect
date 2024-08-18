import os
import cv2

all_files = os.listdir("image_dir")
images = []
image_types = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp']
for x in all_files:
    if x.endswith(tuple(image_types)):
        images.append(x)
threshold = 100
for img in images:
    image = cv2.imread("image_dir/"+img, cv2.IMREAD_GRAYSCALE)
    if image is not None:
        laplacian_var = cv2.Laplacian(image, cv2.CV_64F).var()
        if laplacian_var < threshold:
            cv2.namedWindow(img, cv2.WINDOW_NORMAL)
            cv2.resizeWindow(img, 300, 300)
            cv2.moveWindow(img, 200, 100 )
            cv2.imshow(img, image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            print(img + " is a blurred image")
            print("Laplacian Value")
            print(laplacian_var)
        else:
            print(img + " is not a blurred image")
            print("Laplacian Value")
            print(laplacian_var)
    else: 
        print("Image Not Found")
