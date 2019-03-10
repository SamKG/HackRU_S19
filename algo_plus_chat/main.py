from time_list_generator import get_timestamps
from chat_putter import get_chat
from argparse import ArgumentParser
import sqlite3
import json


def get_vid_data(video_id="377499328"):
    
    chat_log = get_chat(video_id)
    print("GOT CHAT LOG DATA")
    for chat in chat_log:
    	print(chat)

    timestamp_list = get_timestamps(chat_log)
    print("GOT TIMESTAMP LIST")
    print(timestamp_list)
    return timestamp_list

if __name__ == '__main__':
    conn = sqlite3.connect('timestamp_cache.db')
    parser = ArgumentParser()
    parser.add_argument('vidid')
    args = parser.parse_args()
    cur = conn.cursor()
    cur.execute('SELECT * FROM cache WHERE key = \''+args.vidid+'\'')
    r = cur.fetchone()
    #print(r)
    if not r is None:
        for t in json.loads(r[0]):
            t = str(t)
            t = t.replace('[','(')
            t = t.replace(']',')')
            print(t)
    else:
        lis = get_vid_data(args.vidid)
        jstring = json.dumps(lis)
        #print(jstring,args.vidid)
        cur.execute('INSERT INTO cache (key,val) VALUES (\''+args.vidid+'\',\''+jstring+'\');')
        for t in lis:
            print(t)

    conn.commit()
    conn.close()
