import tkinter
import tkinter.messagebox
import customtkinter
import os
from PIL import Image
import logging 
from memory_profiler import profile


class App(customtkinter.CTk):
    @profile
    def __init__(self):
        super().__init__()

        # configure window
        self.title("PIK")
        # if expand:
        #     self.expand = expand
        # else:
        #     self.height = height
        
        # self.geometry(f"{1200}x{650}")
        customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
        # configure grid layout (4x4)
        # self.grid_columnconfigure(1, weight=1)
        # self.grid_columnconfigure((2, 3), weight=1)
        # self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, rowspan=9, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)
        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="PIK NAV",
                                                             font=customtkinter.CTkFont(size=20, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=10)

        #Dashboard button
        self.Dashboard_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Dashboard",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                    anchor="w", command=self.Dashboard_button_event)
        self.Dashboard_button.grid(row=1, column=0, sticky="ew")

        #Individual button
        self.Individual = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Individual",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                       anchor="w", command=self.Individual_event)
        self.Individual.grid(row=2, column=0, sticky="ew")

        #organization button
        self.Organization = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Organization",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                       anchor="w", command=self.Organization_event)
        self.Organization.grid(row=3, column=0, sticky="ew")

        #Groups button
        self.Groups = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Groups",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                       anchor="w", command=self.Groups_event)
        self.Groups.grid(row=4, column=0, sticky="ew")

        #appearance ui
        self.appearance_mode_label = customtkinter.CTkLabel(self.navigation_frame, text="Appearance Mode:", anchor="s")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.navigation_frame, text="UI Scaling:", anchor="s")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # create Dashboard frame
        self.Dashboard_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.Dashboard_frame.grid_columnconfigure(0, weight=1)

        self.Dashboard_frame_large_image_label = customtkinter.CTkLabel(self.Dashboard_frame, text="",)
        self.Dashboard_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        self.Dashboard_frame_button_1 = customtkinter.CTkButton(self.Dashboard_frame, text="")
        self.Dashboard_frame_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.Dashboard_frame_button_2 = customtkinter.CTkButton(self.Dashboard_frame, text="CTkButton",  compound="right")
        self.Dashboard_frame_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.Dashboard_frame_button_3 = customtkinter.CTkButton(self.Dashboard_frame, text="CTkButton",  compound="top")
        self.Dashboard_frame_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.Dashboard_frame_button_4 = customtkinter.CTkButton(self.Dashboard_frame, text="CTkButton",  compound="bottom", anchor="w")
        self.Dashboard_frame_button_4.grid(row=4, column=0, padx=20, pady=10)

        # create main entry and button
        # self.entry = customtkinter.CTkEntry(self, placeholder_text="Search Entry")
        # self.entry.grid(row=3, column=1, padx=(20, 0), pady=(20, 20), sticky="nsew")

        # self.main_button_1 = customtkinter.CTkButton(master=self,text="Search", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        # self.main_button_1.grid(row=3, column=2, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # create second frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # create image frame
        self.test_image = customtkinter.CTkImage(Image.open("08-09.png"), size=(500, 450))
        self.image_frame = customtkinter.CTkFrame(self.second_frame)
        self.image_frame.grid(row=0, column=1, rowspan=4, padx=(10, 0), pady=(10, 0), sticky="nsew")
        self.ttl_label = customtkinter.CTkLabel(self.image_frame, text="Image Profile", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.ttl_label.grid(row=0, column=0, pady=(10, 0))
        self.image_label = customtkinter.CTkLabel(self.image_frame, text="", image=self.test_image)
        self.image_label.grid(row=1, column=0)

        # create data frame
        self.data_frame = customtkinter.CTkTabview(self.second_frame, bg_color="transparent")
        self.data_frame.grid(row=0, column=2, rowspan=4, columnspan=2, padx=(10, 0), pady=(0, 0), sticky="nsew")
        self.data_frame.add("Profile")
        self.data_frame.add("Social")
        self.data_frame.add("Bio")
        self.data_frame.tab("Profile").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.data_frame.tab("Social").grid_columnconfigure(0, weight=1)
        self.data_frame.tab("Bio").grid_columnconfigure(0, weight=1)

        #profile
        self.case_no = customtkinter.CTkEntry(self.data_frame.tab("Profile"), height=70, placeholder_text="Case Number")
        self.case_no.grid(row=0, column=0, padx=10, pady=(20, 10) ,sticky="nsew")
        self.id_no = customtkinter.CTkEntry(self.data_frame.tab("Profile"), height=70, placeholder_text="ID Number")
        self.id_no.grid(row=0, column=2, padx=10, pady=(20, 10) ,sticky="nsew")
        self.name_1 = customtkinter.CTkEntry(self.data_frame.tab("Profile"), height=70, placeholder_text="First Name Entry")
        self.name_1.grid(row=1, column=0, padx=10, pady=(20, 10) ,sticky="nsew")
        self.name_2 = customtkinter.CTkEntry(self.data_frame.tab("Profile"), height=70, placeholder_text="Middle Name Entry")
        self.name_2.grid(row=1, column=1, padx=10, pady=(20, 10) ,sticky="nsew")
        self.name_3 = customtkinter.CTkEntry(self.data_frame.tab("Profile"), height=70, placeholder_text="Last Name Entry")
        self.name_3.grid(row=1, column=2, padx=10, pady=(20, 10) ,sticky="nsew")
        self.pnumber = customtkinter.CTkEntry(self.data_frame.tab("Profile"), height=70, placeholder_text="Phone number")
        self.pnumber.grid(row=2, column=0, padx=10, pady=(20, 10) ,sticky="nsew")
        self.dob = customtkinter.CTkEntry(self.data_frame.tab("Profile"), height=70, placeholder_text="Date of birth")
        self.dob.grid(row=2, column=1, padx=10, pady=(20, 10) ,sticky="nsew")
        self.caseas = customtkinter.CTkEntry(self.data_frame.tab("Profile"), height=70, placeholder_text="Case Association")
        self.caseas.grid(row=2, column=2, padx=10, pady=(20, 10) ,sticky="nsew")
        self.case_no = customtkinter.CTkEntry(self.data_frame.tab("Profile"), height=70, placeholder_text="Address")
        self.case_no.grid(row=3, column=0, columnspan=2, padx=10, pady=(20, 10) ,sticky="nsew")
        self.location = customtkinter.CTkEntry(self.data_frame.tab("Profile"), height=70, placeholder_text="Location")
        self.location.grid(row=3, column=2, padx=10, pady=(20, 10) ,sticky="nsew")
        self.company = customtkinter.CTkEntry(self.data_frame.tab("Profile"), height=70, placeholder_text="Company")
        self.company.grid(row=4, column=0, columnspan=2, padx=10, pady=(20, 10) ,sticky="nsew")
        self.nation = customtkinter.CTkEntry(self.data_frame.tab("Profile"), height=70, placeholder_text="Nationality")
        self.nation.grid(row=4, column=2, padx=10, pady=(20, 10) ,sticky="nsew")

        self.optionmenu_1 = customtkinter.CTkOptionMenu(self.data_frame.tab("Profile"), dynamic_resizing=True,
                                                        values=["", "Database", "Datawase", "Something-else"])
        self.optionmenu_1.grid(row=0, column=1, padx=20, pady=(20, 10))

        self.combobox_1 = customtkinter.CTkComboBox(self.data_frame.tab("Profile"),
                                                    values=[" ","Male", "Female", "Non-Binary"])
        self.combobox_1.grid(row=5, column=0, padx=10, pady=(20, 10))

        #social
        self.email = customtkinter.CTkEntry(self.data_frame.tab("Social"), height=70, placeholder_text="Email / IP")
        self.email.grid(row=0, column=0, padx=10, pady=(20, 10) ,sticky="nsew")
        self.usern = customtkinter.CTkEntry(self.data_frame.tab("Social"), height=70, placeholder_text="Username")
        self.usern.grid(row=0, column=1, padx=10, pady=(20, 10) ,sticky="nsew")
        self.media = customtkinter.CTkEntry(self.data_frame.tab("Social"), height=70, placeholder_text="Media")
        self.media.grid(row=0, column=2, padx=10, pady=(20, 10) ,sticky="nsew")

        self.email1 = customtkinter.CTkEntry(self.data_frame.tab("Social"), height=70, placeholder_text="Email / IP")
        self.email1.grid(row=1, column=0, padx=10, pady=(20, 10) ,sticky="nsew")
        self.usern1 = customtkinter.CTkEntry(self.data_frame.tab("Social"), height=70, placeholder_text="Username")
        self.usern1.grid(row=1, column=1, padx=10, pady=(20, 10) ,sticky="nsew")
        self.media1 = customtkinter.CTkEntry(self.data_frame.tab("Social"), height=70, placeholder_text="Media")
        self.media1.grid(row=1, column=2, padx=10, pady=(20, 10) ,sticky="nsew")

        self.email2 = customtkinter.CTkEntry(self.data_frame.tab("Social"), height=70, placeholder_text="Email / IP")
        self.email2.grid(row=2, column=0, padx=10, pady=(20, 10) ,sticky="nsew")
        self.usern2 = customtkinter.CTkEntry(self.data_frame.tab("Social"), height=70, placeholder_text="Username")
        self.usern2.grid(row=2, column=1, padx=10, pady=(20, 10) ,sticky="nsew")
        self.media2 = customtkinter.CTkEntry(self.data_frame.tab("Social"), height=70, placeholder_text="Media")
        self.media2.grid(row=2, column=2, padx=10, pady=(20, 10) ,sticky="nsew")

        self.email3 = customtkinter.CTkEntry(self.data_frame.tab("Social"), height=70, placeholder_text="Email / IP")
        self.email3.grid(row=3, column=0, padx=10, pady=(20, 10) ,sticky="nsew")
        self.usern3 = customtkinter.CTkEntry(self.data_frame.tab("Social"), height=70, placeholder_text="Username")
        self.usern3.grid(row=3, column=1, padx=10, pady=(20, 10) ,sticky="nsew")
        self.media3 = customtkinter.CTkEntry(self.data_frame.tab("Social"), height=70, placeholder_text="Media")
        self.media3.grid(row=3, column=2, padx=10, pady=(20, 10) ,sticky="nsew")

        self.email4 = customtkinter.CTkEntry(self.data_frame.tab("Social"), height=70, placeholder_text="Email / IP")
        self.email4.grid(row=4, column=0, padx=10, pady=(20, 10) ,sticky="nsew")
        self.usern4 = customtkinter.CTkEntry(self.data_frame.tab("Social"), height=70, placeholder_text="Username")
        self.usern4.grid(row=4, column=1, padx=10, pady=(20, 10) ,sticky="nsew")
        self.media4 = customtkinter.CTkEntry(self.data_frame.tab("Social"), height=70, placeholder_text="Media")
        self.media4.grid(row=4, column=2, padx=10, pady=(20, 10) ,sticky="nsew")


        #bio-meta
        # create textbox
        self.bgtext = customtkinter.CTkTextbox(self.data_frame.tab("Bio"), width=500)
        self.bgtext.grid(row=0, column=0, columnspan=2, padx=(0, 0), pady=(0, 10), sticky="nsew")

        self.bgtext2 = customtkinter.CTkTextbox(self.data_frame.tab("Bio"), width=500)
        self.bgtext2.grid(row=2, column=0, columnspan=2, padx=(0, 0), pady=(0, 10), sticky="nsew")

        self.combobox_2 = customtkinter.CTkComboBox(self.data_frame.tab("Bio"),
                                                    values=[" ","Submit", "Update", "Delete"])
        self.combobox_2.grid(row=4, column=1, padx=10, pady=(20, 10))

        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # create fourth frame
        self.fourth_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # select default frame
        self.select_frame_by_name("Dashboard")

        # set default values
        self.Groups.configure(state="disabled", text="New Groups Feature")
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
        self.bgtext.insert("0.0", "Background\n\n" + "Profession, age, economic status, other demographic attributes.\n\n")
        self.bgtext2.insert("0.0", "Behaviour\n\n" + "Interests Strengths Weaknesses.\n\n")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.Dashboard_button.configure(fg_color=("gray75", "gray25") if name == "Dashboard" else "transparent")
        self.Individual.configure(fg_color=("gray75", "gray25") if name == "Individual" else "transparent")
        self.Organization.configure(fg_color=("gray75", "gray25") if name == "Organization" else "transparent")
        self.Groups.configure(fg_color=("gray75", "gray25") if name == "Groups" else "transparent")

        # show selected frame
        if name == "Dashboard":
            self.Dashboard_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.Dashboard_frame.grid_forget()
        if name == "Individual":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
            # self.second_frame.grid_rowconfigure(9, weight=1)
        else:
            self.second_frame.grid_forget()
        if name == "Organization":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()
        if name == "frame_4":
            self.fourth_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.fourth_frame.grid_forget()

    def Dashboard_button_event(self):
        self.select_frame_by_name("Dashboard")

    def Individual_event(self):
        self.select_frame_by_name("Individual")

    def Organization_event(self):
        self.select_frame_by_name("Organization")

    def Groups_event(self):
        self.select_frame_by_name("frame_4")

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    app = App()
    app.mainloop()

