import os
import random, string



def rename(path, len_new_name = 128):
    for n, image in enumerate(os.listdir(path)):
        name, extension = os.path.splitext(os.path.join(path, image))
        new_name = random_text(len_new_name) + extension
        os.rename(os.path.join(path, image), os.path.join(path, new_name))
    print(f"RENAMED ALL {len([file for file in os.listdir(path)])} IMAGES")

def random_text(n):
    return ''.join([random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for i in range(n)])

rename(r"G:\Python\data\pre\c499fc7b-5697-4910-93f0-dce57849d01f")
