import subprocess
import ast
import pprint

def get_chat(video_id):
    vid = bytes(video_id, encoding = 'utf - 8')
    pipes = subprocess.Popen(["python3", "twitchfreq_server/lib/algo_plus_chat/app.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    #print("STEP 1")
    std_out, std_err = pipes.communicate(input=vid)
    print(std_out)
    #print("STEP 2")
    out = eval(std_err)
    #print("STEP 3")
    # pprint.pprint(out)
    return out
