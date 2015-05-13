import os 
import sys

root = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(root, 'site-packages'))

from werobot.robot import werobot
from werobot.session.saekvstorage import SaeKVDBStorage

session_storage = SaeKVDBStorage()

robot = werobot.WeRoBot(token="freesz", enable_session=True,
                        session_storage=session_storage)


@robot.handler
def echo(message):
    return 'Hello World!'


