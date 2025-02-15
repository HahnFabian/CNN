import os
import cv2
from pathlib import Path


def get_info(path):
    global large_files
    images = []
    total_infos = []
    large_files = []
    list_dirs = [dir for dir in os.listdir(path) if os.path.isdir(os.path.join(path, dir))]
    if len(list_dirs) > 0:
        for dirs in list_dirs:
            images.append([image for image in os.listdir(os.path.join(path, dirs))])
    else:
        images = [image for image in os.listdir(path)]
        total_infos.append(info(images, path, os.path.dirname))

    print("[O V E R V I E W]")

    for n, (image_folders, name_folders) in enumerate(zip(images, os.listdir(path))):
        print(f"[{n+1}/ {len(images)}] > [EXAMINING FOLDER] > [{name_folders}]")
        print(f"[TOTAL IMAGES IN FOLDER] > [{len(image_folders)}]")
        total_infos.append(info(image_folders, os.path.join(path, name_folders), name_folders))
        print(f"[AVERAGE DIMENSIONS] > [WIDTH : {round(total_infos[n][0], 2)}px] | [HEIGHT : {round(total_infos[n][1], 2)}px]")
        print(f"[AVERAGE FILE SIZE] > [{round(total_infos[n][2] / 1E3, 2)}KB]")
        print(f"[TOTAL FOLDER SIZE] > [{round(total_infos[n][2] * len(image_folders) / 1E6, 2)}MB]")
        print()

    print()
    print("[INFORMATION CONSIDERING ALL DATA]")

    total_infos_calculated = get_total_infos(total_infos)

    print(f"[TOTAL IMAGES] > [{(total_images := sum([len(x) for x in images]))}]")
    print(f"[AVERAGE IMAGES PER FOLDER] > [{round(total_images/len(images), 2)}]")
    print(f"[MOST IMAGES >{(max_images := max([(len(x), n) for n,x in enumerate(images)]))[0]}< IN FOLDER {list_dirs[max_images[1]]}] > "
          f"[LEAST IMAGES >{(min_images := min([(len(x), n) for n,x in enumerate(images)]))[0]}< IN FOLDER {list_dirs[min_images[1]]}] > "
          f"[OFFSET {round(((max_images[0] / min_images[0]) - 1) * 100,2)}%]")
    print(f"[AVERAGE DIMENSIONS] > [WIDTH : {round(total_infos_calculated[0], 2)}px] | [HEIGHT : {round(total_infos_calculated[1], 2)}px]")
    print(f"[AVERAGE FILE SIZE] > [{round(total_infos_calculated[2] / 1000, 2)}KB]")
    print(f"[TOTAL FILE SIZE] > [{round((size := sum(f.stat().st_size for f in Path(path).glob('**/*')))/1E6,2)}MB / {round(size/1E9,2)}GB]")
    print(f"[TOTAL FILES LARGER THAN 1MB > {len(large_files)}] > [POSSIBLE REDUCTION > {round((red := sum([x[2] for x in large_files]))/1E6,2)}MB] > "
          f"[WORKS OUT TO {round((red/size)*100,2)}%]")



def info(list, path, dir):
    width_total = 0; height_total = 0; size = 0
    len_list = len(list)
    for files in list:
        im = cv2.imread(os.path.join(path, files))
        new_size = os.path.getsize(os.path.join(path, files))
        size += new_size
        if new_size > 1000000:
            large_files.append((dir, files, new_size))
        try:
            width, height, dim = im.shape
        except:
            width, height, dim = (0, 0, 0)
            len_list -= 1
        width_total += width
        height_total += height
    return [width_total/len_list, height_total/len_list, size/len_list]


def get_total_infos(list):
    width = 0; height = 0; size = 0
    for sublists in list:
        width += sublists[0]
        height += sublists[1]
        size += sublists[2]
    return [width/len(list), height/len(list), size/len(list)]



get_info("G:/Python/data/eval_images/")

