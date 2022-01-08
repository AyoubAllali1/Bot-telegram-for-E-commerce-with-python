import telebot
from telebot import types
from telebot.types import LabeledPrice, ShippingOption
API_KEY = 'your key'

provider_token = 'your provider token here'  # @BotFather -> Bot Settings -> Payments

# Data of items 
pizza = [
  {'title':'Pizza Chicken','description':'want to eat Pizza ?','photo':'https://tmbidigitalassetsazure.blob.core.windows.net/rms3-prod/attachments/37/1200x1200/Chicken-Pizza_exps30800_FM143298B03_11_8bC_RMS.jpg','price':[LabeledPrice('pizza', 600)]},
  {'title':'Pizza Fish','description':'want to eat Pizza ?','photo':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT5j8d1Ytw07h4FOWHzTEJT5yq5Jhgk7adJQw&usqp=CAU','price':[LabeledPrice('pizza', 700)]},
  {'title':'Pizza Marinara','description':'want to eat Pizza ?','photo':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ79wBpDIQGbRKdyMeGGjzGpv4dJGJtgtuLww&usqp=CAU','price':[LabeledPrice('pizza', 800)]},
  {'title':'Pizza Margherita','description':'want to eat Pizza ?','photo':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSsFdurA4BY4h-Y3DZS2EIHMRHmnXDCSGfBXg&usqp=CAU','price':[LabeledPrice('pizza', 900)]},
]

chicken = [
  {'title':'Chicken','description':'want to eat Chicken ?','photo':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTD2v2Mq0kh6AKcwmxUwdD6dyf9n3mDVH5D5A&usqp=CAU','price':[LabeledPrice('Chicken', 600)]},
  {'title':'chicken','description':'want to eat Chicken ?','photo':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRSEbpHtvcr6gxP9BMCOmFFLeEgeAPZf6XAUQ&usqp=CAU','price':[LabeledPrice('Chicken', 700)]},
  {'title':'chicken','description':'want to eat Chicken?','photo':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTStK_Bo_bWN2O3jVWD30PjNUbj5VfXF2-c8A&usqp=CAU','price':[LabeledPrice('Chicken', 800)]},
  {'title':'Chicken','description':'want to eat Chicken ?','photo':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQSLH_kBR8ualXJ3SgFJPNuaSmz_ED8O06IGQ&usqp=CAU','price':[LabeledPrice('Chicken', 900)]},
]

meat = [
  {'title':'Meat','description':'want to eat Meat ?','photo':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSC8Bj_q_pUH8-C63NgGmz_xTuTLwia5YzbBg&usqp=CAU','price':[LabeledPrice('Meat', 600)]},
  {'title':'Meat','description':'want to eat Meat ?','photo':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTun33FqcafVdfmLrju-Ru_T2WSu0mHZT0Zfw&usqp=CAU','price':[LabeledPrice('Meat', 700)]},
  {'title':'Meat','description':'want to eat Meat ?','photo':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSh55daxhDKdA5GdvwHkKEzyiBplv3O7UOQaA&usqp=CAU','price':[LabeledPrice('Meat', 800)]},
  {'title':'Meat','description':'want to eat Meat ?','photo':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSmMSxzyMJ4of1uyvXv4fGvIsdgJtERQzhSlw&usqp=CAU','price':[LabeledPrice('Meat', 900)]},
]

tacos = [
  {'title':'Tacos 1','description':'want to eat Tacos ?','photo':'https://img.cuisineaz.com/660x660/2019/04/17/i146583-tacos-poulet-curry.jpeg','price':[LabeledPrice('Tacos', 600)]},
  {'title':'Tacos 2','description':'want to eat Tacos ?','photo':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKmFDC4zsK3k9VBvx4gKyIZGECG4rQ5oLXRQ&usqp=CAU','price':[LabeledPrice('Tacos', 700)]},
  {'title':'Tacos 3','description':'want to eat Tacos ?','photo':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSE8MKGX9eAwSvHpY-Tqa27xU43zKM2GyiGYQ&usqp=CAU','price':[LabeledPrice('Tacos', 800)]},
  {'title':'Tacos 4','description':'want to eat Tacos ?','photo':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRw2tpE4jC21mnf914HXs4YqqXASsFJV9zCgg&usqp=CAU','price':[LabeledPrice('Tacos', 900)]},
]

shipping_options = [
    ShippingOption(id='Glovo', title='Glovo').add_price(LabeledPrice('Glovo', 1000)),
    ShippingOption(id='Teleporter', title='Our Teleporter').add_price(LabeledPrice('Our Teleporter', 300))]

bot = telebot.TeleBot(API_KEY)

markup = types.ReplyKeyboardMarkup(row_width=2)
itembtn1 = types.KeyboardButton(u"\U0001F355"+'Pizza')
itembtn2 = types.KeyboardButton(u"\U0001F32E"+'Tacos')
itembtn3 = types.KeyboardButton(u"\U0001F414"+'chicken')
itembtn4 = types.KeyboardButton(u"\U0001F356"+'meat')
markup.add(itembtn1, itembtn2, itembtn3,itembtn4)

@bot.message_handler(commands=['start', 'help'])
def exemple_keyboard(message):
  cid = message.chat.id 
  bot.send_message(cid, "Choose a Categorie :",reply_markup=markup)

@bot.message_handler(commands=['startpay'])
def command_start(message):
    bot.send_message(message.chat.id,
                     "Hello," +str(message.from_user.first_name)+str(message.from_user.last_name)+" I'm the merchant bot."
                     " I can sell you a pizza or tacos or everything in our store."
                     " Use /start to buy, /terms for Terms and Conditions")

@bot.message_handler(commands=['terms'])
def command_terms(message):
    bot.send_message(message.chat.id,
                     'Thank you for shopping with our bot. We hope you like our store!\n'
                     '1. If your item was not delivered on time, kindly contact our service workshops on +212666666666.\n'
                     '2. If you would like a refund, kindly apply and we will have sent it to you immediately.\n')


@bot.shipping_query_handler(func=lambda query: True)
def shipping(shipping_query):
    #print(shipping_query)
    bot.answer_shipping_query(shipping_query.id, ok=True, shipping_options=shipping_options,
                              error_message='Oh, Try again later!')   
@bot.pre_checkout_query_handler(func=lambda query: True)
def checkout(pre_checkout_query):
    bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True,
                                  error_message=" try to pay again in a few minutes")


@bot.message_handler(content_types=['successful_payment'])
def got_payment(message):
  print(message)
  bot.send_message(message.chat.id,
  'Hoooooray! Thanks for payment! We will proceed your order for `{} {}` as fast as possible! '
  'Stay in touch.'.format(
    message.successful_payment.total_amount / 100, message.successful_payment.currency),parse_mode='Markdown')                                                  


@bot.message_handler(func=lambda message: True)
def echo_all(message):
  if message.text == u"\U0001F355"+'Pizza':
    for i in pizza:
      bot.send_invoice(message.chat.id, title=i['title'],
                     description=i['description'],
                     provider_token=provider_token,
                     currency='usd',
                     photo_url=i['photo'],
                     photo_height=300,  # !=0/None or picture won't be shown
                     photo_width=300,
                     photo_size=300,
                     is_flexible=True,  # True If you need to set up Shipping Fee
                     prices=i['price'],
                     start_parameter='pizza',
                     invoice_payload='HAPPY FRIDAYS COUPON')
  elif message.text == u"\U0001F32E"+'Tacos':
    for i in tacos:
      bot.send_invoice(message.chat.id, title=i['title'],
                     description=i['description'],
                     provider_token=provider_token,
                     currency='usd',
                     photo_url=i['photo'],
                     photo_height=300,  # !=0/None or picture won't be shown
                     photo_width=300,
                     photo_size=300,
                     is_flexible=True,  # True If you need to set up Shipping Fee
                     prices=i['price'],
                     start_parameter='Tacos',
                     invoice_payload='HAPPY FRIDAYS COUPON')
  elif message.text == u"\U0001F414"+'chicken':
    for i in chicken:
      bot.send_invoice(message.chat.id, title=i['title'],
                     description=i['description'],
                     provider_token=provider_token,
                     currency='usd',
                     photo_url=i['photo'],
                     photo_height=300,  # !=0/None or picture won't be shown
                     photo_width=300,
                     photo_size=300,
                     is_flexible=True,  # True If you need to set up Shipping Fee
                     prices=i['price'],
                     start_parameter='chicken',
                     invoice_payload='HAPPY FRIDAYS COUPON')
  elif message.text == u"\U0001F356"+'meat':
    for i in meat:
      bot.send_invoice(message.chat.id, title=i['title'],
                     description=i['description'],
                     provider_token=provider_token,
                     currency='usd',
                     photo_url=i['photo'],
                     photo_height=300,  # !=0/None or picture won't be shown
                     photo_width=300,
                     photo_size=300,
                     is_flexible=True,  # True If you need to set up Shipping Fee
                     prices=i['price'],
                     start_parameter='meat',
                     invoice_payload='HAPPY FRIDAYS COUPON')


@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
  bot.answer_callback_query(callback_query_id=call.id,
                              show_alert=True,
                              text=call.data)

bot.skip_pending = True            
bot.polling(none_stop=True)
