#Python Script
#Playground #1

def message_creator(text):
    match text:
        case 'computadora':
            return 'Con mi computadora puedo programar usando Python'
        case 'telefono':
            return 'En mi celular puedo aprender usando la app de Platzi'
        case 'cable':
            return '¡Hay un cable en mi bota!'
        case _:
            return 'Articulo no encontrado'





text = 'computadora'
response = message_creator(text)
print(response)