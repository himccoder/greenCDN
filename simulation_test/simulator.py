import requests
from requests.auth import HTTPBasicAuth

def set_weight(server, weight):

    server_name = f"s{server}"

    url = f"http://localhost:5555/v3/services/haproxy/configuration/backends/webservers/servers/{server_name}"
    headers = {
        "Content-Type": "application/json"
    } 
    data = {
        "name": server_name,
        "address": "host.docker.internal:7001",
        "weight": weight
    }

    response = requests.put(
        url,
        json=data,
        headers=headers,
        auth=HTTPBasicAuth('admin', 'password')
    )

    print(response.status_code)
    print(response.text)
    
def calculate_weight(carbon_intensity, latency = 0):
    return 100 / carbon_intensity

def run_simulation():
    print("beginning simulation")

    L1 = [5, 10, 20]
    L2 = [11, 12, 13]
    L3 = [15, 10, 1]

    for i in range(3):
        set_weight(1, calculate_weight(L1[i]))
        set_weight(2, calculate_weight(L2[i]))
        set_weight(3, calculate_weight(L3[i]))

        response = requests.get("http://localhost")
        if response.status_code == 200:
            data = response.json()
            print(f"Request {i + 1} was handled by server {data.id}")
        else:
            print(f"Error handling request number {i + 1}: {response.status_code} - {response.text}")

def simulation_test():
    print("simulation test")

    print("testing")
    url = "http://localhost:5555/v3/info"
    response = requests.get(url, auth=HTTPBasicAuth('admin', 'password'))
    print(response.status_code)
    print(response.text)

    print("test complete")

if __name__ == "__main__":
    simulation_test()
    # run_simulation()