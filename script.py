from tiktok_uploader.upload import upload_video

video_path = 'sample.mp4'
description = 'Check out this awesome video! #tiktok #viral'
cookies_file = "cookies.txt"

upload_video(
    video_path,
    description=description,
    cookies=cookies_file
)