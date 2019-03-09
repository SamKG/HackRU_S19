def convert(s):
	return str(s/3600)+":"+str((s%3600)/60)+":"+str(s%60);

print(convert(195236))