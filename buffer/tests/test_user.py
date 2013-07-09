import json

from nose.tools import eq_, raises
from mock import MagicMock, patch

from buffer.user import User

def test_simple_user_request():
  '''
    Test to see if the api is called when a user request is made
  '''

  mocked_api = MagicMock()
  mocked_api.get.return_value = {
    "key": "value"
  }

  with patch('buffer.user.ResponseObject') as mocked_response:
    User(api=mocked_api)
