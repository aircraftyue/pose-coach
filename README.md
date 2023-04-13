# pose-coach

## Usage

```bash
# you can download better but larger model by running 'models/download_cmu.sh'
# change model's path in 'openpose_COCO.py' at line 30

# put video into 'data/records'

# extract pose from video
python openpose_COCO.py --input data/records/record_0.mov

# convert frames to video
python frame2video.py
# you'll get video in 'data/output/videos'
```

## Requirements

```bash
pip install opencv-python numpy argparse moviepy
```
