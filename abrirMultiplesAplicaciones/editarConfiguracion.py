from configobj import ConfigObj
import  re, time
def main():
    switcher = {
                '1': lambda : createConfig(),
                '2': lambda : selectConfig(),
                '3': lambda : borrarCofig(),
                'exit': lambda : exit()
            }
    while True:
        selectedOption = input('Seleccione opcion:' + 
        '\n\t1: Crear configuracion' +
        '\n\t2: Seleccionar configuracion' +
        '\n\t3: Borrar configuracion' +
        '\n\texit: Volver al menu de arranque\n\t')
        return switcher.get(selectedOption, lambda : 'Opcion incorrecta')()
pass

def createConfig():
    i = 0
    nombreDeLaConfiguracion = input('Introduce nombre de la configuración:\n\t')
    confiText = '{\n'
    print('A continuacion introduce las direcciones de los ejecutables en orden de ejecucion\n')
    while True:
        dir = input('Direccion del ejecutable:\n\t').replace('\\', '\\\\')
        if dir == 'exit': break
        treatedDir = re.sub(r'\\{3,}', r'\\', dir)
        #Recordar que se ha modificado la creacion del diccionario
        confiText = confiText + '\'' + str(i) + '\': \'{\'dir\': \'' + treatedDir + '\', \'time\': \'0\'}\''
        #config[nombreDeLaConfiguracion][str(i)] = {'Directory': treatedDir, 'Power': 'shell=False'}
        continuar = input('Continuar (y/n)\n\t')
        if continuar == 'n':
            confiText = confiText + '\n' + '}'
            break
        else: confiText = confiText + ',\n'
        i = i + 1
    config = ConfigObj('example.ini')
    config[nombreDeLaConfiguracion] = confiText
    config.write()
pass

def selectConfig():
    config = ConfigObj('example.ini')
    print('¿Que configuracion quieres seleccionar? ')
    printConfigs()
    selConfig = existConfig()
    config['selectedConfig'] = '' + selConfig
    config.write()
    pass

def borrarCofig():
    config = ConfigObj('example.ini')
    print('¿Que configuracion quieres borrar?')
    printConfigs()
    configABorrar = existConfig()
    if '' + configABorrar == 'exit': return ''
    config.pop('' + configABorrar)
    config.write()
    pass

def printConfigs():
    config = ConfigObj('example.ini')
    for key in config.keys():
            if key != 'selectedConfig': print('\t' + key)
    pass

def existConfig():
    config = ConfigObj('example.ini')
    while True:
        selConfig = input('\t')
        res = ''
        for existsKey in config.keys():
            if selConfig == 'exit': break
            if existsKey == selConfig:
                res = input
                break
        if res != '' or selConfig == 'exit': return selConfig
        print('La condiguracion seleccionada no existe\n')
    pass

def exit(): return 'exit'