import flet as ft

def main(page: ft.Page):
    
    page.add(ft.Text("Registro de Participantes",size=30))
    nombre=page.add(ft.TextField(label="Nombre Completo"))
    correo=page.add(ft.TextField(label="Correo Electronico"))
    
    taller=page.add(ft.Dropdown(
        options=[
            ft.DropdownOption(key="1", text="Python para principiantes"),
            ft.DropdownOption(key="2", text="Python para intermedio"),
            ft.DropdownOption(key="3", text="Análisis de Datos con Pandas"),
        ]
    ))
    
    pago=page.add(ft.RadioGroup(
        content=ft.Column([
            ft.Radio(value="Python para principiantes", label="Python para principiantes"),
            ft.Radio(value="Python para intermedio", label="Python para intermedio"),
            ft.Radio(value="Análisis de Datos con Pandas", label="Análisis de Datos con Pandas"),
        ])
    ))
    
    requiere=page.add(ft.Checkbox(label="Requiere computadora portátil"))
    
    nivel=page.add(ft.Slider(label="{value}", value=1, max=5, min=1, divisions=5, width=400))

    
    def resume():
        page.add(ft.Text(f"--- FICHA DEL PARTICIPANTE ---\n Nombre: {nombre}\n Email:{correo}\n Taller{taller} \n Pago{pago}\n Requiere Portatil: {requiere}\n Nivel:{nivel}\n --- Gracias por su registro ---"))    
    
    
ft.run(main) 
