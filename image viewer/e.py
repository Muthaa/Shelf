from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import os

class ImageViewer:

    def __init__(self, root):
        
        self.root = root
        self.root.title("Photo Viewer")
        self.root.geometry("1360x750")
        self.root.config(bg = "lightgray")

        menus = Menu(self.root)
        self.root.config(menu = menus)

        file_menu = Menu(menus)
        menus.add_cascade(label = "File", menu = file_menu)
        
        file_menu.add_command(label = "Open", command = self.open_dialog)
        file_menu.add_separator()
        file_menu.add_command(label = "Previous", command = self.previous_img)
        file_menu.add_command(label = "Next", command = self.next_img)
        file_menu.add_separator()
        file_menu.add_command(label = "Exit", command = self.root.destroy)

        self.label = Label(self.root, text = "Open a image using open menu", font = ("Helvetica", 15), foreground = "#0000FF", background = "lightblue")
        self.label.grid(row = 0, column = 0, columnspan = 4)

        self.buttons()

    def path_func(self, path):
        l = []
        self.path = path.split('/')
        self.path.pop()

        self.path = '/'.join([str(x) for x in self.path])
        
        #print(self.path)
        
        for file in os.listdir(self.path):
            if file.endswith('.jpg') or file.endswith('.png'):
                l.append(file)
                #print(l)

        def join(file):
            os.chdir(self.path)
            #print(os.getcwd())
            cwd = os.getcwd().replace('\\', '/')
            #print(cwd)
            f = cwd + '/' + file
            #print(f)
            return f
        
        global file_list
        file_list = list(map(join, l))
        #print(file_list) 

    def open_dialog(self):
            global file_name
            file_name = filedialog.askopenfilename(initialdir = "E:/Jake/100/shelf/assets/images", title = "Open file")
            #print(file_name)
            self.view_image(file_name)
            self.path_func(file_name)

            '''except:
            label = Label(self.root, text = "Select a file to open")
            label.grid(row = 4, column =1)'''

    def view_image(self, filename):
        try:
            self.label.destroy()
            global img
            img = Image.open(filename)
            img = img.resize((1360, 650))
            img = ImageTk.PhotoImage(img)
        
        #print(img)

            show_pic = Label(self.root, image = img)
            show_pic.grid(row = 1, column = 0, columnspan = 3)

        except:
            pass
        
    def buttons(self):
        open_button = Button(self.root, text = "Browse", command = self.open_dialog, background = "lightgray")
        open_button.grid(row = 1, column = 1)
        
        previous_button = Button(self.root, text = "Previous", command = self.previous_img, background = "lightgray", width = 25)
        previous_button.grid(row = 3, column = 0, pady = 10)

        empty = Label(self.root, text = "        ", background = "lightgray")
        empty.grid(row = 3, column = 1)
        
        next_button = Button(self.root, text = "Next", command = self.next_img, background = "lightgray", width = 25)
        next_button.grid(row = 3, column = 2)


    def previous_img(self):
        global file_name
        #print(file_list)
        index = file_list.index(file_name)
        #print(index)
        curr = file_list[index - 1]
        #print(curr)
        self.view_image(curr)
        file_name = curr


    def next_img(self):
        global file_name
        index = file_list.index(file_name)
        #print(index)
        if index == len(file_list) - 1:
            index = -1
            curr = file_list[index + 1]
            #print(curr)
            self.view_image(curr)
            file_name = curr
        else:
            curr = file_list[index + 1]
            #print(curr)
            self.view_image(curr)
            file_name = curr

 
if __name__ == "__main__":
    root = Tk()
    gallery = ImageViewer(root)
    root.mainloop()