import configparser
config=configparser.RawConfigParser()

config.read("..\\configuration\\config.ini")


class ReadConfig:
    @staticmethod
    def getapplicationURL():
        urls=config.get('genericdetails','url')
        return urls
