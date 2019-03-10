from .time_list_generator import get_timestamps
from .chat_putter import get_chat
from argparse import ArgumentParser

def get_vid_data(video_id="377499328"):
    chat_log = get_chat(video_id)

    # for chat in chat_log:
    # 	print(chat)

    timestamp_list = get_timestamps(chat_log)
    return timestamp_list

if __name__ == '__main__':
    for t in get_vid_data():
        print(t,'\n')
