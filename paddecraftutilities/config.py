import os
import json

userPath = os.path.expanduser("~")
os.makedirs(os.path.join(userPath, ".PaddeCraftSoftware"), exist_ok=True)

class ExistingConfigException(Exception):
    pass

class Config:
    def __init__(self, appName:str) -> None:
        self.appName = appName
        os.makedirs(
            os.path.join(userPath, ".PaddeCraftSoftware", appName), exist_ok=True
        )

    def configFileExists(self, fileName:str) -> bool:
        return os.path.isfile(
            os.path.join(userPath, ".PaddeCraftSoftware", self.appName, fileName + ".json")
        )

    def createConfigFile(self, fileName:str, defaultValues:dict, existOk=False) -> None:
        if not existOk and self.configFileExists(fileName):
            raise ExistingConfigException(
                f"Config file already exists: {format(fileName)}"
            )
        else:
            with open(os.path.join(userPath, ".PaddeCraftSoftware", self.appName, fileName + ".json"), "w") as f:
                f.write(json.dumps(defaultValues))
    
    def readConfigFile(self, fileName:str) -> dict:
        with open(os.path.join(userPath, ".PaddeCraftSoftware", self.appName, fileName + ".json")) as f:
            return json.loads(f.read())
    
    def writeConfigFile(self, fileName:str, values:dict) -> None:
        self.createConfigFile(fileName, values, True)
    
    def deleteConfigFile(self, fileName:str) -> None:
        os.remove(os.path.join(userPath, ".PaddeCraftSoftware", self.appName, fileName + ".json"))
    
    def deleteAllConfigFiles(self) -> None:
        os.rmdir(os.path.join(userPath, ".PaddeCraftSoftware", self.appName))
    
    def getConfigFilePath(self, fileName:str) -> str:
        return os.path.join(userPath, ".PaddeCraftSoftware", self.appName, fileName + ".json")
    
    def getConfigValue(self, fileName:str, key:str) -> str:
        return self.readConfigFile(fileName)[key]
    
    def setConfigValue(self, fileName:str, key:str, value:str) -> None:
        with open(os.path.join(userPath, ".PaddeCraftSoftware", self.appName, fileName + ".json"), "rw") as f:
            config = json.loads(f.read())
            config[key] = value
            f.write(json.dumps(config))