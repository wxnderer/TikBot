from tiktok_uploader.upload import upload_video


# Set up authentication
cookies_list = [
    {
        'name': 'sessionid',
        'value': '***REMOVED***',
        'domain': 'https://tiktok.com',
        'path': '/',
        'expiry': '01/07/2025, 10:01:08 PM'
    }
    # the rest of your cookies all in a list
]

# Video details
video_path = 'sample.mp4'
description = 'Check out this awesome video! #tiktok #viral'
tags = ['fyp', 'foryoupage', 'trending']

# Upload the video
upload_video(
    video_path,
    description=description,
    tags=tags,
    cookies_list=cookies_list
)

print("Video uploaded successfully!")
