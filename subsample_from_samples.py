import os
from random import randint


def subsample_from_samples(path, amount=10, method='random'):
    if len([dir for dir in os.listdir(path) if os.path.isdir(os.path.join(path, dir))]) == 0:
        images = subsample_single(path, amount, method)
    else:
        images = subsample_multi(path, amount, method)
    print(images)


def subsample_single(path, amount, method):
    images_pre = [img for img in os.listdir(path)]
    images = []
    rand_numbs = [-1]; n = -1
    for i in range(amount):

        if method == 'random':
            while n in rand_numbs:
                n = randint(0, len(images_pre)-1)
            rand_numbs.append(n)
        else:
            n = i

        images.append((os.path.join(path, images_pre[n]), os.path.basename(path)))

    return images


def subsample_multi(path, amount, method):
    dirs = [dir for dir in os.listdir(path) if os.path.isdir(os.path.join(path, dir))]
    rand_numbs = [-1]; n = (-1, -1); k = 0
    images_pre = []
    images_pre_1dim = []
    images = []

    for dir in dirs:
        images_pre.append([img for img in os.listdir(os.path.join(path, dir))])

    for sublist in images_pre:
        sublist = sorted(sublist)
        for img in sublist:
            images_pre_1dim.append(img)

    for i in range(amount):

        if method == 'random':
            while n in rand_numbs:
                k = randint(0, len(images_pre))
                n = (k, randint(0, len(images_pre[k])))
            rand_numbs.append(n)
        else:
            if i != 0 and i % len(images_pre) == 0:
                k += 1
                i = i % len(images_pre)
            n = (i, k)
        print(n)

        images.append((os.path.join(path, images_pre[n[0]][n[1]]), dirs[n[0]]))

    return images


subsample_from_samples(r"G:\Python\data\fruits", 10, 'ssss')