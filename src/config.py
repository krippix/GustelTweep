import logging
import configparser
import pathlib
import os

class Config:
    # $ProjectRoot/data/config.ini
    datafolder = os.path.join(pathlib.Path(__file__).parent.parent,"data")
    inipath = os.path.join(pathlib.Path(__file__).parent.parent,"data","config.ini")


    def generateConfig(self):
        # Generates entire configuration anew, this will CLEAR any previous configuration
        config = self.get_default_config()

        # Write config to file
        self.writeConfig(config)
        
        logging.info("Success! config.ini has been created!")
        logging.info("Change its parameters and restart the program.")
        exit()


    def checkConfig(self):
        # Check if config.ini is present, or if it's incomplete
        
        # Check if 'data' folder is present
        if not os.path.exists(self.datafolder):
            logging.warning("Data folder doesen't exist, creating...")
            try:
                os.mkdir(self.datafolder)
            except Exception as e:
                logging.error("Failed to create data directory: "+ str(e))

        # Check if 'config.ini' is present
        if not os.path.exists(self.inipath):
            logging.warning("ini file doesen't exist, creating...")
            self.generateConfig()

        # Check if 'config.ini' is missing sections or keys
        defaultconfig = self.get_default_config()
        config = configparser.ConfigParser()
        config.read(self.inipath)

        # Adding missing sections/keys (Using defaultconfig as basefile)
        for section in defaultconfig.sections():
            # Adding sections
            if not section in config.sections():
                logging.warning("Section '"+str(section)+"' missing. Adding it now.")
                config.add_section(section)
            
            # Adding keys to sections
            for defaultkey in defaultconfig.items(section):
                currentKeys = []

                # Create list of current section keys
                for key in config.items(section):
                    currentKeys.append(key[0])

                if not defaultkey[0] in currentKeys:
                    logging.warning("Key '"+str(defaultkey[0])+"' missing. Adding it now.")
                    config[section][defaultkey[0]] = ""
                
        self.writeConfig(config)


    def writeConfig(self, config):
        # Write config to file
        try:
            with open(self.inipath, 'w') as configfile:
                config.write(configfile)
        except Exception as e:
            logging.error("Failed to write 'config.ini': "+ str(e))
            exit()


    def get_default_config(self):
        config = configparser.ConfigParser()

        config['AUTH'] = {
            "consumer_key" : "",
            "consumer_secret" : "",
            "access_token" : "",
            "access_token_secret" : ""
        }

        config['USERS'] = {
            "monitored_users" : ""
        }

        return config
    
    
    def get_config(self, category, key):
        config = configparser.ConfigParser()
        
        self.checkConfig()

        try:
            config.read(self.inipath) 
        except Exception as e:
            logging.error("Failed to read 'config.ini' "+ str(e))

# if config.py is run directly it will check and regenerate the 'config.ini'
test = Config()
test.checkConfig() 
    