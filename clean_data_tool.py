from PIL import Image
import os

formats = ["JPEG", "JPG", "PNG", "BMP", "GIF"]
false_images = []
broken_images = []

def search(path):
    count_false_images = 0
    count_broken_images = 0
    for dirs in os.listdir(path):
        new_path = os.path.join(path, dirs)
        print()
        print("-------------------------------------------")
        print(f"NOW IN DIR: {dirs}")
        for images in os.listdir(new_path):
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
    print()
    print(f"FOUND {count_false_images} IMAGES NOT MATCHING THE FORMATS AND {count_broken_images} FILES WHICH WERE UNABLE TO BE ACCESSED")



def remove(type_of_images):
    for x, item in enumerate(type_of_images):
        os.remove(item)
        print(f"REMOVED FILE {x+1}/{len(type_of_images)}")

search("G:/Python/data/animals/")
remove(false_images)
