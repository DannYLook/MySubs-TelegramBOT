import requests

TOKEN = 'токен телеграм бот'
id_chat = 'чат айди телеграмы'
key_YouTube = 'ютюб ключ'
id_channel = 'айди канал'

def read_file():
    with open('sab.txt', 'r') as f_obj:
        row = f_obj.read()
        return row


def write_file(sabs):
    with open('sab.txt', 'w') as f_obj:
        f_obj.write(sabs)


def main():
    url = 'https://www.googleapis.com/youtube/v3/channels?part=statistics&id='+id_channel+'&key=' + key_YouTube
    response = requests.get(url)
    responseJson = response.json()
    subscriberCount =responseJson['items'][0]['statistics']['subscriberCount']

    row = subscriberCount
    now = read_file()
    if row != now:
        message = 'Сейчас у тебя ' + row + ' подписчиков'
        requests.get('https://api.telegram.org/bot{}/sendMessage'.format(TOKEN),params=dict(chat_id=id_chat, text=message))

        write_file(row)

if __name__ == "__main__":
    main()