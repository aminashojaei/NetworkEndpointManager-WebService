import requests
from config.settings import HOST, PORT 


def get_agent_status(agent_url):
    response = requests.get(f'http://{agent_url}/status')
    if response.status_code == 200:
        print("Agent Info:", response.json())
    else:
        print("Failed to get agent info.")

def restart_agent(agent_url):
    response = requests.post(f'http://{agent_url}/restart')
    if response.status_code == 200:
        print("Agent restarting...")
    else:
        print("Failed to restart agent.")
        
def get_agent_processes(agent_url):
    response = requests.get(f'http://{agent_url}/processes')
    if response.status_code == 200:
        print("Agent Info:", response.json())
    else:
        print("Failed to restart agent.")

agent_url = str(HOST) +":"+ str(PORT)

get_agent_status(agent_url)
get_agent_processes(agent_url)
# restart_agent(agent_url)
