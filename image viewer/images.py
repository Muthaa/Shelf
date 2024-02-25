import flet
from flet import Image, Page, Row, border_radius
import random

def main(page: Page):
    page.title = "Images Example"
    page.theme_mode = "dark"
    page.padding = 50
    page.update()

    img = Image(
        src=f"E:/Jake/100/shelf/assets/images/4.png",
        # src=f"/images/3.png",
        width=200,
        height=200,
        fit="contain",
    )
    images = Row(expand=1, wrap=False, scroll="always")

    page.add(img, images)

    for i in range(0, 30):
        # rane= [lambda i:i for i in range(30)]
        rane=random.randrange(1,31)     # create a list import dir all *.png
        images.controls.append(
            Image(
                # src=f"/images**",
                src=f"/images/{rane}.png",
                width=200,
                height=200,
                fit="contain",
                repeat="noRepeat",
                border_radius=border_radius.all(10),
            )
        )
    page.update()


flet.app(target=main,
    assets_dir="assets")
