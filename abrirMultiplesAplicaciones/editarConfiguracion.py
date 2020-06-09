from configobj import ConfigObj
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from WindowManager import WindowManager
import  re, time
def main():
    switcher = {
                '1': lambda : createConfig(),
                '2': lambda : selectConfig(),
                '3': lambda : borrarCofig(),
                '4': lambda : añadirTiempos(),
                'exit': lambda : exit()
            }
    printSelectedConfig()
    while True:
        selectedOption = input('Seleccione opcion:' + 
        '\n\t1: Crear configuracion' +
        '\n\t2: Seleccionar configuracion' +
        '\n\t3: Borrar configuracion' +
        '\n\t4: Añadir tiempos de espera a la configuracion' +
        '\n\texit: Volver al menu de arranque\n\t\t')
        print('\n')
        if ConfigObj('config.ini')['selectedConfig'] == None and selectedOption != '1': print('Necesitas crear una configuracion\n')
        else:
            returnedValue = switcher.get(selectedOption, lambda : 'Opcion incorrecta')() 
            if returnedValue == 'exit': return ''
pass

def createConfig():
    i = 0
    nombreDeLaConfiguracion = input('Introduce nombre de la configuración:\n\t\t')
    if nombreDeLaConfiguracion == 'exit': 
        print('\n')
        return False
    confiText = '{\n'
    print('A continuacion introduce las direcciones de los ejecutables en orden de ejecucion\n')
    while True:
        Tk().withdraw()
        dir = askopenfilename().replace('/', '\\\\')
        if dir == '': 
            print('\n')
            return False
        treatedDir = re.sub(r'\\{3,}', r'\\', dir)
        confiText = confiText + '\'' + str(i) + '\': {\'dir\': \'' + treatedDir + '\', \'time\': \'0\'}'
        w = WindowManager()
        #Nombre del ejecutable
        w.find_and_set(".*python.exe*")
        continuar = input('Continuar (y/n)\n\t')
        if continuar != 'y' and continuar != 'yes':
            confiText = confiText + '\n' + '}'
            break
        else: confiText = confiText + ',\n'
        i = i + 1
    config = ConfigObj('config.ini')
    if ConfigObj('config.ini')['selectedConfig'] == str(None) : config['selectedConfig'] = nombreDeLaConfiguracion
    config[nombreDeLaConfiguracion] = confiText
    config.write()
    return True
pass

def selectConfig():
    config = ConfigObj('config.ini')
    print('¿Que configuracion quieres seleccionar? ')
    printConfigs()
    selConfig = existConfig()
    if selConfig == 'exit': 
        print('\n')
        return False
    config['selectedConfig'] = '' + selConfig
    config.write()
    printSelectedConfig()
    return True
pass

def borrarCofig():
    config = ConfigObj('config.ini')
    print('¿Que configuracion quieres borrar?')
    printConfigs()
    configABorrar = existConfig()
    if configABorrar == 'exit': 
        print('\n')
        return False
    config.pop('' + configABorrar)
    config.write()
    if configABorrar == config['selectedConfig']: selectConfig()
    return True
pass

def printConfigs():
    config = ConfigObj('config.ini')
    for key in config.keys():
            if key != 'selectedConfig': print('\t' + key)
    return True
pass

def existConfig():
    config = ConfigObj('config.ini')
    while True:
        selConfig = input('\t\t')
        res = ''
        for existsKey in config.keys():
            if selConfig == 'exit': break
            if existsKey == selConfig:
                res = input
                break
        if res != '' or selConfig == 'exit': return selConfig
        print('La condiguracion seleccionada no existe\nSelecciona otra configuracion')
pass

def añadirTiempos():
    config = ConfigObj('config.ini')
    print('¿Que configuracion quieres seleccionar? ')
    printConfigs()
    selConfig = existConfig()
    if selConfig == 'exit': 
        print('\n')
        return False
    configValues = eval(config[selConfig])
    while True:
        dirChosen, timeChosen = '',''
        for configGroup in configValues.keys():
            especificConfig = configValues.get(configGroup)
            print(str(configGroup) + ' --> | Direccion del ejecutable: ' + str(especificConfig.get('dir'))
                     + '\n      | Tiempo de espera antes de ejecutarse (s): ' + str(especificConfig.get('time')))
        while True:
            try:
                dirChosen = input('¿Que direccion quieres seleccionar?\n\t\t')
                if dirChosen == 'exit': 
                    print('\n')
                    return False
                break
            except:
                print('\nDireccion incorrecta, selecciona otra\n')
        while dirChosen != 'exit':
            try:
                timeChosen = input('¿Que tiempo de espera quieres poner?\n\t\t')
                if timeChosen == 'exit': 
                    print('\n')
                    return False
                if int(timeChosen) < 0: raise NameError('Formato tiempo incorrecto')
                break
            except:
                print('\nFormato de tiempo incorrecto, insertar unicamente numeros\n')
        configValues = eval(config[selConfig])
        configValues.get(dirChosen)['time'] = str(timeChosen)
        config[selConfig] = str(configValues)
        config.write()
    return True
pass

def printSelectedConfig():
    config = ConfigObj('config.ini')
    if config['selectedConfig'] == str(None): print('No hay ninguna configuracion seleccionada\n')
    else: print('La configuracion seleccionada es: ' + config['selectedConfig'] + '\n')
pass

def exit(): return 'exit'