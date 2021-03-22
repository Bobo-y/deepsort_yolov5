from .YOLOv5 import YOLOv5

__all__ = ['build_detector']


def build_detector(cfg, use_cuda):
    if 'YOLOV5' in cfg.keys():
        return YOLOv5(cfg.YOLOV5.WEIGHT, cfg.YOLOV5.CLASS_NAMES,img_size=cfg.YOLOV5.IMAGE_SIZE, conf_thres=cfg.YOLOV5.SCORE_THRESH,
                      iou_thres=cfg.YOLOV5.NMS_THRESH, device=cfg.YOLOV5.DEVICE)

