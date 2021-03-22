# Deep Sort with PyTorch


## Quick Start

1. Download deepsort parameters ckpt.t7
```
cd deep_sort/deep/checkpoint
# download ckpt.t7 from
https://drive.google.com/drive/folders/1xhG0kRH1EX5B9_Iz8gQJb7UNnn_riXi6 to this folder
cd ../../../
```  


Notice:
If compiling failed, the simplist way is to **Upgrade your pytorch >= 1.1 and torchvision >= 0.3" and you can avoid the troublesome compiling problems which are most likely caused by either `gcc version too low` or `libraries missing`.

2. Run demo
```
usage: python yolov5_deepsort.py VIDEO_PATH
                                [--help]
                                [--frame_interval FRAME_INTERVAL]
                                [--config_detection CONFIG_DETECTION]
                                [--config_deepsort CONFIG_DEEPSORT]
                                [--display]
                                [--display_width DISPLAY_WIDTH]
                                [--display_height DISPLAY_HEIGHT]
                                [--save_path SAVE_PATH]          
                                [--cpu]          

# yolov5 + deepsort
python yolov5_deepsort.py [VIDEO_PATH]
```
Use `--display` to enable display.  
Results will be saved to `./output/results.avi` and `./output/results.txt`.


## References

- code: [deepsot.pytorch](https://github.com/ZQPei/deep_sort_pytorch)

- code: [yolov5](https://github.com/ultralytics/yolov5)
