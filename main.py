import asyncio
import random

from telethon.sync import TelegramClient
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError, UserChannelsTooMuchError, FloodWaitError, UserAlreadyParticipantError
from telethon.tl.functions.channels import InviteToChannelRequest

api_id = 25384018  # THAY BẰNG API ID MỚI CỦA BẠN
api_hash = '88bb30ce227b0b26a89342c6b1baf084' # THAY BẰNG API HASH MỚI CỦA BẠN
phone_number = '+84968811628' # SỐ ĐIỆN THOẠI CỦA BẠN

# 3. ID CỦA NHÓM NGUỒN VÀ NHÓM ĐÍCH
source_group_id = -1002865411653
target_group_id = -1002549126370

async def main():
    print("Bước 1: Lấy danh sách thành viên đã có trong nhóm đích...")
    target_group_members_ids = set()
    try:
        target_participants = await client.get_participants(target_group_id, aggressive=True)
        for member in target_participants:
            target_group_members_ids.add(member.id)
        print(f"-> Nhóm đích hiện có {len(target_group_members_ids)} thành viên.")
    except Exception as e:
        print(f"Lỗi không thể lấy danh sách thành viên nhóm đích: {e}")
        print("Vui lòng kiểm tra lại target_group_id và quyền admin của bạn trong nhóm.")
        return
    # ---------------------------------------------------------

    print("\nBước 2: Lấy danh sách thành viên từ nhóm nguồn...")
    try:
        source_participants = await client.get_participants(source_group_id, aggressive=True)
    except Exception as e:
        print(f"Lỗi nghiêm trọng, không thể lấy danh sách thành viên nhóm nguồn: {e}")
        return
    print(f"-> Nhóm nguồn có {len(source_participants)} thành viên.")

    print("\nBước 3: Bắt đầu quá trình mời...")
    for user in source_participants:
        if user.bot or user.deleted:
            continue

        if user.id in target_group_members_ids:
            continue
        # ---------------------------------------------------------

        try:
            print(f"Đang mời: {user.first_name} {user.last_name or ''} (ID: {user.id})")
            await client(InviteToChannelRequest(channel=target_group_id, users=[user]))

            delay_time = random.randrange(60, 120)
            print(f"-> Mời thành công! Tạm dừng trong {delay_time} giây.")
            await asyncio.sleep(delay_time)

        except UserAlreadyParticipantError:
            print("-> Lỗi: Người dùng đã là thành viên (đã được kiểm tra nhưng có thể có độ trễ). Bỏ qua.")
            await asyncio.sleep(5)
        except FloodWaitError as e:
            print(f"!!! Lỗi FloodWaitError. Telegram yêu cầu phải chờ {e.seconds} giây.")
            await asyncio.sleep(e.seconds + 5)
        except PeerFloodError:
            print("!!! Lỗi PEER_FLOOD_ERROR. Giới hạn nghiêm trọng. Dừng 1 giờ.")
            await asyncio.sleep(3600)
        except UserPrivacyRestrictedError:
            print(f"-> Lỗi: Không thể mời do cài đặt quyền riêng tư của người dùng.")
            await asyncio.sleep(10)
        except UserChannelsTooMuchError:
            print(f"-> Lỗi: Người dùng đã tham gia quá nhiều kênh/nhóm.")
            await asyncio.sleep(10)
        except Exception as e:
            print(f"-> Gặp lỗi không xác định: {e}")
            await asyncio.sleep(15)

    print("\nĐã hoàn tất quá trình mời.")

print("Đang kết nối tới Telegram...")
with TelegramClient(phone_number, api_id, api_hash) as client:
    client.loop.run_until_complete(main())