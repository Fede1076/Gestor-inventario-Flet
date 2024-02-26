from flet import *
from controls import return_control_reference

control_map = return_control_reference()


def return_form_button():
    return Container(
        alignment=alignment.center,
        content=ElevatedButton(
            on_click=lambda e: get_input_data(e),
            bgcolor="#081d33",
            color="white",
            content=Row(
                controls=[
                    Icon(
                        name=icons.ADD_ROUNDED,
                        size=12,
                    ),
                    Text(
                        "Add input Field to table",
                        size=11,
                        weight="bold",
                    ),
                ],
            ),
            style=ButtonStyle(
                shape={
                    "": RoundedRectangleBorder(radius=6),
                },
                color={
                    "": "white",
                },
            ),
            height=42,
            width=220,
        ),
    )