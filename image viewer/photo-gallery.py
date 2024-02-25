import flet
from flet import GridView, Image, Page, border_radius
import os
from os import listdir
import glob

def main(page: Page):
    page.title = "GridView Example"
    page.theme_mode = "dark"
    page.padding = 50
    page.update()

    images = GridView(
        expand=1,
        runs_count=5,
        max_extent=150,
        child_aspect_ratio=1.0,
        spacing=5,
        run_spacing=5,
    )
    page.add(images)

    # r=[]
    # # get the path or directory
    # folder_dir = "E:/Jake/100/shelf/assets/images"
    # for imges in os.listdir(folder_dir):
    # # check if the image ends with png or jpg or jpeg
    #     if (imges.endswith(".png") or images.endswith(".jpg")\
    #         or imges.endswith(".jpeg")):
    #         # display
    #         # print(images)
    #         r.append(imges)

    r=glob.glob("E:/Jake/100/shelf/assets/images/*.png")

    for i in range(len(r)):
        images.controls.append(
            Image(
                # src=f"C:/Users/Jack/Pictures?{i}",
                # src=f"/images?{i}",
                # src=r[imges],
                # src="E:/Jake/100/shelf/assets/images",
                fit="none",
                repeat="noRepeat",
                border_radius=border_radius.all(10),
            )
        )

    # for i in range(0, 60):
    #     images.controls.append(
    #         Image(
    #             # src=f"C:/Users/Jack/Pictures?{i}",
    #             # src=f"/images?{i}",
    #             src=r[imges],
    #             fit="none",
    #             repeat="noRepeat",
    #             border_radius=border_radius.all(10),
    #         )
    #     )
    page.update()


flet.app(target=main,
    assets_dir="assets")
