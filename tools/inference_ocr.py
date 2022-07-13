import argparse
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../'))

import cv2

from vedastr.runners import InferenceRunner
from vedastr.utils import Config




def main(a_imagelist,config,gpus,checkpoint):
   
    #Namespace(checkpoint='D:\\FYPtesting\\vedastr\\vedastr\\workdir\\small_satrn_modifiedV4\\best_acc_86.pth', config='configs/small_satrn_modifiedV4.py', gpus='0', image='D:\\FYPtesting\\vedastr\\vedastr\\test_infer_image\\word_1.png')
    
    cfg_path = config
    cfg = Config.fromfile("D:\FYPtesting/vedastr/vedastr/"+cfg_path)
    

    deploy_cfg = cfg['deploy']
    common_cfg = cfg.get('common')
    deploy_cfg['gpu_id'] = gpus.replace(" ", "")

    runner = InferenceRunner(deploy_cfg, common_cfg)
    runner.load_checkpoint(checkpoint)

    # if os.path.isfile(a_image):
    #     images = [a_image]
    # else:
    #     images = [os.path.join(a_image, name)
    #               for name in os.listdir(a_image)]
    
    #image = cv2.imread(img)
    pre_list=[]
    for a_image in a_imagelist:
        image=a_image
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        pred_str, probs = runner(image)
        runner.logger.info('predict string: {} \t '.format(pred_str))
        pre_list.append(pred_str)
    return pre_list


# test run
#python ocr.py configs/small_satrn_modifiedV4.py D:\FYPtesting\vedastr\vedastr\workdir\small_satrn_modifiedV4\best_acc_86.pth D:/FYPtesting/vedastr/OCR/input_img/orchard.jpg "0"