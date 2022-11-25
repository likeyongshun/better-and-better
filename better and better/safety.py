import os
import sys
import datetime
import random
from string import *
import time
from tqdm import tqdm

path = sys.argv[1]
if not os.path.exists(path):
    os.makedirs(path)
n = int(sys.argv[2])
the_str = ascii_letters+digits

def create_dir(path, n):
    dir_name = random.sample(the_str, 8)
    for i in range(n):
        dir_name = ''.join(dir_name)
        os.mkdir(path+os.sep+dir_name+str(i))
    path_dir = os.listdir(path)
    return path_dir
# print(create_dir(path))

def dir_wenben(path, name, wenben_data):
    for i in create_dir(path, n):
        wenben_dir = os.path.join(path, i)
        print(wenben_dir)
        wenben_wrt = str(wenben_dir+os.sep+name)
        # wenben_wr=''.join(wen)
        with open(wenben_wrt, 'w')as f:
            f.write(wenben_data)
# path=r'/mnt/d/Python/test'

def path_search():
    for roots, dirs, files in os.walk(path):
        search = (roots, dirs, files)
        start = datetime.datetime.now()
        for i, value in enumerate(
            tqdm(search, desc='正在遍历{}内容'.format(
                path), ncols=100)
        ):
            print('{},{}'.format(i, value))
            time.sleep(0.5)
        end = datetime.datetime.now()
    print('>>>>>>>>>>>>>>>>>>{}遍历完成{}s<<<<<<<<<<<<<<<<<<<<<<'.format(path, end-start))

name = ''.join(random.sample(the_str, 8))
wenben_data = ''.join(random.sample(the_str, 8))
dir_wenben(path, name, wenben_data)
path_search()