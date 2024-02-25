import tkinter
import tkinter.messagebox
import customtkinter
import os
from PIL import Image

customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):

    def __init__(self, expand=True, height=650):
        super().__init__()

        # configure window
        self.title("PIK")
        if expand:
            self.expand = expand
        else:
            self.height = height
        
        # self.geometry(f"{1200}x{650}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.test_image = customtkinter.CTkImage(Image.open("08-09.png"), size=(500, 450))
        
        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="PIK NAV", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Individual", command=self.sidebar_button_event)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Groups", command=self.sidebar_button_event)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10, sticky="ew")
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, text="Organization", command=self.sidebar_button_event)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10, sticky="ew")
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # create image frame
        self.image_frame = customtkinter.CTkFrame(self,)
        self.image_frame.grid(row=0, column=1, rowspan=3, padx=(10, 0), pady=(10, 0), sticky="nsew")
        self.ttl_label = customtkinter.CTkLabel(self.image_frame, text="Image Profile", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.ttl_label.grid(row=0, column=0, pady=(10, 0))
        self.image_label = customtkinter.CTkLabel(self.image_frame, text="", image=self.test_image)
        self.image_label.grid(row=1, column=0)


        # create data frame
        self.data_frame = customtkinter.CTkTabview(self, bg_color="transparent")
        self.data_frame.grid(row=0, column=2, rowspan=3, columnspan=2, padx=(10, 0), pady=(0, 0), sticky="nsew")
        self.data_frame.add("Profile")
        self.data_frame.add("Social")
        self.data_frame.add("Bio")
        self.data_frame.tab("Profile").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.data_frame.tab("Social").grid_columnconfigure(0, weight=1)
        self.data_frame.tab("Bio").grid_columnconfigure(0, weight=1)

        self.case_no = customtkinter.CTkEntry(self.data_frame.tab("Profile"), height=70, placeholder_text="Case Number")
        self.case_no.grid(row=0, column=0, columnspan=2, padx=10, pady=(20, 10) ,sticky="nsew")
        self.id_no = customtkinter.CTkEntry(self.data_frame.tab("Profile"), height=70, placeholder_text="ID Number")
        self.id_no.grid(row=0, column=2, padx=10, pady=(20, 10) ,sticky="nsew")
        self.name_1 = customtkinter.CTkEntry(self.data_frame.tab("Profile"), height=70, placeholder_text="First Name Entry")
        self.name_1.grid(row=1, column=0, padx=10, pady=(20, 10) ,sticky="nsew")
        self.name_2 = customtkinter.CTkEntry(self.data_frame.tab("Profile"), height=70, placeholder_text="Middle Name Entry")
        self.name_2.grid(row=1, column=1, padx=10, pady=(20, 10) ,sticky="nsew")
        self.name_3 = customtkinter.CTkEntry(self.data_frame.tab("Profile"), height=70, placeholder_text="Last Name Entry")
        self.name_3.grid(row=1, column=2, padx=10, pady=(20, 10) ,sticky="nsew")


        # create main entry and button
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Search Entry")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.main_button_1 = customtkinter.CTkButton(master=self,text="Search", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # set default values
        self.sidebar_button_3.configure(state="disabled", text="New Feature")
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")

    def sidebar_button_event(self):
        self.grid_forget()
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.second_frame.grid(row=0, column=1, sticky="nsew")

    def change_appearance_mode_event(self, new_appearance_mode:str):
    	customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

if __name__ == "__main__":
	app = App()
	app.mainloop()
