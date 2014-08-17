import os, sys
from PIL import Image

size = (258, 256)


for infile in sys.argv[1:]:
    outfile = os.path.splitext(infile)[0] + ".thumbnail"
    if infile != outfile:
        try:
            im = Image.open(infile)
            im.thumbnail(size)
            im.save(outfile, "JPEG")
            print outfile
        except IOError:
            print("cannot create thumbnail for", infile)


def main():
	try:
		im = Image.open('test.png')
		im.thumbnail(size)
		im.save('test.pn', 'png')
	except IOError:
		print("cannot create thumbnail for", infile)
	

if __name__ == '__main__':
	main()
	print 'self excute'