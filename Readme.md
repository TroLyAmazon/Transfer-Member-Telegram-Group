Transfer Member Telegram Group
Một script Python sử dụng thư viện Telethon để tự động mời thành viên từ một nhóm Telegram nguồn sang một nhóm Telegram đích.


# ✨ Tính năng

Lấy danh sách thành viên từ nhóm nguồn.
Lấy danh sách thành viên hiện có trong nhóm đích để tránh mời trùng lặp.
Mời từng thành viên từ nhóm nguồn sang nhóm đích.
Tự động bỏ qua bot và tài khoản đã bị xóa.
Xử lý các lỗi phổ biến một cách thông minh, bao gồm:
PeerFloodError: Giới hạn mời của Telegram.
UserPrivacyRestrictedError: Người dùng không cho phép mời vào nhóm.
UserChannelsTooMuchError: Người dùng đã tham gia quá nhiều nhóm/kênh.
FloodWaitError: Telegram yêu cầu tạm dừng một khoảng thời gian.
UserAlreadyParticipantError: Người dùng đã có trong nhóm đích.


Tự động thêm khoảng dừng ngẫu nhiên giữa các lần mời để giảm nguy cơ bị giới hạn.

# 📋 Yêu cầu trước khi sử dụng
Trước khi chạy script, hãy đảm bảo bạn đã chuẩn bị:

Python 3.x: Tải và cài đặt Python 3.x từ python.org.

Thư viện Telethon: Cài đặt bằng lệnh:
pip install telethon


Thông tin API Telegram:

Truy cập my.telegram.org/apps.
Đăng nhập bằng số điện thoại của bạn.
Tạo một ứng dụng mới để nhận api_id và api_hash.



# ⚙️ Cấu hình
Mở tệp main.py và chỉnh sửa các thông tin sau:
api_id = 12344321  # Thay bằng API ID của bạn
api_hash = 'YOUR_API_HASH'  # Thay bằng API Hash của bạn
phone_number = '+84...'  # Số điện thoại của bạn (ví dụ: +84xxxxxxxxx)

# ID của nhóm nguồn và nhóm đích
source_group_id = -100xxxxxxxxxx  # Thay bằng ID nhóm nguồn
target_group_id = -100yyyyyyyyyy  # Thay bằng ID nhóm đích

Cách lấy ID nhóm

Sử dụng bot Telegram như @userinfobot hoặc @myidbot.
Chuyển tiếp một tin nhắn từ nhóm nguồn hoặc đích đến bot, bot sẽ trả về ID nhóm (thường là số âm).
Lưu ý: Bạn phải là quản trị viên của nhóm đích để có quyền mời thành viên.

# 🚀 Hướng dẫn sử dụng

Lưu các thay đổi trong tệp main.py.

Chạy script từ terminal hoặc command prompt:
python main.py


Lần chạy đầu tiên:

Nhập số điện thoại và mã xác thực được Telegram gửi đến.
Tệp .session sẽ được tạo để lưu phiên đăng nhập, giúp bạn không cần đăng nhập lại ở các lần sau.


Script sẽ thực hiện:

Lấy danh sách thành viên từ nhóm đích.
Lấy danh sách thành viên từ nhóm nguồn.
Bắt đầu mời từng thành viên, hiển thị nhật ký chi tiết trên màn hình.



# ⚠️ Lưu ý quan trọng

Giới hạn của Telegram: Telegram áp dụng giới hạn nghiêm ngặt về số lượng lời mời để chống spam. Script đã tích hợp khoảng dừng ngẫu nhiên, nhưng mời quá nhiều người trong thời gian ngắn có thể gây lỗi PeerFloodError hoặc FloodWaitError.
An toàn tài khoản: Sử dụng tính năng mời quá mức có thể dẫn đến tài khoản bị hạn chế tạm thời hoặc khóa vĩnh viễn. Hãy sử dụng cẩn thận.
Tôn trọng quyền riêng tư: Chỉ mời những người phù hợp và tôn trọng cài đặt quyền riêng tư của họ.
Thời gian thực hiện: Quá trình mời có thể mất nhiều thời gian, tùy thuộc vào số lượng thành viên và thời gian dừng giữa các lần mời.
Lỗi thường gặp:
UserChannelsTooMuchError: Người dùng đã tham gia quá nhiều nhóm/kênh, không thể khắc phục từ phía bạn.
UserPrivacyRestrictedError: Cài đặt quyền riêng tư của người dùng chặn lời mời từ người lạ.



# 🛡️ Miễn trừ trách nhiệm
Script này được cung cấp cho mục đích học tập và thử nghiệm. Người dùng chịu hoàn toàn trách nhiệm về cách sử dụng script và mọi hậu quả phát sinh, bao gồm việc vi phạm Điều khoản Dịch vụ của Telegram hoặc bị hạn chế tài khoản. Nhà phát triển không chịu trách nhiệm cho bất kỳ thiệt hại nào do sử dụng script này.
# 📬 Hỗ trợ
Nếu gặp sự cố hoặc có câu hỏi, vui lòng mở issue trên repository hoặc liên hệ với người duy trì.

Chúc bạn thành công! 🚀
