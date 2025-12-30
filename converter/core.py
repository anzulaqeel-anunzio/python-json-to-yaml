# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import json

class JsonToYamlConverter:
    @staticmethod
    def _dump_yaml(data, indent_level=0):
        lines = []
        indent = "  " * indent_level
        
        if isinstance(data, dict):
            for key, value in data.items():
                if isinstance(value, (dict, list)):
                    lines.append(f"{indent}{key}:")
                    lines.extend(JsonToYamlConverter._dump_yaml(value, indent_level + 1))
                else:
                    val_str = JsonToYamlConverter._format_scalar(value)
                    lines.append(f"{indent}{key}: {val_str}")
                    
        elif isinstance(data, list):
            for item in data:
                if isinstance(item, (dict, list)):
                    # For complex items in list
                    # YAML list item starts with "- "
                    # If it's a dict, the first key goes on the same line usually, 
                    # but simple block style is:
                    # - 
                    #   key: val
                    lines.append(f"{indent}-")
                    # We need to indent the content of the list item
                    # The content of the item is at indent_level + 1
                    # But wait, standard yaml is:
                    # - key: val
                    #   key2: val
                    # My recursion above adds indent.
                    
                    # Hand-rolling YAML is subtle. Let's do block style consistently.
                    sub_lines = JsonToYamlConverter._dump_yaml(item, indent_level + 1)
                    # We can try to make it prettier by merging first line if it's a dict key?
                    # No, let's stick to safe block style.
                    lines.extend(sub_lines)
                else:
                    val_str = JsonToYamlConverter._format_scalar(item)
                    lines.append(f"{indent}- {val_str}")
                    
        return lines

    @staticmethod
    def _format_scalar(val):
        if val is None:
            return "null"
        if isinstance(val, bool):
            return "true" if val else "false"
        if isinstance(val, (int, float)):
            return str(val)
        if isinstance(val, str):
            # Check if needs quoting
            if ":" in val or "{" in val or "[" in val or "\n" in val or val.strip() != val or val == "":
                # Simple quoting
                escaped = val.replace('"', '\\"')
                return f'"{escaped}"'
            return val
        return str(val)

    @staticmethod
    def convert(json_content):
        try:
            data = json.loads(json_content)
            lines = JsonToYamlConverter._dump_yaml(data)
            return "\n".join(lines)
        except json.JSONDecodeError as e:
            return f"Error parsing JSON: {e}"

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
