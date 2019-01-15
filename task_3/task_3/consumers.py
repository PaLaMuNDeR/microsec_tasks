import json
import logging
from channels import Group
from channels.sessions import channel_session
from .models import Temperature

log = logging.getLogger(__name__)

@channel_session
def ws_connect(message):
    # Extract the values
    try:
        prefix, label = message['path'].decode('ascii').strip('/').split('/')
        if prefix != 'temperature':
            log.debug('1 invalid ws path=%s', message['path'])
        temperature = Temperature.objects.last()
    except ValueError:
        log.debug('invalid ws path=%s', message['path'])
        return
    log.debug('last temperature=%s ',
        temperature.value)
    log.debug('prefix=%s ',
        prefix)
    log.debug('label=%s ',
        label)

    Group('temperature', channel_layer=message.channel_layer).add(str(temperature.value))

    message.channel_session['temperature'] = temperature.value

