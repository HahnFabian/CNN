import os

def duplicate_images(path_image, path_dataset):
    dirs = [dir for dir in os.listdir(path_dataset) if os.path.isdir(os.path.join(path_dataset, dir))]
    if len(dirs) > 0:
        for dirs in os.listdir(path_dataset):
            print(f"CHECKING FOLDER: {dirs}")
            duplicate_images_check(path_image, os.path.join(path_dataset, dirs))
    else:
        duplicate_images_check(path_image, path_dataset)

def duplicate_images_check(path_image, path_dataset):
    check = False
    for images in os.listdir(path_dataset):
        if open(path_image, "rb").read() == open(os.path.join(path_dataset, images), "rb").read():
            print("---FOUND IDENTICAL IMAGE---")
            print(f"IMAGE NAME: {images}")
            print(f"PATH: {os.path.join(path_dataset, images)}")
            check = True
    print("NO IMAGES FOUND") if not check else print("IMAGES FOUND")


duplicate_images("G:/Python/data/img_from_google/14.jpg", "G:/Python/data/animals")

