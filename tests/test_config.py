from core.config.config_manager import ConfigManager

config = ConfigManager()

print(config.get("platformName"))
print(config.get("udid"))