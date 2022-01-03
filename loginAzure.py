from azure.identity import DefaultAzureCredential
from azure.keyvault.keys import KeyClient

url_path = "https://my-strong-vault.vault.azure.net/"

credential = DefaultAzureCredential()

key = KeyClient(vault_url=url_path, credential=credential)

rsa_key = key.create_rsa_key("my-second-key", size=2048)
print(rsa_key.name)
print(rsa_key.key_type)
print(rsa_key.id)