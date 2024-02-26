from typing import Any, List
import flet as ft
from flet import *
from controls import add_to_control_reference, return_control_reference

control_map = return_control_reference()

class AppHeader(UserControl):
    def __init__(self):
        super().__init__()

    def app_header_instance(self):
        add_to_control_reference("AppHeader", self)


    def app_header_brand(self):
        return Container(
            content= Text(
                "Inventario",
                size = 15
            )
        )
    
    def app_header_search(self):
        return Container(
            width= 320,
            bgcolor= 'white10',
            border_radius= 6,
            padding=8,
            content=Row(
                spacing=10,
                vertical_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Icon(
                        name= icons.SEARCH_ROUNDED,
                        size=17,
                        opacity=0.85
                    ),
                    TextField(
                        border_color= "transparent",
                        height=20,
                        text_size=14,
                        content_padding=0,
                        cursor_color="white",
                        cursor_width=1,
                        color="white",
                        hint_text="Buscar",
                    )
                ],
            ),

        )

    def build(self):
        self.app_header_instance()

        return Container(
            expand= True,
            on_hover= lambda e: self.show_search_bar(e),
            height= 60,
            bgcolor= "#081d33",
            border_radius= 6,
            padding= padding.only(left=15, right=15),
            content=Row(
                expand= True,
                alignment=MainAxisAlignment.SPACE_BETWEEN, 
                controls=[
                    self.app_header_brand(),
                    self.app_header_search(),
                ],
            ),
        )