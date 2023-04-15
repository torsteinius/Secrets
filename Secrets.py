import os   


#################################################
# Description:
#   Module to handle secrets
#################################################
class SecretsCls:
    #########################################
    def __init__(self, path = 'Secrets.txt'):
        self.path = path
        self.secrets = {}
        self.load()

    #########################################
    def load(self):
        # Set the path to current folder
        os.chdir(os.path.dirname(os.path.abspath(__file__)))

        with open(self.path, 'r') as f:
            for line in f:
                if line.startswith('#'):
                    continue
                line = line.strip()
                if line == '':
                    continue    
                key, value = line.split('=')
                self.secrets[key] = value
    
    #########################################
    def getSecret(self, key):
        return self.secrets[key]
    

