import json
from pathlib import Path
from typing import Dict, Optional
from genson import SchemaBuilder

def write_json_to_file(content: Dict, file_path: str) -> bool:
    """write JSON to a given file path

    Args:
        content (Dict): The content to be written as JSON to a file
        file_path (str): The file path in which the content should be written to

    Returns:
        is_success (bool): True if written, else False.
    """
    is_success = False
    if content:
        with open(Path(file_path), "w") as f_obj:
            json.dump(content, f_obj)
            is_success = True
    return is_success

def read_json_content(json_path: str) -> Optional[Dict]:
    """Read the JSON file in the given json_file path

    Args:
        json_path (str): The file path where the json file resides

    Returns:
        Optional[Dict]: The JSON content as a Dictionary
    """
    msg = None
    json_content = None
    try:
        with open(json_path, "r") as file_obj:
            json_content = json.loads(file_obj.read())
        if json_content:
            msg = json_content.get("message")
    except OSError:
        print("Unable to open json file")
    return msg

def generate_schema_builder(json_content: Dict) -> Dict:
    """Generate the schema for the JSON

    Args:
        json_content (Dict): The JSON Content as a Dictionary

    Returns:
        SchemaBuilder: Return the schema
    """
    schema_dict = {}
    try:
        if json_content:
            builder = SchemaBuilder()
            builder.add_schema(
                {
                    "type": "object",
                    "tag": "",
                    "required": [False],
                    "description": "",
                    "properties": {
                        "ENUM": {"type": "array", "items": {"type": "string", "required": [False]}},
                        "ARRAY": {
                            "type": "array",
                            "items": {"type": "object", "required": [False]},
                        },
                        "string": {"type": "string", "required": [False]},
                        "string": {"type": "integer", "required": [False]},
                    },
                        "string": {"type": "string", "required": [False]},
                        "integer": {"type": "integer", "required": [False]},

                }
            )
            builder.add_object(json_content)
            schema_dict = builder.to_schema()
            schema_dict.pop("$schema")
    except Exception as e:
        print(f"Issue generating Schema {e}")
    return schema_dict


if __name__ == "__main__":
    msg_1 = read_json_content("data/data_1.json")
    if msg_1:
        schema_content = generate_schema_builder(msg_1)
        write_json_to_file(schema_content, 'schema/schema_1.json')
    msg_2 = read_json_content("data/data_2.json")
    if msg_2:
        schema_content = generate_schema_builder(msg_2)
        write_json_to_file(schema_content, 'schema/schema_2.json')
