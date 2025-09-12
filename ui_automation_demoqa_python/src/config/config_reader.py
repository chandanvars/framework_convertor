import configparser
import os


class ConfigReader:
    def __init__(self):
        self.config = configparser.ConfigParser()
        config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config.ini')
        self.config.read(config_path)
    
    def get_property(self, key, section='DEFAULT'):
        """Get property value from config file"""
        return self.config.get(section, key)
    
    def get_browser(self):
        """Get browser type from config"""
        return self.get_property('browser')
    
    def get_base_url(self):
        """Get base URL from config"""
        return self.get_property('base_url')
    
    def get_implicit_wait(self):
        """Get implicit wait time from config"""
        return int(self.get_property('implicit_wait'))
    
    def get_explicit_wait(self):
        """Get explicit wait time from config"""
        return int(self.get_property('explicit_wait'))


# Create global config instance
config_reader = ConfigReader()