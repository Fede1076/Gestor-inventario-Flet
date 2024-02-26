from typing import Any, List
from flet import *
from flet_core.control import Control
from flet_core.ref import Ref
from flet_core.types import ClipBehavior
from controls import add_to_control_reference

class AppForm(UserControl):
    def __init__(self):
        super().__init__()

    def app_form_input_instance(self):
        add_to_control_reference("AppForm", self)

    def app_form_input_field(self, name:str, expand:int):
        return Container(
            expand=expand,
            height=45,
            bgcolor= "#ebebeb",
            border_radius=6,
            padding=8,
            content=Column(
                spacing=1,
                controls=[
                    Text(
                        value=name, size=9, color="black", weight="bold"
                    ),
                    TextField(
                        border_color="transparent",
                        height=20,
                        text_size=13,
                        content_padding=0,
                        cursor_color="black",
                        cursor_width=1,
                        cursor_height=18,
                        color="black",
                    )
                ],
            ),
        )

    def build(self):
        self.app_form_input_instance
        return Container(
            expand= True,
            height=190,
            bgcolor= "white10",
            border= border.all(1, "#ebebeb"),
            border_radius=8,
            padding=15,
            content=Column(
                expand=True,
                controls=[
                    Row(
                        controls=[
                            self.app_form_input_field("Field *", True)
                        ],
                    ),
                    Row(
                        controls=[
                            self.app_form_input_field("Field one", 3),
                            self.app_form_input_field("Field two", 1),
                            self.app_form_input_field("Field three", 1),
                        ],
                    ),
                    Row(
                        alignment=MainAxisAlignment.END,
                        controls=[
                            
                        ]
                    )
                ],
            ),
        )