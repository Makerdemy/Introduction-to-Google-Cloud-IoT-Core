import os
from google.cloud import iot_v1


def device_config(config):
    client = iot_v1.DeviceManagerClient()
    name = client.device_path(
        os.environ['PROJECT_ID'], os.environ['REGION'], os.environ['REGISTRY'],
        os.environ['DEVICE'])
    binary_data = bytes(config, 'utf-8')
    client.modify_cloud_to_device_config(name, binary_data)