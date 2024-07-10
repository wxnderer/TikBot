import asyncio
from TikTokApi import TikTokApi

async def post_video_on_tiktok(video_file_path, caption):
    async with TikTokApi() as api:
        # Authenticate (you may need to implement a proper authentication method)
        await api.login(username='your_username', password='your_password')

        # Upload the video
        result = await api.upload_video(video_file_path, caption=caption)

        if result.get('statusCode') == 0:
            print(f"Video uploaded successfully. Video ID: {result.get('video', {}).get('id')}")
        else:
            print(f"Failed to upload video. Error: {result.get('statusMsg')}")

# Usage
video_path = 'sample.mp4'
video_caption = 'Check out my awesome video! #fyp #viral'

asyncio.run(post_video_on_tiktok(video_path, video_caption))
