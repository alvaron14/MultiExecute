from configobj import ConfigObj
import subprocess, time, os, editarConfiguracion

print('---------------------------------------------------------------------------------')
print('En cualquier momento puedes usar el comando \'exit\' para volver al menu anterior')
print('---------------------------------------------------------------------------------')
config = ConfigObj('config.ini')
if len(config) == 0: 
	config['selectedConfig'] = None
	config.write()
while True: 
	returnedValue = editarConfiguracion.main()
	if returnedValue != 'Opcion incorrecta': break
config = ConfigObj('config.ini')

selectedConfig = eval(config[str(config['selectedConfig'])])
for key in selectedConfig.keys():
	especificConfig = selectedConfig.get(key)
	if int(especificConfig.get('time')) > 0: time.sleep(int(especificConfig.get('time')))
	subprocess.Popen(str(especificConfig.get('dir')), shell=True) 
	arrayTemp = str(especificConfig.get('dir')).rsplit('\\')
	print('Ejecutado programa: ' + arrayTemp[len(arrayTemp) - 1])

print('Ejecucion completa')
time.sleep(1)
os._exit(1)