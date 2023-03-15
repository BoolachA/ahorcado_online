#Parte gráfica
import eel, os

def salir(*kw):
    os._exit(0)

def main():
    eel.init('webUI')
    eel.start('index.html', close_callback=salir)


if __name__ == "__main__":
    main()