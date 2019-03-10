import subprocess
import ast
import pprint

def get_chat(video_id):

	vid = bytes(video_id, encoding = 'utf - 8')
	pipes = subprocess.Popen(["python", "app.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
	std_out, std_err = pipes.communicate(input=vid)

	out = eval(std_err)
	# pprint.pprint(out)

	return out
