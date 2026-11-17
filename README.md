# Test VPS

সিম্পল টেলিগ্রাম টেস্ট বট — VPS ঠিকমতো কাজ করছে কিনা চেক করার জন্য।

## Commands
- `/start` – বট চালু আছে কিনা
- `/ping` – pong রিপ্লাই
- `/status` – VPS এর host, OS, Python, uptime
- `/id` – তোমার Telegram ID

## VPS এ চালানো

```bash
git clone https://github.com/shohagkumarofficial/test-vps.git
cd test-vps
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
export BOT_TOKEN="তোমার_বট_টোকেন"
python bot.py
```

ব্যাকগ্রাউন্ডে চালাতে: `nohup python bot.py &` অথবা `screen -S bot`
