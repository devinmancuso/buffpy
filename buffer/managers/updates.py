from buffer.models.update import Update

PATHS = {
  'GET_PENDING': 'profiles/%s/updates/pending.json',
  'GET_SENT': 'profiles/%s/updates/sent.json',
}

class Updates(list):

  def __init__(self, api, profile_id):
    self.api = api
    self.profile_id = profile_id

    self.__pending = []
    self.__sent = []

  @property
  def pending(self):
    pending_updates = []
    url = PATHS['GET_PENDING'] % self.profile_id

    response = self.api.get(url=url)
    for update in response['updates']:
      pending_updates.append(update(api=self.api, raw_response=update))

    self.__pending = pending_updates

    return self.__pending

  @property
  def sent(self):
    sent_updates = []
    url = PATHS['GET_SENT'] % self.profile_id

    response = self.api.get(url=url)
    for update in response['updates']:
      sent_updates.append(Update(api=self.api, raw_response=update))

    self.__sent = sent_updates

    return self.__sent