import json

def load_json():

    with open('/home/ubuntu/pCloudDrive/FLM JSON PROCESSED V2 BACKUP/FLM_MASTER.JSON') as json_file:
        obj = json_file.read()
        obj2 = json.loads(obj)
        return obj2