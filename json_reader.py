import json
import sys
from typing import TextIO

def main():
    data = read_json_input_stream(sys.stdin)
    print(data)

def read_json_input_stream(input_stream: TextIO):
    input_string = ""
    for row in input_stream:
        input_string += row
    return json.loads(input_string)

if __name__ == '__main__':
    main()

