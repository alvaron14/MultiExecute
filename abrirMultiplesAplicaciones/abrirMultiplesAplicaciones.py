from configobj import ConfigObj
import subprocess, time, os, _thread, editarConfiguracion, csv

def sleepThread():
	while True:
	   time.sleep(5)
	   print(isExecuting)
	   if isExecuting == 1: os._exit(1)
pass

"""
print("La ejecución de este programa suele tardar 20 segundos")
subprocess.Popen("E:\\Launcher\\LauncherPatcher.exe")
subprocess.Popen("E:\\Steam 2.0\\steam.exe")
subprocess.Popen("D:\\TS\\ts3client_win64.exe", shell=True) 
"""
print('---------------------------------------------------------------------------------')
print('En cualquier momento puedes usar el comando \'exit\' para volver al menu anterior')
print('---------------------------------------------------------------------------------')
while True: 
	returnedValue = editarConfiguracion.main()
	if returnedValue != 'Opcion incorrecta': break
config = ConfigObj('example.ini')

selectedConfig = eval(config[str(config['selectedConfig'])])
for key in selectedConfig.keys():
	especificConfig = selectedConfig.get(key)
	if int(especificConfig.get('time')) > 0: time.sleep(int(especificConfig.get('time')))
	subprocess.Popen(str(especificConfig.get('dir')), shell=True) 
	arrayTemp = str(especificConfig.get('dir')).rsplit('\\')
	print('Ejecutado programa: ' + arrayTemp[len(arrayTemp) - 1])

print('Ejecucion completa')

#for key in config.keys():
#	config = ConfigObj('example.ini')
#	if key == 'selectedConfig': print('La configuracion seleccionada es: ' + config.get(key))
#	else: 
#		configValues = eval(config.get(key))
#		for configGroup in configValues:
#			especificConfig = configValues.get(configGroup)
#			print(str(configGroup) + ': {\'dir\': ' + str(especificConfig.get('dir')) + ', \'time\': ' + str(especificConfig.get('time')) + '}')
"""
print(config['exe1']['Directory'] + ' | ' + config['exe1']['Power'])
print(config['exe2']['Directory'] + ' | ' + config['exe2']['Power'])
time.sleep(12)
numThreads = 0
isExecuting = 0
while True:
	try:
		if numThreads == 0:
			_thread.start_new_thread(sleepThread, ())
			numThreads = 1
	except:
		print("thread exploded")
	try:
		isExecuting = 0
		o = subprocess.Popen("E:\\JUEGOS\\RedM\\RedM.exe")
		isExecuting = 1
		o.wait()
		isExecuting = 2
	except:
		print("Fallo try al intentar ejecutar RedM " + isExecuting)
	print("Fallo al intentar ejecutar RedM")
"""