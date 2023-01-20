from openbb_terminal.rich_config import console

BASE_URL = "http://127.0.0.1:8000/"


class Success:
    def __init__(self, msg=""):
        self.msg = msg
        console.print(msg)


class Failure:
    def __init__(self, msg=""):
        self.msg = msg
        console.print(msg)
