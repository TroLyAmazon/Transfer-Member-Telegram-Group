import requests
import random
import time

tokenbot = '7644314791:AAGzIpsQL081N7R8ilvJo4-epjrIC8ckVU8'

MESSAGE_VARIANTS = [
    "Bạn ơi, tham gia nhóm mới của mình nhé: https://t.me/+MG8Fzn70EV0xYTZl",
    "Mời bạn vào group mới của mình: https://t.me/+MG8Fzn70EV0xYTZl",
    "Rất vui nếu bạn tham gia nhóm mới này: https://t.me/+MG8Fzn70EV0xYTZl",
    "Hãy cùng mình tham gia group mới: https://t.me/+MG8Fzn70EV0xYTZl",
    "Nhóm mới của mình đang chờ bạn: https://t.me/+MG8Fzn70EV0xYTZl",
    "Bạn có thể tham gia nhóm mới tại đây nhé: https://t.me/+MG8Fzn70EV0xYTZl",
    "Mình vừa tạo group mới, mời bạn tham gia: https://t.me/+MG8Fzn70EV0xYTZl",
    "Nếu rảnh, ghé nhóm mới của mình nha: https://t.me/+MG8Fzn70EV0xYTZl",
    "Tham gia nhóm mới cùng mình nhé: https://t.me/+MG8Fzn70EV0xYTZl",
    "Đừng bỏ lỡ group mới này: https://t.me/+MG8Fzn70EV0xYTZl"
]

def send_message(user_id, message):
    url = f"https://api-free-proxy-telegram-baomatdo.tacphosting.workers.dev/bot{tokenbot}/sendMessage"
    payload = {
        "chat_id": user_id,
        "text": message
    }
    response = requests.post(url, data=payload)
    return response.json()

def main():
    with open("idtelegram.txt", "r", encoding="utf-8") as f:
        ids = [line.strip() for line in f if line.strip()]

    print(f"Đang gửi tin nhắn cho {len(ids)} thành viên...")

    for idx, user_id in enumerate(ids, 1):
        message = random.choice(MESSAGE_VARIANTS)
        print(f"[{idx}/{len(ids)}] Gửi tới ID: {user_id} - Nội dung: {message}")
        try:
            result = send_message(user_id, message)
            print(f"Kết quả: {result}")
        except Exception as e:
            print(f"Lỗi khi gửi tới {user_id}: {e}")
        delay = random.randint(5, 15)
        print(f"-> Đã gửi! Đợi {delay} giây trước khi gửi tiếp...")
        time.sleep(delay)

    print("Đã gửi xong tất cả tin nhắn.")

if __name__ == "__main__":
    main()