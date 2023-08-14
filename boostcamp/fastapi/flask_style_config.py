from typing import Dict, Any
import yaml

class Config(object):
    ENV: str = None
    TESTING: bool = False
    DB: Dict[str, Any] = {}
    
    @classmethod
    def from_yaml(cls, config_path: str):
        with open(config_path, 'r') as config_file:
            config = yaml.load(config_file, Loader=yaml.FullLoader)
            
        cls.ENV = config["env"]
        cls.DB = config["db"]
        return cls

class DevConfig(Config):
    pass

class ProdConfig(Config):
    pass

config = DevConfig.from_yaml("dev_config.yaml")
assert config.ENV == "dev"
print(config.ENV,)
# assert config.DB == 'expected'