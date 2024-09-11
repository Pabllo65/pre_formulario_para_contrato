import flet as ft
from flet import Text, TextField, FilledButton, Row, Banner, colors, Icon, icons, TextButton


def main(page):

    dict_values = {
    'comtratante': '',
    'medida_judicial': '',
    'outra_parte': '',
    'prolabore': '',
    'exito': '',
    'foro': '',
    'data': '',
    }

    def gerar_contrato(e):
        dict_values['comtratante']= contratante.value
        dict_values['medida_judicial']= medida_judicial.value
        dict_values['outra_parte']= outra_parte.value
        dict_values['prolabore']= prolabore.value
        dict_values['exito']= exito.value
        dict_values['foro']= foro.value
        dict_values['data']= data.value

        for val in dict_values.values():
            if not val:
                page.banner.open=True
                page.update()
                return
        print("Já e possivel gerar o contrato!")

    def fecha_banner(e):
        page.banner.open=False
        page.update()
        


    page.banner = Banner(
        bgcolor=colors.AMBER_100,
        leading=Icon(
            icons.DANGEROUS_SHARP,
            color=colors.RED_400,
            size=40
        ),
        content=Text("Opa todos os campos obrigatorio !"),
        actions=[
            TextButton(
                "entendi",
                on_click= fecha_banner
            )
        ]

    )
                
            


    titulo = Text(value="Gerador de contratos de Prestação de serviços Advocatícios",weight="bold", size=20,color="blue")
    contratante = TextField(label="Nome do contratante", autofocus=True)
    medida_judicial = TextField(label="Medida Judicial")
    outra_parte =  TextField(label="Outra parte")
    prolabore =  TextField(label="Prolabore", prefix_text='R$ ')
    exito =  TextField(label="Exito", suffix_text=" %")
    foro =  TextField(label="Foro")
    data =  TextField(label="Data")
    botao_gerar = FilledButton("Gerar contrato", on_click=gerar_contrato)

    page.add(
        Row(
            controls=[
                titulo
            ]
        ),
        Row(
            controls=[
                contratante
            ]
        ),
        Row(
            controls=[
                medida_judicial,
                outra_parte,
            ]
        ),
        Row(
            controls=[
                prolabore,
                exito,
            ]
        ),
        Row(
            controls=[
                foro,
                data,
            ]
        ),
        Row(
            controls=[
                botao_gerar
            ]
        )

    )

    botao_gerar = FilledButton(text="Gerar contrato")

    
ft.app(target=main)
