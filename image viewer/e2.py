import os
import math
import tkinter as tk
from PIL import Image , ImageTk
from PIL.ImageTk import PhotoImage

#function to get thumbnail images
def makeThumbs(imgdir, size=(100, 100), subdir='thumbs'):
	thumbdir = os.path.join(imgdir,subdir)
	if not os.path.exists(thumbdir):
		os.mkdir(thumbdir)

	thumbs=[]
	for imgfile in os.listdir(imgdir):
		thumbpath = os.path.join(thumbdir, imgfile)
		if os.path.exists(thumbpath):
			thumbobj = Image.open(thumbpath)# Use already created
			thumbs.append((imgfile, thumbobj))
		else:
			print('Making...', thumbpath)
			imgpath = os.path.join(imgdir, imgfile)
			try:
				imgobj=Image.open(imgpath)#make new thumb
				imgobj.thumbnails(size, Image.ANTIALIAS)
				imgobj.save(thumbpath)#type via ext or passed
				thumbs.append((imgfile, imgobj))

			except:
				print("error")
				# print("Skipping:...", imgpath) #not always IOerror
	return thumbs

#open image in  a popup window
class ViewOne(tk.Toplevel):
	def __init__(self, imgdir, imgfile):
		tk.Toplevel.__init__(self)
		self.title(imgfile)
		imgpath=os.path.join(imgdir, imgfile)
		imgobj=PhotoImage(file=imgpath)
		tk.Label(self, image=imgobj).pack()
		print(imgpath, imgobj.width(), imgobj.height())#size in pixels
		self.savephotos=imgobj #keep ref

#viewer function
def viewer(imgdir, Tk=tk.Toplevel, cols=None):
	win=tk.Tk()
	win.title("Viewer: "+imgdir)
	thumbs=makeThumbs(imgdir)
	if not cols:
		cols = int(math.ceil(math.sqrt(len(thumbs)))) #fixed or NxN
	savephotos=[]
	while thumbs:
		thumbsrow = thumbs[cols:]
		thumbs = thumbs[:cols]
		row=tk.Frame(win)
		row.pack(fill='BOTH')
		for (imgfile, imgobj) in thumbsrow:
			size=max(imgobj.size) #width, height
			photo= ImageTk.PhotoImage(imgobj)
			link = tk.Button(row, image=photo)
			handler = lambda savefile=imgfile: ViewOne(imgdir, savefile)
			link.config(command=handler, width=size, height=size)
			link.pack(side='LEFT', expand='YES')
			savephotos.append(photo)


	#creating exit button
	tk.Button(win, text = "Quit", command= win.quit, bg = '#02AC66').pack(fill ='x')
	return win, savephotos

if __name__ == '__main__':
	imgdir="images"
	main, save=viewer(imgdir, tk.Tk)
	main.mainloop()
