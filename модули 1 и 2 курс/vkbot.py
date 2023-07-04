import random
import vk_api
from course import *
from wiki import *
from vk_api.longpoll import VkLongPoll, VkEventType

token="vk1.a._rAB0JB2QjHloMcHlOXUQic5r-wFX-VuKQeUEqxyqZMh-oGRzOHl08jd59rev2D6eiM785QHI6_49gspt43guUhB3VzE2PFWlALUwD5JNq1kQVKNnW_W1pY24JuydEY34bJ4dsd5u5193L0ymNoJmCjbrRWwjSgta9XhNCRw2Oh97yqehSL8_4oJH9MO_XTd6fP1A14c1MWOk5x8OrBGhQ"
vk_session = vk_api.VkApi(token = token)
vk=vk_session.get_api()
longpoll = VkLongPoll(vk_session)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        msg = event.text.lower()
        user_id = event.user_id
        random_id = random.randint(1, 10000000)
        if msg == "курс":
            responce = f'{getCourse("R01235")} рублей за 1 доллар, {getCourse("R01239")} за 1 евро, ' \
                       f'{getCourse("R01035")} за 1 фунт'

        elif msg.startswith("вики"):
            article = msg[4:]
            responce = get_wiki_article(article)
        else:
            responce = "Неизвестная команда"
        vk.messages.send(user_id=user_id, random_id=random_id, message = responce[:4096])