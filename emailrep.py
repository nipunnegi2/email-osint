import requests


API_KEY = 'd71sr7mjnocpnegswirkjsek2ma2mwon5m3qahr2pj1kxw2t'
API_URL = 'https://emailrep.io/'

def get_email_reputation(email):
    headers = {
        'Key': API_KEY,
        'User-Agent': 'emailrep.io Python Client'
    }
    response = requests.get(f'{API_URL}{email}', headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return {'error': f'Failed to retrieve data: {response.status_code}'}

def print_email_reputation(data):
    if 'error' in data:
        print(data['error'])
    else:
        print("Email:", data.get('email', 'N/A'))
        print("Reputation:", data.get('reputation', 'N/A'))
        print("Suspicious:", data.get('suspicious', 'N/A'))
        print("References:", data.get('references', 'N/A'))
        print("Details:")
        for key, value in data.get('details', {}).items():
            print(f'  {key}: {value}')

if __name__ == '__main__':
    email = input("Enter the email address: ")
    reputation_data = get_email_reputation(email)
    print_email_reputation(reputation_data)
