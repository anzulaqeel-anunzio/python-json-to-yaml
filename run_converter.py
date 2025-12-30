# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import argparse
import sys
import os

# Add current dir to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from converter.core import JsonToYamlConverter

def main():
    parser = argparse.ArgumentParser(description="JSON to YAML Converter")
    parser.add_argument("file", help="Input JSON file")
    parser.add_argument("--output", "-o", help="Output YAML file")

    args = parser.parse_args()

    if not os.path.exists(args.file):
        print(f"Error: File '{args.file}' not found.")
        sys.exit(1)

    try:
        with open(args.file, 'r', encoding='utf-8') as f:
            json_content = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    yaml_output = JsonToYamlConverter.convert(json_content)

    if yaml_output.startswith("Error"):
        print(yaml_output)
        sys.exit(1)

    if args.output:
        try:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(yaml_output)
            print(f"Converted file saved to {args.output}")
        except Exception as e:
            print(f"Error writing output: {e}")
            sys.exit(1)
    else:
        print(yaml_output)

if __name__ == "__main__":
    main()

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
