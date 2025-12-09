import argparse
import requests

def parse_arguments():
    parser = argparse.ArgumentParser(description="Do you like CAPITALIZED strings??? Here's a tool to capitalize them! Just put a string and it will be capitalized")
    parser.add_argument('N', type=int, help='how many strings??')
    return parser.parse_args()


with open('key.txt') as f:
    PASTEBIN_API_KEY = f.read()

def capitalize(string: str):
    return input_string.upper()

def post_on_pastebin(string: str):
    data = {
        'api_option': 'paste',
        'api_dev_key': PASTEBIN_API_KEY,
        'api_paste_code': string,
    }
    r = requests.post('https://pastebin.com/api/api_post.php', data=data)
    return r.text

if __name__ == "__main__":
    args = parse_arguments()
    capitalized = []
    for _ in range(args.N):
        print("Please give me a string!!!!")
        input_string = input()
        capitalized_string = capitalize(input_string)
        print("Here is your CAPITALIZED string!!!")
        capitalized.append(capitalized_string)
        print(capitalized_string)
    t = post_on_pastebin('\n'.join(capitalized))
    print("Here's your link, enjoy ur day!!!")
    print(t)

