from time_list_generator import get_timestamps
from chat_putter import get_chat

video_id = "391828640"

chat_log = get_chat(video_id)

for chat in chat_log:
	print(chat)

timestamp_list = get_timestamps(chat_log)

# for i, j in timestamp_list:
# 	print(("%s %s" %(i, j)))