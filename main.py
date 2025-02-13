import requests # pip install requests
import yaml # pip install PyYAML
import logging as logger
import time
import os # pip install os
from urllib.parse import urlparse

def grab_domain(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    return domain

def check_availability(pos, num_requests=100):
    success_count = 0
    up = True
    description = pos["name"]
    method = pos.get("method", None)
    url = pos["url"]
    headers = pos.get("headers", {})
    headers["x-description"] = description
    body = pos.get("body", None)
    latency_cap = 0.5
    if method == "GET" or method == None:
        for x in range(num_requests):
            try:
                response = requests.get(url, headers = headers)
                latency = response.elapsed.total_seconds()
                if response.status_code == 200 and up == (latency < latency_cap) :
                    success_count += 1 # Add to success count for every successful connection
            except requests.exceptions.RequestException: # Throw exception for failed 
                pass  # Ignore connection errors
    elif method == "POST":
        for x in range(num_requests):
            try:
                response = requests.post(url, headers = headers, json = body)
                latency = response.elapsed.total_seconds()
                if response.status_code == 200 and up == (latency < latency_cap):
                    success_count += 1 # Add to success count for every successful connection
            except requests.exceptions.RequestException: # Throw exception for failed 
                pass  # Ignore connection errors
    availability = (success_count / num_requests) * 100
    return availability
    

def parse_yaml(file_path):
    try:
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
            return data
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
        return None
    except yaml.YAMLError as e:
         print(f"Error parsing YAML: {e}")
         return None
    

def find_key(d, target_key):
    for key, value in d.items():
        if key == target_key:
            return value
        elif isinstance(value, dict):
            result = find_key(value, target_key)
            if result:
                return result
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    result = find_key(item, target_key)
                    if result:
                        return result
    return None

def string_with_percent(num):
    return "{}%".format(num)


def domain_matches(url, domain):
    parsed_url = urlparse(url)
    return parsed_url.netloc == domain

def get_valid_file_path():
    while True:
        file_path = input("Please enter a valid file path: ").strip()
        if os.path.exists(file_path) and os.path.isfile(file_path):  # Check if file exists
            print(f"The file '{file_path}' exists.")
            return file_path  # Return the valid file path
        else:
            print(f"'{file_path}' is not a valid file path. Please try again.")

def get_valid_yaml_file():
    while True:
        file_path = input("Please enter a valid YAML file path: ").strip()
        if not os.path.exists(file_path):
            print(f"Error: The file '{file_path}' does not exist. Please try again.")
            continue
        if not file_path.endswith(('.yml', '.yaml')):
            print(f"Error: The file '{file_path}' is not a YAML file. Please try again.")
            continue
        print(f"The file '{file_path}' exists and is a valid YAML file.")
        return file_path

# Add up the number of of availability percentages divided by the number each domain shows up
def main(): 
        file_name = get_valid_yaml_file()
        parsed_file = parse_yaml(file_name)
        domain_list = {}
        while True:
            domain_list = []
            for pos in parsed_file:
                url = find_key(pos, "url")
                domain = grab_domain(url) #Check if the url in the parsed_file is the domain in the domain_list
                domain_present = any(item for item in domain_list if domain in item["domain"])
                if  domain_present is False:
                    new_availability = check_availability(pos)
                    num_of_requests = 1
                    new_base_url = {"domain": domain, 
                                    "total_availability": new_availability,
                                    "number_of_requests": num_of_requests}
                    domain_list.append(new_base_url)    
                else:
                    new_request = next((item for item in domain_list if item["domain"] == domain), None)
                    new_availability = new_request["total_availability"] + check_availability(pos)
                    domain_list[domain_list.index(new_request)]["total_availability"] = new_availability
                    new_num_requests = new_request["number_of_requests"] + + 1
                    domain_list[domain_list.index(new_request)]["number_of_requests"] = new_num_requests
            logger.basicConfig(level=logger.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
            for pos in domain_list:
                domain_name = pos["domain"]
                overall = str(pos["total_availability"]/ pos["number_of_requests"])
                overall_availability = string_with_percent(overall)
                statement = f" {domain_name} has {overall_availability} availability"
                logger.info(statement)
            time.sleep(15)




main()