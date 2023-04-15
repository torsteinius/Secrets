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
        # Remember the current working directory
        cwd = os.getcwd()

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
        
        # Set the path back to the original working directory
        os.chdir(cwd)
    
    #########################################
    def getSecret(self, key):
        return self.secrets[key]
    

