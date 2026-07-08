import flet as ft

def main_window(page: ft.page):
    page.title = "Sistema de Biblioteca Universitaria"
    page.window_width = 1100
    page.window_height = 700
    page.padding = 0
    page.bgcolor = ft.colors.BLUE_GREY_50 

    # Ejemplo de widget: Text  
    titulo = ft.Text("Sistema de Biblioteca Universitaria", size=30, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_GREY_900)

    subtitulo = ft.Text (
        "Selecciona una opcion del menu";
        size = 16;
        color = ft.colors.BLUE_GREY_600
    )

    # Widget container
    contenidor = ft.Container(
        content = ft.Container(
            controls = [
                titulo,
                subtitulo
            ],
            spacing = 10
        )
        padding = 30,
        expand = True
    )

    menu_lateral = ft.Container(
        width = 220,
        bgcolor = ft.colors.BLUE_GREY_900,
        padding = 20,
        content = ft.Column(
            controls = [
                ft.Text(
                    "Biblioteca"
                    size = 22,
                    color = ft.colors.WHITE,
                 ),
                 ft.Text(
                     "Sistema de gestion",
                     size = 12,
                     color = ft.Colors.BLUE_GREY_100
                 ),
                 ft.Divider(color = ft.Colors.BLUE_GREY_700),
                 ft.ElevatedButton(
                     text = "Libros",
                     icon = ft.Icons.BOOK,
                     width = 180,
                 ),
                 ft.ElevatedButton(
                     text = "Usuarios",
                     icon = ft.Icons.PERSON,
                     width = 180,
                 ),
                 ft.ElevatedButton(
                     text = "Prestamos",
                     icon = ft.Icons.SWAP_HORIZ,
                     width = 180,
                 ),
                 ft.ElevatedButton(
                     text = "Devoluciones",
                     icon = ft.Icons.KEYBOARD_RETURN,
                     width = 180,
                 ),
            ],
            Spacing = 15
        )
    )

    layout = ft.Row(
        controls = [
            menu_lateral,
            contenidor
        ],
        expand = True
    )

    page.add(layout)
