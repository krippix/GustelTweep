import tweepy
import logging
import config

# ToDo: set loglevel on boot, read it from config
config = config.Config()

logging.basicConfig(filename=config.logfile, encoding='utf-8', level=config.get_loglevel())