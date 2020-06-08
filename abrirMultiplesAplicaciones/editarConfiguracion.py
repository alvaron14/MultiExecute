from configobj import ConfigObj
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
        dir = input('Direccion del ejecutable:\n\t\t').replace('\\', '\\\\')
        if dir == 'exit': 
            print('\n')
            return False
        treatedDir = re.sub(r'\\{3,}', r'\\', dir)
        confiText = confiText + '\'' + str(i) + '\': {\'dir\': \'' + treatedDir + '\', \'time\': \'0\'}'
        continuar = input('Continuar (y/n)\n\t')
        if continuar == 'n':
            confiText = confiText + '\n' + '}'
            break
        else: confiText = confiText + ',\n'
        i = i + 1
    config = ConfigObj('example.ini')
    config[nombreDeLaConfiguracion] = confiText
    config.write()
    return True
pass

def selectConfig():
    config = ConfigObj('example.ini')
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
    config = ConfigObj('example.ini')
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
    config = ConfigObj('example.ini')
    for key in config.keys():
            if key != 'selectedConfig': print('\t' + key)
    return True
pass

def existConfig():
    config = ConfigObj('example.ini')
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
    config = ConfigObj('example.ini')
    print('¿Que configuracion quieres seleccionar? ')
    printConfigs()
    selConfig = existConfig()
    if selConfig == 'exit': 
        print('\n')
        return False
    configValues = eval(config[selConfig])
    while True:
        dirChoosed, timeChoosed = '',''
        for configGroup in configValues:
            especificConfig = configValues.get(configGroup)
            print(str(configGroup) + ' --> | Direccion del ejecutable: ' + str(especificConfig.get('dir'))
                     + '\n      | Tiempo de espera antes de ejecutarse (s): ' + str(configValues.get('time')))
        while True:
            try:
                dirChoosed = input('¿Que direccion quieres seleccionar?\n\t\t')
                if dirChoosed == 'exit': 
                    print('\n')
                    return False
                break
            except:
                print('\nDireccion incorrecta, selecciona otra\n')
        while dirChoosed != 'exit':
            try:
                timeChoosed = input('¿Que tiempo de espera quieres poner?\n\t\t')
                if timeChoosed == 'exit': 
                    print('\n')
                    return False
                if int(timeChoosed) < 0: raise NameError('Formato tiempo incorrecto')
                break
            except:
                print('\nFormato de tiempo incorrecto, insertar unicamente numeros\n')
        configValues = eval(config[selConfig])
        configValues[dirChoosed]['time'] = int(timeChoosed)
        #No guarda bien el tiempo
        config.write()
    return True
pass

def printSelectedConfig():
    config = ConfigObj('example.ini')
    print('La configuracion seleccionada es: ' + config['selectedConfig'] + '\n')
pass

def exit(): return 'exit'