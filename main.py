import flet as ft
from flet import *
from header import AppHeader
from form import AppForm

def main(page: ft.Page):
    page.bgcolor = '#fdfdfd'
    page.padding = 20
    page.add(
        Column(
            expand=True,
            controls=[
                AppHeader(),
                Divider(height= 2, color="transparent"),
                AppForm()
            ]
        )
    )
    pass


if __name__== "__main__":
    ft.app(target=main)