import logging
import configparser
import pathlib
import os



class config:
    # $ProjectRoot/data/config.ini
    datafolder = os.path.join(pathlib.Path(__file__).parent.parent,"data")
    inipath = os.path.join(pathlib.Path(__file__).parent.parent,"data","config.ini")


    def generateConfig(self):
        # Generates entire configuration anew, this will CLEAR any previous configuration
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

        # Write config to file
        try:
            with open(self.inipath, 'w') as configfile:
                config.write(configfile)
        except Exception as e:
            logging.error("Failed to generate config.ini: "+ str(e))

        logging.info("Success! config.ini has been created!")
        logging.info("Change its parameters and restart the program.")
        exit()


    def checkConfig(self):
        # Check if config.ini is present, or if it's incomplete
        
        # Check if 'data' folder is present
        if not self.datafolder.exists():
            logging.warning("Data folder doesen't exist, creating...")
            try:
                os.mkdir(self.datafolder)
            except Exception as e:
                logging.error("Failed to create data directory: "+ str(e))

        # Check if 'config.ini' is present
        if not self.inipath.exists():
            logging.warning("ini file doesen't exist, creating...")
            self.generateConfig()

        # Check if 'config.ini' is missing parameters
        # I think i should implement a base object and compare it to the current one, ignoring any parameters set

test = config() # TESTING
test.generateConfig() # TESTING
    