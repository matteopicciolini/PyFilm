import subprocess
subprocess.run(["ffmpeg", "-i", "video.ts", "video.mp4"])

# it's better to use this command from command line:
# ffmpeg -i video.ts -c copy output.mp4
# and than, for trimming:
# ffmpeg -ss 01:33:42 -to 01:36:16 -i output.mp4 -c copy trimmed.mp4