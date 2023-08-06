from PIL import Image
import os

formats = ["JPEG", "JPG", "PNG", "BMP", "GIF"]
false_images = []
broken_images = []

count_false_images = 0
count_broken_images = 0
count_small_size = 0

def search(path):
    global dirs
    list_dirs = [dir for dir in os.listdir(path) if os.path.isdir(os.path.join(path, dir))]
    if len(list_dirs) > 0:
        for n, dirs in enumerate(os.listdir(path)):
            print()
            print("-------------------------------------------")
            print(f"NOW IN DIR: {dirs} - {n+1}/{len(list_dirs)}")
            new_path = os.path.join(path, dirs)
            search_func(new_path)
    else:
        dirs = path
        search_func(path)
    print()
    print(f"FOUND [{count_false_images}] IMAGES NOT MATCHING THE FORMATS AND [{count_broken_images}] FILES WHICH WERE UNABLE TO BE ACCESSED")
    print(f"FOUND [{count_small_size} / {count_images}] IMAGES WITH A FILE SIZE OF LESS THAN 5KB")
    if len(false_images) > 0:
        remove(false_images) if bool(input("REMOVE FILES WITH FALSE FORMATS? [True/False] > ")) else print("TOOL DID NOT DELETE ANY DATA")
    if len(broken_images) > 0:
        remove(broken_images) if bool(input("REMOVE BROKEN FILES? [True/False] > ")) else print("TOOL DID NOT DELETE ANY DATA")

def search_func(new_path):
    global count_false_images, count_broken_images, count_small_size, count_images
    count_images = 0
    for images in os.listdir(new_path):
        count_images += 1
        try:
            img = Image.open(os.path.join(new_path, images))
            if not img.format in formats:
                print(img.format + " --> " + dirs, images)
                false_images.append(os.path.join(new_path, images))
                count_false_images += 1
        except:
            print(f"UNABLE TO OPEN FILE -- DIR: {dirs} -- FILE: {images}")
            broken_images.append(os.path.join(new_path, images))
            count_broken_images += 1
        try:
            size = os.path.getsize(os.path.join(new_path, images))
            if size < 5000:
                count_small_size += 1
        except:
            print(f"UNABLE TO CALCULATE SIZE OF FILE {images} in {dirs}")



def remove(type_of_images):
    for x, item in enumerate(type_of_images):
        if os.path.isfile(item):
            os.remove(item)
            print(f"REMOVED FILE [{item}] > {x+1}/{len(type_of_images)}")

search(r"G:\Python\data\pre\c499fc7b-5697-4910-93f0-dce57849d01f")
