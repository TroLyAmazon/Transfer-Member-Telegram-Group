import asyncio
from telethon.sync import TelegramClient

api_id = 25384018
api_hash = '88bb30ce227b0b26a89342c6b1baf084'
phone_number = '+84968811628'

target_group_id = -1002865411653

async def main():
    print("Bước 1: Lấy danh sách thành viên nhóm cũ...")
    try:
        target_participants = await client.get_participants(target_group_id, aggressive=True)
        print(f"-> Nhóm cũ có {len(target_participants)} thành viên.")
    except Exception as e:
        print(f"Lỗi không thể lấy danh sách thành viên nhóm: {e}")
        return

    usernames = []
    ids = []

    for user in target_participants:
        if user.bot or user.deleted:
            continue
        if user.username:
            usernames.append(user.username)
        ids.append(str(user.id))

    with open("username.txt", "w", encoding="utf-8") as f_user:
        for username in usernames:
            f_user.write(username + "\n")

    with open("idtelegram.txt", "w", encoding="utf-8") as f_id:
        for id_ in ids:
            f_id.write(id_ + "\n")

    print("Đã lưu xong danh sách username và id.")

print("Đang kết nối tới Telegram...")
with TelegramClient(phone_number, api_id, api_hash) as client:
    client.loop.run_until_complete(main())