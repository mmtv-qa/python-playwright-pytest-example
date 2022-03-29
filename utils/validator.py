import jsonschema


class Validator:

    @staticmethod
    def validate_credentials(creds: dict):
        schema = {
            "login": "string",
            "password": "string"
        }
        jsonschema.validate(creds, schema)
