import dataiku

def get_credentials(key):
        
    client = dataiku.api_client()
    auth_info = client.get_auth_info(with_secrets=True)

    api_secret = None
    for secret in auth_info["secrets"]:
        if secret["key"] == str(key):
            api_secret = str(secret["value"])

    if not api_secret:
        raise Exception("secret not found")
    
    return api_secret
