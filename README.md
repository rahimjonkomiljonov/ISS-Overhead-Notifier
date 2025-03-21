# ISS Overhead Notifier

A Python script that monitors the International Space Station (ISS) position and sends an email notification when it's overhead your location during nighttime.

## Features
- Tracks ISS position in real-time
- Checks local sunrise/sunset times
- Sends email alerts when ISS is overhead at night
- Continuous monitoring with 60-second intervals
- Error handling for API requests and email sending

## Prerequisites
- Python 3.x
- Required Python packages:
  - `requests`
- Gmail account with App Password (for SMTP)

## Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/iss-overhead-notifier.git
cd iss-overhead-notifier
```

2. Install dependencies:
```bash
pip install requests
```

## Configuration
- `MY_LAT`: Your latitude (default: 37.566536, Seoul)
- `MY_LONG`: Your longitude (default: 126.977966, Seoul)
- `EMAIL`: Your Gmail address
- `PASSWORD`: Gmail App Password (not regular password)
- `ISS_API_URL`: "https://api.open-notify.org/iss-now.json"
- `SUNRISE_SUNSET_API_URL`: "https://api.sunrise-sunset.org/json"
- `SMTP_SERVER`: "smtp.gmail.com"

## Usage
1. Update the script with your coordinates and email credentials
2. Run the script:
```bash
python iss_notifier.py
```

3. The script will:
- Check ISS position every 60 seconds
- Send email if ISS is within ±5° of your location at night

## How It Works
- **ISS Position**: Fetches current ISS coordinates
- **Night Check**: Determines if it's night based on sunrise/sunset
- **Notification**: Sends email via Gmail SMTP when conditions met
- **Loop**: Runs continuously with 60-second delay

## Functions
- `is_overhead()`: Checks if ISS is within ±5° of your location
- `is_night()`: Verifies if current time is after sunset or before sunrise
- `send_email()`: Sends notification via SMTP

## APIs Used
- ISS Location: Open Notify API
- Sunrise/Sunset: Sunrise-Sunset API

## Customization
- Adjust `MY_LAT` and `MY_LONG` for your location
- Modify ±5° range in `is_overhead()`
- Change `time.sleep(60)` for different check intervals
- Update email message in `send_email()`

## Notes
- Uses UTC time for sunrise/sunset comparison
- Requires Gmail App Password (not regular password)
- 5-second timeout on API requests
- Prints error messages to console
- Background color and padding customizable

## Requirements.txt
```
requests
```

## Limitations
- Gmail-specific SMTP configuration
- No persistent logging of notifications
- Basic ±5° proximity check
- Single recipient email

## License
[MIT License](LICENSE)

## Disclaimer
- Secure your email credentials
- Be aware of API rate limits
- Requires stable internet connection
- Gmail may require "Less secure app access" or App Password
```

