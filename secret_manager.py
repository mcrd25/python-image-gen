import os
import json

class SecretManager:
    def __init__(self):
        self.secrets = {}

    def get_secrets(self, service_name):
        if service_name in self.secrets:
            return self.secrets[service_name]
        else:
            secrets_file = f"{service_name}_secrets.json"
            if os.path.exists(secrets_file):
                with open(secrets_file, "r") as f:
                    secrets = json.load(f)
                    self.secrets[service_name] = secrets
                    return secrets
            else:
                raise Exception(f"Secrets for {service_name} not found")

    def get_services(self):
        return list(self.secrets.keys())
