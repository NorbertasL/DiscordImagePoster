import configparser


class Config:
    """
    Singleton class that allows easy loading of config entries.
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, '_initialized'):
            self._initialized = True
            self.data = {}
            self.load()

    def load(self, path='config.ini'):
        """
        Load config file from the given path.
        """
        config = configparser.ConfigParser()
        config.read(path)
        self.data = {section: dict(config.items(section)) for section in config.sections()}

    def get(self, section, key):
        """
        Retrieve a configuration value from the loaded data.

        Args:
            section (str): The section in the config file.
            key (str): The key within the section.

        Returns:
            str: The configuration value if found, otherwise Not Found!.
        """
        return self.data.get(section, {}).get(key, f"{section}->{key} Not Found!")
