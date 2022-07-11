from jsonschema import validate, exceptions


def validate_json(json_data, schema):
    try:
        validate(instance=json_data, schema=schema)
    except exceptions.ValidationError:
        return False
    return True
