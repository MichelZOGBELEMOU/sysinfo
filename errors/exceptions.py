"""Custom argparse errors for friendly CLI messages"""
import argparse
class InvalidOptionError(argparse.ArgumentError):
    """Describe an Invalid option exeption"""
    pass
class InvalidOptionTypeError(argparse.ArgumentTypeError):
    """Describe an Invalid option type"""
    pass
class CustomParser(argparse.ArgumentParser):
    def error(self, message):
        bad_option = message.split(":")[-1].strip()
        raise InvalidOptionError(None,f"Invalid option {bad_option}")