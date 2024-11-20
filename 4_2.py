import os

def fods(dir):
	fodsize = 0
	if os.path.isfile(dir):
		fodsize = os.path.getsize(dir)
	else:
		for dp, dns, fns in os.walk(dir):
			for fn in fns:
				fp = os.path.join(dp, fn)
				if os.path.isfile(fp):
					fodsize += os.path.getsize(fp)
	return fodsize

def bkmgt(fods):
	for unit in ['B', 'K', 'M', 'G', 'T']:
		if fods < 1024:
			break
		else:
			fods /= 1024
	return "{:.1f}{}\t".format(fods, unit)

def main():
	pwd = os.getcwd()
	fad = os.listdir(pwd)
	arrays = []
	for fod in fad:
		fullp = os.path.join(pwd, fod)
		fodsize = fods(fullp)
		arrays.append((fodsize, fod))
		
	arrays.sort(key=lambda x: x[0], reverse=True)
	for fodsize, fod in arrays:
		print ("{} {}".format(bkmgt(fodsize), fod))
	
	
if __name__ == "__main__":
	main()
