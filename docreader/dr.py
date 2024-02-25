from tkinter import *
from tkinter import  filedialog
import os
import ebooklib
from tkdocviewer import *
import customtkinter
import logging
import tkinter

def ev():
	# Create a root window
	root = Tk()
	root.geometry("600x700+400+100")
	root.title("Doc & Ebooks Reader")
	root.configure(bg="black")

	def browseFiles():
		filename = filedialog.askopenfilename(initialdir=os.getcwd(),
			title="select #file",
			filetype=(("ALL  Files", ".*"),
				("PDF File", ".pdf"),
				("PDF File",".PDF"),
				("EPUB", ".epub")))
		# v1=pdf.ShowPdf()
		# v2=v1.pdf_view(root,pdf_location=open(filename,"r"), width=77, height=100)
		# v2.pack(pady=(0,0))

		# Create a DocViewer widget
		v = DocViewer(root)
		v.pack(side="top", expand=True, fill="both")

		# Display some document
		v.display_file(filename)
		v.pack(pady=(0,0))
	Button(root, text="open", command= browseFiles, width=10, font ="arial 18", bd = 2).pack()

	# Start Tk's event loop
	root.mainloop()

customtkinter.ScalingTracker.set_window_scaling(0.5)
customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
# app.geometry("650x700")
app.title("Document Reader")

def browseFiles():
	try:
		filename = filedialog.askopenfilename(initialdir=os.getcwd(),
			title="select #file",
			filetype=(("ALL  Files", ".*"),
				("PDF File", ".pdf"),
				("PDF File",".PDF"),
				("EPUB", ".epub")))

		# Create a DocViewer widget
		v = DocViewer(a_frame)
		v.pack(side="top", expand=True, fill="both")

		# Display some document
		v.display_file(filename)
		v.pack(pady=(0,0))
	except Exception as e:
		print(f"This error occured {e}")

def slider_function(value):
    customtkinter.set_widget_scaling(value * 2)
    customtkinter.set_window_scaling(value * 2)

y_padding = 10
a_frame = customtkinter.CTkFrame(master=app)

a_frame.pack(pady=20, padx=60, fill="both", expand=True)

o_butt = customtkinter.CTkButton(master=a_frame,corner_radius=0, height=40, border_spacing=10, text="open", 
												text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), command= browseFiles)
o_butt.pack(pady=10, padx=10, anchor=tkinter.CENTER, side=LEFT)

slider_1 = customtkinter.CTkSlider(master=a_frame, command=slider_function, from_=0, to=1)
slider_1.pack(pady=y_padding, padx=10, fill=X)
slider_1.set(0.5)

if __name__ == "__main__":
    # logging.basicConfig(level=logging.DEBUG)
    # app = App()
    app.mainloop()