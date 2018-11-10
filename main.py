# -*- coding: utf-8 -*-
import os
import gc
import copy
import pickle
import logging
import argparse

import torch

logger = logging.getLogger('hair segmentation project')

# WIP

def get_args():
    model_names = [] # from networks
    scheduler_names = [] # default torch or others
    optimizer_names = [] # default torch or others
    pretrained_names = [] # from models or torchvision

    parser = argparse.ArgumentParser(description='Hair Segmentation')
    parser.add_argument('--adaptive_pool', action='store_true', default=False)
    parser.add_argument('--networks', default='resnet101')
    parser.add_argument('--scheduler', default='ReduceLROnPlateau')
    parser.add_argument('--batch_size', type=int, default=4)
    parser.add_argument('--description', type=str, default='binary_class')
    parser.add_argument('--epochs', default=1, type=int)
    parser.add_argument('--lr', default=0.001, type=float)
    parser.add_argument('--trainable', type=bool, default=True)
    parser.add_argument('--num_workers', type=int, default=4)
    parser.add_argument('--optimizer', type=str, default='adam')
    parser.add_argument('--use_pretrained', type=str, default='ImageNet')

    args = parser.parse_args()
    args.use_gpu = torch.cuda.is_available()

    breakable # juckgo

    return args

def main():
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        '[%(asctime)10s][%(levelname)s] %(message)s',
        datefmt='%Y/%m/%d %H:%M:%S'
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    file_handler = logging.FileHandler('log.log')
    file_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)

    args = get_args()

if __name__ == '__main__':
    main()