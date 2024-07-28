from util import mkdir
import os
import glob
# root to the testsets
# dataroot = '/home/zhainaixin/hades/data/AIGCDetect_testset/zhong2023_test'
dataroot = './0711_test'

# list of synthesis algorithms
print(dataroot)


vals = [ i.split("/")[-1] for i in glob.glob(dataroot+"/*")]
# vals = ['progan', 'stylegan', 'biggan', 'cyclegan', 'stargan', 'gaugan',
#         'stylegan2', 'whichfaceisreal',
#         'ADM','Glide','Midjourney','stable_diffusion_v_1_4','stable_diffusion_v_1_5','VQDM','wukong','DALLE2']

