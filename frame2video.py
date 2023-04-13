from moviepy.video.io.ImageSequenceClip import ImageSequenceClip
import os

# 设置图片文件夹和输出视频文件名
image_folder = 'data/output/frames'
video_name = 'data/output/videos/output.mp4'

# 读取文件夹下的所有图片文件，并按照创建时间排序
images = [img for img in os.listdir(image_folder) if img.endswith('.png')]
images.sort(key=lambda x: os.path.getctime(os.path.join(image_folder, x)))

# 创建图像序列剪辑并输出为mp4文件
clip = ImageSequenceClip([os.path.join(image_folder, img) for img in images], fps=30)
clip.write_videofile(video_name, fps=30, codec='mpeg4', bitrate='5000k', threads=4, audio=False)
