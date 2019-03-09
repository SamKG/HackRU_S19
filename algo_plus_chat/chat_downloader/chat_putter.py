import subprocess
import ast
import pprint

pipes = subprocess.Popen(["python", "app.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
std_out, std_err = pipes.communicate(input=b"391828640")

out=ast.literal_eval(std_err)
pprint.pprint(out)
