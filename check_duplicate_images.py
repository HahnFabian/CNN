import os

identical_images = []


def duplicate_images(path, path_dataset):
    if os.path.isdir(path):
        length = len([img for img in os.listdir(path)])
        for n, images in enumerate(os.listdir(path)):
            print(f"[CHECKING IMAGE {n+1} / {length}]")
            duplicate_images_start(os.path.join(path, images), path_dataset)
        print()
        print(f"[FOUND {len(identical_images)} DUPLICATES]")
        print(identical_images) if len(identical_images) > 0 else ...
        if len(identical_images) > 0:
            delete_duplicates() if str(input("DELETE DUPLICATE IMAGES? (y/n) > ")) == "y" else print("IMAGES WERE NOT REMOVED")
    else:
        duplicate_images_start(path, path_dataset)


def duplicate_images_start(path_image, path_dataset):
    length = len([dir for dir in os.listdir(path_dataset) if os.path.isdir(os.path.join(path_dataset, dir))])
    if length > 0:
        for n, dirs in enumerate(os.listdir(path_dataset)):
            print(f"[CHECKING FOLDER: {dirs} - {n+1} / {length}]")
            duplicate_images_check(path_image, os.path.join(path_dataset, dirs))
    else:
        duplicate_images_check(path_image, path_dataset)


def duplicate_images_check(path_image, path_dataset):
    check = False
    for images in os.listdir(path_dataset):
        if open(path_image, "rb").read == open(os.path.join(path_dataset, images), "rb").read():
            print('\x1b[0;30;41m' + "---FOUND IDENTICAL IMAGE---" + '\x1b[0m')
            print('\x1b[0;30;41m' + f"IMAGE NAME: {images}" + '\x1b[0m')
            print('\x1b[0;30;41m' + f"PATH (image-folder): {path_image}" + '\x1b[0m')
            print('\x1b[0;30;41m' + f"PATH (dataset): {os.path.join(path_dataset, images)}" + '\x1b[0m')
            identical_images.append(path_image)
            check = True
    print("NO IMAGES FOUND") if not check else print("IMAGES FOUND")
    print()


def delete_duplicates():
    print()
    for image in identical_images:
        os.remove(image)
        print(f"SUCCESSFULLY REMOVED {image}")


duplicate_images(r"G:\Python\data\eval_images\turtle", r"G:\Python\data\10_animals\turtle")
