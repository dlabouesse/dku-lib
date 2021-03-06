import dataiku
import requests
import pandas as pd
from .dataiku_secrets import get_credentials

def get_customers(with_labels):
    '''
    Return customers from third part CRM
    
    Parameters:
        with_labels (bool): whether or not retrieving customers where the ground truth is known.
    
    Returns:
        pd.DataFrame: all customers matching the search criteria.
    '''

    headers = {'Authorization': 'Basic ' + get_credentials('customers')}
    payload = {} 
    url = dataiku.get_custom_variables()["customers_url"] + "/schema"

    response = requests.request("GET", url, headers=headers, data = payload)
    columns = []
    for column in response.json()["columns"]:
        columns.append(column["name"])

    url = dataiku.get_custom_variables()["customers_url"] + "/data/?format=json"
    
    if (with_labels):
        url+="&filter=Churn!=\"\""
    else:
        url+="&filter=Churn==\"\""
        
    response = requests.request("GET", url, headers=headers, data = payload)
    return pd.DataFrame(response.json(), columns=columns)
