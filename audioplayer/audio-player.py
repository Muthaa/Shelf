import logging
import os
import flet
from flet import Audio, ElevatedButton, Page, Card, ListTile, Icon, Column, Container, Row, border, border_radius
from flet import Text, AlertDialog, ElevatedButton, OutlinedButton, icons, TextButton, alignment, colors, WindowDragArea
from flet import IconButton, AppBar, theme, Divider, VerticalDivider

logging.basicConfig(level=logging.DEBUG)

file = "E:/404/-/LofiBrownMix.mp3"
# DEEP_ORANGE
LIGHT_SEED_COLOR = colors.TEAL
DARK_SEED_COLOR = colors.TEAL

def main(page: Page):
    page.window_title_bar_hidden = True
    # page.window_title_bar_buttons_hidden = True

    # set page properties
    page.horizontal_alignment = "center"
    page.vertical_alignment = "spaceBetween"
    
    page.title = "Audio Player"
    page.theme_mode = "dark"
    page.theme = theme.Theme(color_scheme_seed=LIGHT_SEED_COLOR, use_material3=True)
    page.dark_theme = theme.Theme(color_scheme_seed=DARK_SEED_COLOR, use_material3=True)
    # page.padding = 50
    page.update()

    def toggle_theme_mode(e):
        page.theme_mode = "dark" if page.theme_mode == "light" else "light"
        lightMode.icon = (
            icons.WB_SUNNY_OUTLINED if page.theme_mode == "light" else icons.WB_SUNNY
        )
        page.update()

    lightMode = IconButton(
        icons.WB_SUNNY_OUTLINED if page.theme_mode == "light" else icons.WB_SUNNY,
        on_click=toggle_theme_mode,
    )

    def toggle_material(e):
        use_material3 = not page.theme.use_material3
        page.theme = theme.Theme(
            color_scheme_seed=LIGHT_SEED_COLOR, use_material3=use_material3
        )
        page.dark_theme = theme.Theme(
            color_scheme_seed=DARK_SEED_COLOR, use_material3=use_material3
        )
        materialMode.icon = (
            icons.INFO_OUTLINE_SHARP if page.theme.use_material3 else icons.INFO_OUTLINED
        )
        page.update()

    materialMode = IconButton(
        icons.INFO_OUTLINE_SHARP if page.theme.use_material3 else icons.INFO_OUTLINED,
        on_click=toggle_material,
    )

    # page.appbar = AppBar(
    #     # toolbar_height=100,
    #     # bgcolor=colors.SECONDARY_CONTAINER,
    #     leading=Icon(icons.BUBBLE_CHART_OUTLINED,size=40),
    #     # color=colors.TEAL,
    #     leading_width=30,
    #     title=Text("window\'s #$&^!", size=30),
    #     center_title=True,
    #     actions=[
    #         lightMode,
    #         materialMode,
    #         IconButton(icons.CLOSE_OUTLINED, on_click=lambda _: page.window_close())
    #     ],
    # )
    # def window_event(e):
    #     if e.data == "close":
    #         page.dialog = confirm_dialog
    #         confirm_dialog.open = True
    #         page.update()

    # page.window_prevent_close = True
    # page.on_window_event = window_event

    # def yes_click(e):
    #     page.window_destroy()

    # def no_click(e):
    #     confirm_dialog.open = False
    #     page.update()

    # confirm_dialog = AlertDialog(
    #     modal=True,
    #     title=Text("Please confirm"),
    #     content=Text("Do you really want to exit this app?"),
    #     actions=[
    #         ElevatedButton("Yes", on_click=yes_click),
    #         OutlinedButton("No", on_click=no_click),
    #     ],
    #     actions_alignment="end",
    # )

    page.add(Row(#window drag area
            [   
                Icon(name=icons.BUBBLE_CHART_OUTLINED, size=40),
                # Icon(name=icons.SIX_FT_APART_OUTLINED, color=colors.BLUE, size=30),
                WindowDragArea(Container(Text("window\'s #$&^!", size=30), alignment=alignment.center, padding=5), expand=True),
                # WindowDragArea(Container(Text("window\'s #$&^!", size=25, color="blue"), padding=5), expand=True),
                IconButton(icons.WB_SUNNY_OUTLINED if page.theme_mode == "light" else icons.WB_SUNNY, on_click=toggle_theme_mode),
                IconButton(icons.INFO_OUTLINE_SHARP if page.theme.use_material3 else icons.INFO_OUTLINED, on_click=toggle_material),
                IconButton(icons.CLOSE_OUTLINED, on_click=lambda _: page.window_close())
            ]
        ),)
    # page.add(Text('window\'s"#"$&^!'))

    def volume_down(_):
        audio1.volume -= 0.1
        audio1.update()

    def volume_up(_):
        audio1.volume += 0.1
        audio1.update()

    def balance_left(_):
        audio1.balance -= 0.1
        audio1.update()

    def balance_right(_):
        audio1.balance += 0.1
        audio1.update()

    audio1 = Audio(
        src=file,
        autoplay=False,
        volume=1,
        balance=0,
        on_loaded=lambda _: print("Loaded"),
        on_duration_changed=lambda e: print("Duration changed:", e.data),
        on_position_changed=lambda e: print("Position changed:", e.data),
        on_state_changed=lambda e: print("State changed:", e.data),
        on_seek_complete=lambda _: print("Seek complete"),
    )
    page.overlay.append(audio1)
    page.add(
        Row([
            Card(
                content=Container(
                    content=Column(
                        [
                            ListTile(
                                leading=Icon(icons.ALBUM),
                                title=Text("The Enchanted Nightingale"),
                                subtitle=Text(
                                    "Music by Julie Gable. Lyrics by Sidney Stein."
                                ),
                            ),
                            Row(
                                [TextButton("Buy tickets"), TextButton("Listen")],
                                alignment="end",
                            ),
                        ]
                    ),

                    alignment=alignment.center,
                    width=400,
                    padding=10,
                )
            ),
            VerticalDivider(),
            Card(
                content=Container(
                    content=Column(
                        [
                            ListTile(
                                leading=Icon(icons.ALBUM),
                                title=Text("The Enchanted Nightingale"),
                                subtitle=Text(
                                    "Music by Julie Gable. Lyrics by Sidney Stein."
                                ),
                            ),
                            Row(
                                [TextButton("Buy tickets"), TextButton("Listen")],
                                alignment="end",
                            ),
                        ]
                    ),

                    alignment=alignment.center,
                    width=400,
                    padding=10,
                )
            ),
            VerticalDivider(width=10),
            # Container(
                    
            #         content=Column(
            #             Text("1"),
            #             Text("2")
            #             ),
            #         bgcolor=colors.AMBER_100,
            #         height=400,
            #     ),
            
            ]),
        
        Divider(),

        Row(
            [Container(
                Row([
                    ElevatedButton("Play", icon="PLAY_CIRCLE_OUTLINE", on_click=lambda _: audio1.play()),
                    ElevatedButton("Pause", icon="MOTION_PHOTOS_PAUSE_OUTLINED", on_click=lambda _: audio1.pause()),
                    ElevatedButton("Resume", icon="PLAY_CIRCLE_OUTLINED", on_click=lambda _: audio1.resume()),
                    ElevatedButton("Stop", icon="STOP_CIRCLE_OUTLINED", on_click=lambda _: audio1.release()),
                    ElevatedButton("Seek 2s", icon="FAST_REWIND_OUTLINED",  on_click=lambda _: audio1.seek(2000)),
                    ElevatedButton("Seek1 2s", icon="FORWARD_5_OUTLINED",  on_click=lambda _: audio1.seek(-2000)),
                    ElevatedButton("Volume down", icon="VOLUME_DOWN_OUTLINED", on_click=volume_down),
                    ElevatedButton("Volume up", icon="VOLUME_UP_OUTLINED", on_click=volume_up),
                ]), bgcolor=" ", alignment=alignment.center, border=border.all(1, colors.TEAL),
                border_radius=border_radius.all(10), padding=10, expand=True)
            ]),
            Row([

                ElevatedButton("Balance left", icon="SPEAKER_OUTLINED", on_click=balance_left),
                ElevatedButton("Balance right", icon="SPEAKER_OUTLINED", on_click=balance_right),
                ElevatedButton(
                    "Get duration", icon="TIMER_OUTLINED", on_click=lambda _: print("Duration:", audio1.get_duration())
                    ),
                ElevatedButton(
                    "Get current position", icon="TIMELINE_ROUNDED", 
                    on_click=lambda _: print("Current position:", audio1.get_duration()),
                     ),
            ]),

    )
                                            

flet.app(target=main)
