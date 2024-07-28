import os
import torch
from tqdm import tqdm
import torchvision

from glob import glob

# datas = glob("/home/zhainaixin/hades/atked_data/*")
datas = ["/home/zhainaixin/hades/mm2024/outputs/eval/gan/resnet/earlystop/advData_resnet_ProGANSynLSUN_FGSM_earlystop_False_0.pt"]

for data in datas:

    name = os.path.basename(data).split(".")[0]

    advData = torch.load(data)  

    adv_imgs = advData[0]
    adv_gts = advData[1]

    save_path = "./0711_test/" + name

    real_dir = os.path.join(save_path, "0_real")
    fake_dir = os.path.join(save_path, "1_fake")
    os.makedirs(real_dir, exist_ok=True)
    os.makedirs(fake_dir, exist_ok=True)


    for index, img in enumerate(tqdm(adv_imgs)):
        img = torchvision.transforms.ToPILImage()(img)
        if adv_gts[index] == 0:
            img.save(os.path.join(real_dir, str(index)+'.png'))
        else:
            img.save(os.path.join(fake_dir, str(index)+'.png'))