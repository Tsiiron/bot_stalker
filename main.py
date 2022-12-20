import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from config import main_token
import random


def send_message(id, text):
    vk_session.method('messages.send', {'peer_id': id, 'message': text, 'random_id': 0})


def send_photo(id, photo):
    vk_session.method("messages.send", {'peer_id': id, "attachment": photo, "random_id": 0})


def send_video(id, video):
    vk_session.method("messages.send", {'peer_id': id, "attachment": video, "random_id": 0})


vk_session = vk_api.VkApi(token=main_token)
longpoll = VkBotLongPoll(vk_session, 217852491)
users_pidors = [113362624, 490357001, 307938264]

fuck_messages = ['Арсений Чернов, пошёл нахуй!', 'Иди нахуй', 'Ливни нахуй', 'Зачилься', 'Съебался в страхе']
fuck_pictures = ['photo-217852491_457239017', 'photo-217852491_457239018', 'photo-217852491_457239019',
                 'photo-217852491_457239020', 'photo-217852491_457239021', 'photo-217852491_457239022',
                 'photo-217852491_457239023', 'photo-217852491_457239024', 'photo-217852491_457239025',
                 'photo-217852491_457239026']
fuck_videos = ['video-217852491_456239017']

types = [[fuck_messages, "message"], [fuck_pictures, "picture"], [fuck_videos, "video"]]

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        print("text", event.message.text)
        id = event.message.peer_id
        messager_id = event.message.from_id
        print(id, messager_id)
        if (messager_id in users_pidors):
            type = random.choice(types)
            fuck = type[0]
            type1 = type[1]
            if (type1 == "message"):
                fuck1 = random.choice(fuck)
                send_message(id, fuck1)
            elif (type1 == "picture"):
                photo = str(random.choice(fuck))
                send_photo(id, photo)
            elif (type1 == "video"):
                video = str(random.choice(fuck))
                send_video(id, video)
