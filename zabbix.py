# -*- coding: utf-8 -*-

'''
Support for Zabbix
'''

def hostgroup_present(name, url, username, password):
  '''
  Makes sure the given hostgroup exists. If it doesn't exist it will be created.
  '''

  ret = {'name': name,
    'changes': {},
    'result': False,
    'comment': 'An error occured.'
  }

  if __salt__['zabbix.existsHostgroup'](name, url, username, password):
    ret['result'] = True
    ret['comment'] = 'Hostgroup already exists.'
  else:
    if __salt__['zabbix.createHostgroup'](name, url, username, password):
      ret['result'] = True
      ret['changes'][name] = {'old': 'Absent', 'new': 'Created'}
      ret['comment'] = 'Hostgroup created.'

  return ret

# TODO: update data
def host_present(name, data, url, username, password):
  '''
  Makes sure the given host exists. If it doesn't exist it will be created.
  '''

  ret = {'name': name,
    'changes': {},
    'result': False,
    'comment': 'An error occured.'
  }

  if __salt__['zabbix.existsHost'](name, url, username, password):
#    if __salt__['zabbix.updateHost'](name, data, url, username, password):
      ret['result'] = True
      ret['comment'] = 'Host exists and is up to date.'
#    else:
#      ret['result'] = True
#      ret['changes'][name] = {'old': 'Exists', 'new': 'Updated'}
#      ret['comment'] = 'Host exists but needed update'
  else:
    if __salt__['zabbix.createHost'](name, data, url, username, password):
      ret['result'] = True
      ret['changes'][name] = {'old': 'Absent', 'new': 'Created'}
      ret['comment'] = 'Host created.'

  return ret

# TODO: update data
def template_present(name, data, url, username, password):
  '''
  Makes sure the given template exists. If it doesn't exist it will be created.
  '''

  ret = {'name': name,
    'changes': {},
    'result': False,
    'comment': 'An error occured.'
  }

  if __salt__['zabbix.existsTemplate'](name, url, username, password):
    ret['result'] = True
    ret['comment'] = 'Template already exists.'
  else:
    if __salt__['zabbix.createTemplate'](name, data, url, username, password):
      ret['result'] = True
      ret['changes'][name] = {'old': 'Absent', 'new': 'Created'}
      ret['comment'] = 'Template created.'

  return ret

# TODO: update data
def item_present(name, data, url, username, password):
  '''
  Makes sure the given item exists. If it doesn't exist it will be created.
  '''

  ret = {'name': name,
    'changes': {},
    'result': False,
    'comment': 'An error occured.'
  }

  if __salt__['zabbix.existsItem'](data['key_'], url, username, password):
    ret['result'] = True
    ret['comment'] = 'Item already exists.'
  else:
    if __salt__['zabbix.createItem'](name, data, url, username, password):
      ret['result'] = True
      ret['changes'][name] = {'old': 'Absent', 'new': 'Created'}
      ret['comment'] = 'Item created.'

  return ret

