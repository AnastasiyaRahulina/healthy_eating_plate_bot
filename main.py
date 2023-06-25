import telebot
import random
import requests
from bs4 import BeautifulSoup
from telebot import types
import os

token = os.getenv("TOKEN")
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Hello' or message.text == 'hello':
        bot.send_message(message.from_user.id,
                         text=f'Hello, I am @HealthyEatingPlate,'
                              f' I can show you, how to eat healthy without counting calories.'
                              f' \nHarvard’s Healthy Eating Plate is the answer!'
                              f' \nHere is the main ideas about: \n{intro_text}')
        bot.send_message(message.from_user.id, 'Would you like to begin? \nWrite yes/no')
        bot.register_next_step_handler(message, intro)
    elif message.text == '/help':
        bot.send_message(message.from_user.id, 'Write Hello')
    else:
        bot.send_message(message.from_user.id, 'Write /help.')


def intro(message):
    if message.text == 'yes':
        bot.send_message(message.from_user.id, 'What is your name?')
        bot.register_next_step_handler(message, start)
    elif message.text == 'no':
        bot.send_message(message.from_user.id,
                         'I can send you a small printable copy of HealthyEatingPlate Guide.'
                         'You can hang it on your refrigerator to serve as a daily reminder '
                         'when planning and preparing your meals. Write yes/no')
        bot.register_next_step_handler(message, end)
    else:
        bot.send_message(message.from_user.id, 'Nice try! You should type yes or no')
        bot.register_next_step_handler(message, intro)


def end(message):
    if message.text == 'yes':
        bot.send_message(message.from_user.id,
                         'https://cdn1.sph.harvard.edu/wp-content/uploads/sites/30/2012/09/HEPJan2015.jpg')
        bot.send_message(message.from_user.id,
                         text='Copyright © 2011, Harvard University. '
                              'For more information about The Healthy Eating Plate, '
                              'please see The Nutrition Source, Department of Nutrition, '
                              'Harvard T.H. Chan School of Public Health, www.thenutritionsource.org, '
                              'and Harvard Health Publications, www.health.harvard.edu.')
    elif message.text == 'no':
        bot.send_message(message.from_user.id, 'Take care! Come back anytime 🫰🏻')
        bot.send_message(message.from_user.id,
                         text='Copyright © 2011, Harvard University. '
                              'For more information about The Healthy Eating Plate, '
                              'please see The Nutrition Source, Department of Nutrition, '
                              'Harvard T.H. Chan School of Public Health, www.thenutritionsource.org, '
                              'and Harvard Health Publications, www.health.harvard.edu.')


global user_name


def start(message):
    global user_name
    user_name = message.text
    bot.send_message(message.from_user.id,
                     f'Glad to meet you, {user_name}🤗. Shall we begin? '
                     f'\nChoose your favorite product and I will offer '
                     f'you a healthy and delicious recipe with it! \nWrite yes/no')
    bot.register_next_step_handler(message, get_plate)


def get_plate(message):
    if message.text == 'yes':
        keyboard = types.InlineKeyboardMarkup()
        key_veg = types.InlineKeyboardButton(text='💚Veggies💚', callback_data='veggies')
        keyboard.add(key_veg)
        key_fru = types.InlineKeyboardButton(text='❤️Fruits❤️', callback_data='fruits')
        keyboard.add(key_fru)
        key_grains = types.InlineKeyboardButton(text='🧡Cereals🧡', callback_data='grains')
        keyboard.add(key_grains)
        key_protein = types.InlineKeyboardButton(text='💙Proteins💙', callback_data='protein')
        keyboard.add(key_protein)
        bot.send_message(message.from_user.id, text=f'Choose, what you like!', reply_markup=keyboard)
    elif message.text == 'no':
        bot.send_message(message.from_user.id, text='If you want, I can send you a random recipe 😺. \nWrite yes/no')
        bot.register_next_step_handler(message, get_recipe)
    else:
        bot.send_message(message.from_user.id, 'Write yes or no')


def get_recipe(message):
    if message.text == 'yes':
        key_rec = listOfAll[random.randint(0, 25)]
        bot.send_message(message.from_user.id, text=rec_dict[key_rec][random.randint(0, len(key_rec))])
        keyboard = types.InlineKeyboardMarkup()
        key_try = types.InlineKeyboardButton(text='Try again', callback_data='try')
        keyboard.add(key_try)
        key_stop = types.InlineKeyboardButton(text='Stop', callback_data='stop')
        keyboard.add(key_stop)
        bot.send_message(message.from_user.id,
                         text=f'Do you like it {user_name}? You can try again until you find THE ONE you need 🫶',
                         reply_markup=keyboard)
    elif message.text == 'no':
        bot.send_message(message.from_user.id, text=f'Take care, {user_name}! Come back anytime 🫰🏻')
        bot.send_message(message.from_user.id,
                         text='Copyright © 2011, Harvard University. '
                              'For more information about The Healthy Eating Plate, '
                              'please see The Nutrition Source, Department of Nutrition, '
                              'Harvard T.H. Chan School of Public Health, www.thenutritionsource.org, '
                              'and Harvard Health Publications, www.health.harvard.edu.')
    else:
        bot.send_message(message.from_user.id, 'Write yes/no')


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'veggies':
        keyboard = types.InlineKeyboardMarkup()
        key_tom = types.InlineKeyboardButton(text='Tomato🍅', callback_data='tomato')
        keyboard.add(key_tom)
        key_cuc = types.InlineKeyboardButton(text='Cucumber🥒', callback_data='cucumber')
        keyboard.add(key_cuc)
        key_zuc = types.InlineKeyboardButton(text='Zucchini', callback_data='zucchini')
        keyboard.add(key_zuc)
        key_aub = types.InlineKeyboardButton(text='Egg_plant🍆', callback_data='egg_plant')
        keyboard.add(key_aub)
        key_pum = types.InlineKeyboardButton(text='Pumpkin🎃', callback_data='pumpkin')
        keyboard.add(key_pum)
        key_cab = types.InlineKeyboardButton(text='Cabbage🥬', callback_data='cabbage')
        keyboard.add(key_cab)
        key_bro = types.InlineKeyboardButton(text='Broccoli🥦', callback_data='broccoli')
        keyboard.add(key_bro)
        key_car = types.InlineKeyboardButton(text='Carrot🥕', callback_data='carrot')
        keyboard.add(key_car)
        bot.send_message(call.message.chat.id, text='Vegetables is always a GOOD idea! What\'s your choice?',
                         reply_markup=keyboard)
    elif call.data == 'fruits':
        keyboard = types.InlineKeyboardMarkup()
        key_apl = types.InlineKeyboardButton(text='Apple🍎', callback_data='apple')
        keyboard.add(key_apl)
        key_ora = types.InlineKeyboardButton(text='Orange🍊', callback_data='orange')
        keyboard.add(key_ora)
        key_kiw = types.InlineKeyboardButton(text='Kiwi🥝', callback_data='kiwi')
        keyboard.add(key_kiw)
        key_che = types.InlineKeyboardButton(text='Cherry🍒', callback_data='cherry')
        keyboard.add(key_che)
        key_pea = types.InlineKeyboardButton(text='Peach🍑', callback_data='peach')
        keyboard.add(key_pea)
        key_ban = types.InlineKeyboardButton(text='Banana🍌', callback_data='banana')
        keyboard.add(key_ban)
        key_avo = types.InlineKeyboardButton(text='Avocado🥑', callback_data='avocado')
        keyboard.add(key_avo)
        key_man = types.InlineKeyboardButton(text='Mango🥭', callback_data='mango')
        keyboard.add(key_man)
        bot.send_message(call.message.chat.id, text='Sweet and juicy, those fruit recipes are GREAT!',
                         reply_markup=keyboard)
    elif call.data == 'grains':
        keyboard = types.InlineKeyboardMarkup()
        key_oat = types.InlineKeyboardButton(text='Oat🍲', callback_data='oat')
        keyboard.add(key_oat)
        key_corn = types.InlineKeyboardButton(text='Corn🌽', callback_data='corn')
        keyboard.add(key_corn)
        key_pas = types.InlineKeyboardButton(text='Pasta🍝', callback_data='pasta')
        keyboard.add(key_pas)
        key_buck = types.InlineKeyboardButton(text='Buckwheat🥣', callback_data='buck')
        keyboard.add(key_buck)
        key_rice = types.InlineKeyboardButton(text='Rice🍚', callback_data='rice')
        keyboard.add(key_rice)
        bot.send_message(call.message.chat.id, text='Grains is PURE energy! What\'s your favorite?',
                         reply_markup=keyboard)
    elif call.data == 'protein':
        keyboard = types.InlineKeyboardMarkup()
        key_egg = types.InlineKeyboardButton(text='Egg 🥚', callback_data='egg')
        keyboard.add(key_egg)
        key_bean = types.InlineKeyboardButton(text='Beans 🫘', callback_data='beans')
        keyboard.add(key_bean)
        key_meat = types.InlineKeyboardButton(text='Meat and Poultry🍗🥩', callback_data='meat')
        keyboard.add(key_meat)
        key_fish = types.InlineKeyboardButton(text='Fish and Seafood🦪🐟', callback_data='fish')
        keyboard.add(key_fish)
        key_nut = types.InlineKeyboardButton(text='Nuts🥜', callback_data='nut')
        keyboard.add(key_nut)
        bot.send_message(call.message.chat.id,
                         text='Protein is the POWER! Here is some advice: '
                              'Choose fish, poultry, beans, and nuts; '
                              'limit red meat and cheese; '
                              'avoid bacon, cold cuts, and other processed meats',
                         reply_markup=keyboard)
    elif call.data in listOfVeggies:
        bot.send_message(call.message.chat.id,
                         text=rec_dict[call.data][random.randint(0, len(rec_dict[call.data]) - 1)])
        bot.send_message(call.message.chat.id,
                         f'Do you like it {user_name}? You can try again until you find THE ONE you need 🫶')
    elif call.data in listOfFruits:
        bot.send_message(call.message.chat.id,
                         text=rec_dict[call.data][random.randint(0, len(rec_dict[call.data]) - 1)])
        bot.send_message(call.message.chat.id,
                         f'Do you like it {user_name}? You can try again until you find THE ONE you need 🫶')
    elif call.data in listOfProteins:
        bot.send_message(call.message.chat.id,
                         text=rec_dict[call.data][random.randint(0, len(rec_dict[call.data]) - 1)])
        bot.send_message(call.message.chat.id,
                         f'Do you like it {user_name}? You can try again until you find THE ONE you need 🫶')
    elif call.data in listOfGrains:
        bot.send_message(call.message.chat.id,
                         text=rec_dict[call.data][random.randint(0, len(rec_dict[call.data]) - 1)])
        bot.send_message(call.message.chat.id,
                         f'Do you like it {user_name}? You can try again until you find THE ONE you need 🫶')
    elif call.data == 'try':
        key_rec = listOfAll[random.randint(0, 25)]
        bot.send_message(call.message.chat.id, text=rec_dict[key_rec][random.randint(0, len(key_rec))])
        keyboard = types.InlineKeyboardMarkup()
        key_try = types.InlineKeyboardButton(text='Try again', callback_data='try')
        keyboard.add(key_try)
        key_stop = types.InlineKeyboardButton(text='Stop', callback_data='stop')
        keyboard.add(key_stop)
        bot.send_message(call.message.chat.id,
                         text=f'Do you like it {user_name}? You can try again until you find THE ONE you need 🫶',
                         reply_markup=keyboard)
    elif call.data == 'stop':
        bot.send_message(call.message.chat.id, 'Take care! Come back anytime 🫰🏻')
        bot.send_message(call.message.chat.id,
                         text='Copyright © 2011, Harvard University. '
                              'For more information about The Healthy Eating Plate, '
                              'please see The Nutrition Source, Department of Nutrition, '
                              'Harvard T.H. Chan School of Public Health, www.thenutritionsource.org, '
                              'and Harvard Health Publications, www.health.harvard.edu.')


intro_text = '''🌿 Make most of your meal vegetables and fruits – ½ of your plate.
🌈 Aim for color and variety, and remember that potatoes don’t count! 
🌾 Go for whole grains – ¼ of your plate.
🍤 Protein power – ¼ of your plate. 
🦚 Choose healthy vegetable oils.
💧 Don’t forget to drink enough water! \nAll recipes were taken from © 2023 EatingWell.com'''

listOfVeggies = ['tomato', 'cucumber', 'zucchini', 'egg_plant', 'pumpkin', 'cabbage', 'broccoli', 'carrot']
listOfFruits = ['apple', 'orange', 'kiwi', 'cherry', 'peach', 'banana', 'avocado', 'mango']
listOfGrains = ['oat', 'corn', 'pasta', 'buck', 'rice']
listOfProteins = ['egg', 'beans', 'meat', 'fish', 'nut']
listOfAll = listOfVeggies + listOfFruits + listOfGrains + listOfProteins

rec_dict = dict.fromkeys(listOfVeggies, [])
rec_dict.update(dict.fromkeys(listOfFruits, []))
rec_dict.update(dict.fromkeys(listOfGrains, []))
rec_dict.update(dict.fromkeys(listOfProteins, []))

url = 'https://www.eatingwell.com/recipes/17943/ingredients/grains/cornmeal/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
tom_rec = []
for link in soup.find_all('a', class_='card__titleLink manual-link-behavior elementFont__titleLink margin-8-bottom'):
    rec = link.get('href')
    rec_dict['corn'] = rec_dict.get('corn', []) + [rec]

url = 'https://www.eatingwell.com/recipes/19226/ingredients/grains/oats/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
tom_rec = []
for link in soup.find_all('a', class_='card__titleLink manual-link-behavior elementFont__titleLink margin-8-bottom'):
    rec = link.get('href')
    rec_dict['oat'] = rec_dict.get('oat', []) + [rec]

url = 'https://www.eatingwell.com/recipes/18250/ingredients/pasta-noodle/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
tom_rec = []
for link in soup.find_all('a', class_='card__titleLink manual-link-behavior elementFont__titleLink margin-8-bottom'):
    rec = link.get('href')
    rec_dict['pasta'] = rec_dict.get('pasta', []) + [rec]

url = 'https://www.eatingwell.com/search/?q=buckwheat'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
tom_rec = []
for link in soup.find_all('a', class_='searchResult__titleLink elementFont__subheadLink'):
    rec = link.get('href')
    rec_dict['buck'] = rec_dict.get('buck', []) + [rec]

url = 'https://www.eatingwell.com/recipes/19227/ingredients/grains/rice/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
tom_rec = []
for link in soup.find_all('a', class_='card__titleLink manual-link-behavior elementFont__titleLink margin-8-bottom'):
    rec = link.get('href')
    rec_dict['rice'] = rec_dict.get('rice', []) + [rec]

url = 'https://www.eatingwell.com/recipes/18238/ingredients/eggs/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
tom_rec = []
for link in soup.find_all('a', class_='card__titleLink manual-link-behavior elementFont__titleLink margin-8-bottom'):
    rec = link.get('href')
    rec_dict['egg'] = rec_dict.get('egg', []) + [rec]

url = 'https://www.eatingwell.com/recipes/18236/ingredients/beans/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
tom_rec = []
for link in soup.find_all('a', class_='card__titleLink manual-link-behavior elementFont__titleLink margin-8-bottom'):
    rec = link.get('href')
    rec_dict['beans'] = rec_dict.get('beans', []) + [rec]

url = 'https://www.eatingwell.com/recipes/22777/ingredients/meat-poultry/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
tom_rec = []
for link in soup.find_all('a', class_='card__titleLink manual-link-behavior elementFont__titleLink margin-8-bottom'):
    rec = link.get('href')
    rec_dict['meat'] = rec_dict.get('meat', []) + [rec]

url = 'https://www.eatingwell.com/recipes/18243/ingredients/fish-seafood/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
tom_rec = []
for link in soup.find_all('a', class_='card__titleLink manual-link-behavior elementFont__titleLink margin-8-bottom'):
    rec = link.get('href')
    rec_dict['fish'] = rec_dict.get('fish', []) + [rec]

url = 'https://www.eatingwell.com/recipes/18248/ingredients/nuts-seeds/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
tom_rec = []
for link in soup.find_all('a', class_='card__titleLink manual-link-behavior elementFont__titleLink margin-8-bottom'):
    rec = link.get('href')
    rec_dict['nut'] = rec_dict.get('nut', []) + [rec]

url = 'https://www.eatingwell.com/recipes/19320/ingredients/vegetables/tomato/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
tom_rec = []
for link in soup.find_all('a', class_='card__titleLink manual-link-behavior elementFont__titleLink margin-8-bottom'):
    rec = link.get('href')
    rec_dict['tomato'] = rec_dict.get('tomato', []) + [rec]

url = 'https://www.eatingwell.com/recipes/19299/ingredients/vegetables/cucumbers/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
for link in soup.find_all('a', class_='card__titleLink manual-link-behavior elementFont__titleLink margin-8-bottom'):
    rec = link.get('href')
    rec_dict['cucumber'] = rec_dict.get('cucumber', []) + [rec]

url = 'https://www.eatingwell.com/recipes/19295/ingredients/vegetables/carrots/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
for link in soup.find_all('a', class_='card__titleLink manual-link-behavior elementFont__titleLink margin-8-bottom'):
    rec = link.get('href')
    rec_dict['carrot'] = rec_dict.get('carrot', []) + [rec]

url = 'https://www.eatingwell.com/recipes/19315/ingredients/vegetables/pumpkin/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
for link in soup.find_all('a', class_='card__titleLink manual-link-behavior elementFont__titleLink margin-8-bottom'):
    rec = link.get('href')
    rec_dict['pumpkin'] = rec_dict.get('pumpkin', []) + [rec]

url = 'https://www.eatingwell.com/recipes/19301/ingredients/vegetables/eggplant/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
for link in soup.find_all('a', class_='card__titleLink manual-link-behavior elementFont__titleLink margin-8-bottom'):
    rec = link.get('href')
    rec_dict['egg_plant'] = rec_dict.get('egg_plant', []) + [rec]

url = 'https://www.eatingwell.com/recipes/19324/ingredients/vegetables/squash/zucchini/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
cab_rec = []
for link in soup.find_all('a', class_='card__titleLink manual-link-behavior elementFont__titleLink margin-8-bottom'):
    rec = link.get('href')
    rec_dict['zucchini'] = rec_dict.get('zucchini', []) + [rec]

url = 'https://www.eatingwell.com/recipes/19294/ingredients/vegetables/cabbage/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
cab_rec = []
for link in soup.find_all('a', class_='card__titleLink manual-link-behavior elementFont__titleLink margin-8-bottom'):
    rec = link.get('href')
    rec_dict['cabbage'] = rec_dict.get('cabbage', []) + [rec]

url = 'https://www.eatingwell.com/recipes/19292/ingredients/vegetables/broccoli/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
for link in soup.find_all('a', class_='card__titleLink manual-link-behavior elementFont__titleLink margin-8-bottom'):
    rec = link.get('href')
    rec_dict['broccoli'] = rec_dict.get('broccoli', []) + [rec]

url = 'https://www.eatingwell.com/recipes/19190/ingredients/fruit/apple/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
for link in soup.find_all('a', class_='card__titleLink manual-link-behavior elementFont__titleLink margin-8-bottom'):
    rec = link.get('href')
    rec_dict['apple'] = rec_dict.get('apple', []) + [rec]

url = 'https://www.eatingwell.com/recipes/19211/ingredients/fruit/citrus/orange/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
for link in soup.find_all('a', class_='card__titleLink manual-link-behavior elementFont__titleLink margin-8-bottom'):
    rec = link.get('href')
    rec_dict['orange'] = rec_dict.get('orange', []) + [rec]

url = 'https://www.eatingwell.com/recipes/19206/ingredients/fruit/kiwi/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
for link in soup.find_all('a', class_='card__titleLink manual-link-behavior elementFont__titleLink margin-8-bottom'):
    rec = link.get('href')
    rec_dict['kiwi'] = rec_dict.get('kiwi', []) + [rec]

url = 'https://www.eatingwell.com/recipes/19197/ingredients/fruit/cherry/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
for link in soup.find_all('a', class_='card__titleLink manual-link-behavior elementFont__titleLink margin-8-bottom'):
    rec = link.get('href')
    rec_dict['cherry'] = rec_dict.get('cherry', []) + [rec]

url = 'https://www.eatingwell.com/recipes/19213/ingredients/fruit/peach/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
for link in soup.find_all('a', class_='card__titleLink manual-link-behavior elementFont__titleLink margin-8-bottom'):
    rec = link.get('href')
    rec_dict['peach'] = rec_dict.get('peach', []) + [rec]

url = 'https://www.eatingwell.com/recipes/19193/ingredients/fruit/banana/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
for link in soup.find_all('a', class_='card__titleLink manual-link-behavior elementFont__titleLink margin-8-bottom'):
    rec = link.get('href')
    rec_dict['banana'] = rec_dict.get('banana', []) + [rec]

url = 'https://www.eatingwell.com/gallery/7651196/avocado-and-egg-recipes/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
for link in soup.find_all('a', class_='glide-slide-cta-button elementButton__standard elementButton__outlined'):
    rec = link.get('href')
    rec_dict['avocado'] = rec_dict.get('avocado', []) + [rec]

url = 'https://www.eatingwell.com/recipes/19209/ingredients/fruit/mango/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
for link in soup.find_all('a', class_='card__titleLink manual-link-behavior elementFont__titleLink margin-8-bottom'):
    rec = link.get('href')
    rec_dict['mango'] = rec_dict.get('mango', []) + [rec]


bot.polling(none_stop=True)
