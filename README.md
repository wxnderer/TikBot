# TikTok Auto Uploader 🤖

This script automates the process of uploading videos to TikTok using the `tiktok-uploader` package and Selenium.

## Prerequisites ✅

- **Python 3.x**
  - **`tiktok-uploader` package:** _Installed via `pip install -r requirements.txt`_
  - **Selenium:** _Installed via `pip install -r requirements.txt`_
- **Appropriate WebDriver:** Download the WebDriver for your browser (e.g., ChromeDriver for Chrome) and place it in your system's PATH.
- **Cookies.txt file:**
  1. Install the "Get cookies.txt" extension for your browser.
  2. Navigate to TikTok and log in to your account.
  3. Use the extension to export your cookies to a file named `cookies.txt` and place it inside the script's folder.

## Usage 🚀

1. **Place your video file in the script's folder and rename accordingly.**
2. **Run the script:** `python tiktok_uploader.py`

## Notes 📝

- The script assumes your video files are in a supported format (e.g., MP4).
- You may need to adjust the script's code to match your specific needs, such as modifying video descriptions or hashtags.
- It's recommended to use Google Chrome as your Selenium browser to minimize the risk of TikTok bot detection.

## Disclaimer ⚠️

This script is provided for educational purposes only. Use it responsibly and be aware of TikTok's terms of service.
