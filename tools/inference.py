import argparse
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../'))

import cv2

from vedastr.runners import InferenceRunner
from vedastr.utils import Config


def parse_args():
    parser = argparse.ArgumentParser(description='Inference')
    parser.add_argument('config', type=str, help='Config file path')
    parser.add_argument('checkpoint', type=str, help='Checkpoint file path', default='vedastr/vedastr/checkpoint/small_satrn.pth')
    parser.add_argument('image', type=str, help='input image path', default='vedastr/vedastr/test_infer_image/word_1.png')
    parser.add_argument('gpus', type=str, help='target gpus',default='0')
    args = parser.parse_args()

    return args


def main():
    args = parse_args()
    print(args)
    cfg_path = args.config
    cfg = Config.fromfile(cfg_path)

    deploy_cfg = cfg['deploy']
    common_cfg = cfg.get('common')
    deploy_cfg['gpu_id'] = args.gpus.replace(" ", "")

    runner = InferenceRunner(deploy_cfg, common_cfg)
    runner.load_checkpoint(args.checkpoint)
    if os.path.isfile(args.image):
        images = [args.image]
    else:
        images = [os.path.join(args.image, name)
                  for name in os.listdir(args.image)]
    for img in images:
        image = cv2.imread(img)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        pred_str, probs = runner(image)
        runner.logger.info('predict string: {} \t of {}'.format(pred_str, img))


if __name__ == '__main__':
    main()



#python tools/inference.py configs/small_satrn.py D:/FYPtesting/vedastr/vedastr/checkpoint/small_satrn.pth D:/FYPtesting/vedastr/vedastr/test_infer_image "0"