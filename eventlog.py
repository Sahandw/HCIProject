import os
def createFile():
	with open('EventLog.txt' , 'w') as logFile:
		logFile.writelines('Event Log File\n')
	logFile.close()


def writeEvent(event):
	with open('EventLog.txt' , 'a') as logFile:
		logFile.writelines(event + '\n')
	logFile.close()

def saveRecordedScenario(scenarioName):
	with open('EventLog.txt' , 'r') as logFile:
		log = logFile.read()
	logFile.close()
	ScenarioEvents = log[log.rfind('Record') : log.rfind('Save')] + 'Save'
	with open('Scenarios/' + scenarioName + '.txt' , 'w') as logFile:
		logFile.write(ScenarioEvents)
	logFile.close()

def getScenarioEvents(scenarioName):
	scenarioEvents = []
	with open('Scenarios/' + scenarioName + '.txt' , 'r') as logFile:
		scenarioEvents = logFile.readlines()
	logFile.close()
	return scenarioEvents

def deleteScenarioFile(scnearioName):
	try:
		os.remove('Scenarios/' + scnearioName + '.txt')
	except Exception as e:
		print(e)

def saveSelectedScenario(scenarioName , scenarioEvents):
	with open('Scenarios/' + scenarioName + '.txt' , 'w') as logFile:
		for element in scenarioEvents:
			logFile.writelines(element)
	logFile.close()