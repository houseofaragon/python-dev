from dataclasses import dataclass
import requests
import json

hue_ip_address = "192.168.1.5"
hue_username = "KB75bFWzLxj101-8ZVeqrrAvs2utaAjEV43AkLmG"

@dataclass
class HueBridgeData:
    id: str
    internalipaddress: str
    port: int
    
    """
     {"1": {"state": StateData,}}
    
    """
@dataclass
class HueLightStateData:
    pass

@dataclass
class HueLightData:
    state: HueLightStateData
    

""" 
    Hue Bridge Data
    HueBridgeData {
        id: string
        internalipaddress: string
        port: number
    }
"""
def get_hue_base_url():
    return f"http://{hue_ip_address}/api/{hue_username}"

def get_hue_bridge_data() -> HueBridgeData:
    request = requests.get('https://discovery.meethue.com')
    status_code = request.status_code
    
    if (status_code != 200):
        raise RuntimeError(f"An error getting ip occurred. Status code={status_code}")
    
    
    raw_data = request.json()[0]
    return HueBridgeData(**raw_data)

def get_hue_lights_data():
    url = f"{get_hue_base_url()}/lights"
    request = requests.get(url)
    status_code = request.status_code
    
    if (status_code != 200):
        raise RuntimeError(f"An error getting ip occurred. Status code={status_code}")
    
    return request.json()
    
def update_light_state(index, data):
    url = f"{get_hue_base_url()}/lights/{index}/state"
    
    request = requests.put(url, data=json.dumps(data))
    print(request)
    
if __name__ == "__main__":
    from pprint import pprint
    # pprint(get_hue_lights_data())
    # keys = get_hue_lights_data()['1'].keys()
    # pprint(keys)
    update_light_state(1, { "on": False })