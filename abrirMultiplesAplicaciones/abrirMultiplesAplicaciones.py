from pynput import keyboard
from pynput.keyboard import Key, Controller

from configobj import ConfigObj
import subprocess, time, os, editarConfiguracion, _thread, asyncio



def sleepThread():
	global pressedKey
	global toConfig
	pressedKey = False
	print('Presiona cualquier tecla para ir al menu de configuracion, de lo contrario en 4 segundos se ejecutara la configuracion seleccionada')
	while not(pressedKey): ''
	keyboardKey = Controller()
	keyboardKey.press(Key.backspace)
	while not(isExecuting):
		returnedValue = editarConfiguracion.main()
		if returnedValue != 'Opcion incorrecta': break
	toConfig = False
	return True
pass

def on_press(key):
	global pressedKey
	global toConfig
	pressedKey = True
	toConfig = True
pass

def main():
	print('---------------------------------------------------------------------------------')
	print('En cualquier momento puedes usar el comando \'exit\' para volver al menu anterior')
	print('---------------------------------------------------------------------------------')
	config = ConfigObj('config.ini')

	global isExecuting
	global toConfig
	isExecuting = False
	toConfig = False
	if len(config) == 0: 
		config['selectedConfig'] = None
		config.write()
		while True:
			returnedValue = editarConfiguracion.main()
			if returnedValue != 'Opcion incorrecta': break
	_thread.start_new_thread(sleepThread, ())
	print('\n' + ConfigObj('config.ini')['selectedConfig'] + '\n')
	time.sleep(4)
	while toConfig: ''
	isExecuting = True
	config = ConfigObj('config.ini')
	selectedConfig = eval(config[str(config['selectedConfig'])])
	for key in selectedConfig.keys():
		especificConfig = selectedConfig.get(key)
		if int(especificConfig.get('time')) > 0: time.sleep(int(especificConfig.get('time')))
		subprocess.Popen(str(especificConfig.get('dir')), shell=True) 
		arrayTemp = str(especificConfig.get('dir')).rsplit('\\')
		print('Ejecutado programa: ' + arrayTemp[len(arrayTemp) - 1])

	print('Ejecucion completa')
	time.sleep(2)
	os._exit(1)
pass


listener = keyboard.Listener(on_press=on_press)
listener.start()
pressedKey = False
toConfig = False
main()