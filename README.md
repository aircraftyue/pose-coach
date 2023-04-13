# pose-coach

## Usage

```bash
# (Optional) You can download better but larger model by running 'models/download_cmu.sh'
# then change model's path in 'openpose_COCO.py' at line 30

# 1. Put detecting video into 'data/records'

# 2. Extract pose from video (two methods here, choose one)
# OpenPose method
python openpose_COCO.py --input data/records/{your_video_name}
# OR use MediaPipe method to get better result
python mediapipe_video.py

# 3. Convert detected frames to mp4 format
python frame2video.py
# you'll get video in 'data/output/videos'
```

## Requirements

```bash
pip install opencv-python numpy argparse moviepy mediapipe
```
