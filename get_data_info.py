import os
import cv2

def get_info(path):
    images = []
    total_infos = []
    list_dirs = [dir for dir in os.listdir(path) if os.path.isdir(os.path.join(path, dir))]
    if len(list_dirs) > 0:
        for dirs in list_dirs:
            images.append([image for image in os.listdir(os.path.join(path, dirs))])
    else:
        images.append([image for image in os.listdir(path)])

    print("[O V E R V I E W]")

    for n, (image_folders, name_folders) in enumerate(zip(images, os.listdir(path))):
        print(f"[EXAMINING FOLDER] > [{name_folders}]")
        print(f"[TOTAL IMAGES IN FOLDER] > [{len(image_folders)}]")
        total_infos.append(info(image_folders, os.path.join(path, name_folders)))
        print(f"[AVERAGE DIMENSIONS] > [WIDTH : {round(total_infos[n][0], 2)}px] | [HEIGHT : {round(total_infos[n][1], 2)}px]")
        print(f"[AVERAGE FILE SIZE] > [{round(total_infos[n][2] / 1000, 2)} KB]")
        print()

    print()
    print("[INFORMATION CONSIDERING ALL DATA]")
    total_infos_calculated = get_total_infos(total_infos)

    print(f"[TOTAL IMAGES] > [{(total_images := sum([len(x) for x in images]))}]")
    print(f"[AVERAGE IMAGES PER FOLDER] > [{round(total_images/len(images)), 2}]")
    print(f"[AVERAGE DIMENSIONS] > [WIDTH : {round(total_infos_calculated[0], 2)}px] | [HEIGHT : {round(total_infos_calculated[1], 2)}px]")
    print(f"[AVERAGE FILE SIZE] > [{round(total_infos_calculated[2] / 1000, 2)} KB]")



def info(list, path):
    width_total = 0; height_total = 0; size = 0
    len_list = len(list)
    for files in list:
        im = cv2.imread(os.path.join(path, files))
        size += os.path.getsize(os.path.join(path, files))
        try:
            width, height, dim = im.shape
        except:
            width, height, dim = (0, 0, 0)
            len_list -= 1
        width_total += width
        height_total += height
    return [width_total/len_list, height_total/len_list, size/len_list]


def get_total_infos(list):
    width = 0; heigth = 0; size = 0
    for sublists in list:
        width += sublists[0]
        heigth += sublists[1]
        size += sublists[2]
    return [width/len(list), heigth/len(list), size/len(list)]



get_info("G:/Python/data/persons/")

