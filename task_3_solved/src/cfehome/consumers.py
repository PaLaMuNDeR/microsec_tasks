import asyncio
import json
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from temperature.models import Temperature
from datetime import datetime

class TemperatureConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        print ("Connected", event)
        # await - wait for the code to finish
        await self.send({
            "type": "websocket.accept"
        })

        self.channel_group = "1"
        await self.channel_layer.group_add(
            self.channel_group,
            self.channel_name
        )

    @database_sync_to_async
    def get_the_last_value(self):
        return Temperature.objects.last()

    @database_sync_to_async
    def upload_new_value(self, value):
        return Temperature.objects.create(value=value)

    async def websocket_receive(self, event):
        # When a message is received from the websocket
        front_text = event.get('text', None)
        if front_text:
            loaded_dict_data = json.loads(front_text)
            value = loaded_dict_data.get('value')
            print(value)
            await self.upload_new_value(value)
            last_value = await self.get_the_last_value()
            # last_value = json.dumps((last_value.value, str(last_value.timestamp)))
            new_message = {
                "type": "websocket.send",
                "text": last_value
            }

            update_value = {
                'value': last_value.value,
                'timestamp': str(last_value.timestamp),
            }

            await self.channel_layer.group_send(
                self.channel_group,
                {
                    "type": "value_message",
                    "text": json.dumps(update_value)
                }
            )

    async def value_message(self, event):
        await self.send({
            "type": "websocket.send",
            "text": event["text"]
        })

    async def websocket_disconnect(self, event):
        # when the socket disconnects
        print("disconnected", event)