import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

bot = telebot.TeleBot('5662928795:AAHhdf4WxBx_CGY1x5CU85Y5qR06Y3UgcFQ')

points = 0

def buttom():
    but = ReplyKeyboardMarkup(row_width=2)
    butitm1 = KeyboardButton('Розпочати!')
    butitm2 = KeyboardButton("Інструкція")
    butitm3 = KeyboardButton('Результати!')
    but.add(butitm1, butitm2, butitm3)
    return but

def markup1():
    markup = InlineKeyboardMarkup(row_width=2)
    itm1 = InlineKeyboardButton('1', callback_data='1')
    itm2 = InlineKeyboardButton('2', callback_data='2')
    itm3 = InlineKeyboardButton('3', callback_data='3')
    itm4 = InlineKeyboardButton('4', callback_data='4')
    markup.add(itm1, itm2, itm3, itm4)

    return markup
def markup2():
    markup2 = InlineKeyboardMarkup(row_width=2)
    itm1 = InlineKeyboardButton('1', callback_data='5')
    itm2 = InlineKeyboardButton('2', callback_data='6')
    itm3 = InlineKeyboardButton('3', callback_data='7')
    itm4 = InlineKeyboardButton('4', callback_data='8')
    markup2.add(itm1, itm2, itm3, itm4)

    return markup2
def markup3():
    markup = InlineKeyboardMarkup(row_width=2)
    itm1 = InlineKeyboardButton('1', callback_data='9')
    itm2 = InlineKeyboardButton('2', callback_data='10')
    itm3 = InlineKeyboardButton('3', callback_data='11')
    itm4 = InlineKeyboardButton('4', callback_data='12')
    markup.add(itm1, itm2, itm3, itm4)

    return markup
def markup4():
    markup = InlineKeyboardMarkup(row_width=2)
    itm1 = InlineKeyboardButton('1', callback_data='13')
    itm2 = InlineKeyboardButton('2', callback_data='14')
    itm3 = InlineKeyboardButton('3', callback_data='15')
    itm4 = InlineKeyboardButton('4', callback_data='16')
    markup.add(itm1, itm2, itm3, itm4)

    return markup
def markup5():
    markup = InlineKeyboardMarkup(row_width=2)
    itm1 = InlineKeyboardButton('1', callback_data='17')
    itm2 = InlineKeyboardButton('2', callback_data='18')
    itm3 = InlineKeyboardButton('3', callback_data='19')
    itm4 = InlineKeyboardButton('4', callback_data='20')
    markup.add(itm1, itm2, itm3, itm4)

    return markup
def markup6():
    markup = InlineKeyboardMarkup(row_width=2)
    itm1 = InlineKeyboardButton('1', callback_data='21')
    itm2 = InlineKeyboardButton('2', callback_data='22')
    itm3 = InlineKeyboardButton('3', callback_data='23')
    itm4 = InlineKeyboardButton('4', callback_data='24')
    markup.add(itm1, itm2, itm3, itm4)

    return markup
def markup7():
    markup = InlineKeyboardMarkup(row_width=2)
    itm1 = InlineKeyboardButton('1', callback_data='25')
    itm2 = InlineKeyboardButton('2', callback_data='26')
    itm3 = InlineKeyboardButton('3', callback_data='27')
    itm4 = InlineKeyboardButton('4', callback_data='28')
    markup.add(itm1, itm2, itm3, itm4)

    return markup
def markup8():
    markup = InlineKeyboardMarkup(row_width=2)
    itm1 = InlineKeyboardButton('1', callback_data='29')
    itm2 = InlineKeyboardButton('2', callback_data='30')
    itm3 = InlineKeyboardButton('3', callback_data='31')
    itm4 = InlineKeyboardButton('4', callback_data='32')
    markup.add(itm1, itm2, itm3, itm4)

    return markup
def markup9():
    markup = InlineKeyboardMarkup(row_width=2)
    itm1 = InlineKeyboardButton('1', callback_data='33')
    itm2 = InlineKeyboardButton('2', callback_data='34')
    itm3 = InlineKeyboardButton('3', callback_data='35')
    itm4 = InlineKeyboardButton('4', callback_data='36')
    markup.add(itm1, itm2, itm3, itm4)

    return markup
def markup10():
    markup = InlineKeyboardMarkup(row_width=2)
    itm1 = InlineKeyboardButton('1', callback_data='37')
    itm2 = InlineKeyboardButton('2', callback_data='38')
    itm3 = InlineKeyboardButton('3', callback_data='39')
    itm4 = InlineKeyboardButton('4', callback_data='40')
    markup.add(itm1, itm2, itm3, itm4)

    return markup
def markup11():
    markup = InlineKeyboardMarkup(row_width=2)
    itm1 = InlineKeyboardButton('1', callback_data='41')
    itm2 = InlineKeyboardButton('2', callback_data='42')
    itm3 = InlineKeyboardButton('3', callback_data='43')
    itm4 = InlineKeyboardButton('4', callback_data='44')
    markup.add(itm1, itm2, itm3, itm4)

    return markup
def markup12():
    markup = InlineKeyboardMarkup(row_width=2)
    itm1 = InlineKeyboardButton('1', callback_data='45')
    itm2 = InlineKeyboardButton('2', callback_data='46')
    itm3 = InlineKeyboardButton('3', callback_data='47')
    itm4 = InlineKeyboardButton('4', callback_data='48')
    markup.add(itm1, itm2, itm3, itm4)

    return markup
def markup13():
    markup = InlineKeyboardMarkup(row_width=2)
    itm1 = InlineKeyboardButton('1', callback_data='49')
    itm2 = InlineKeyboardButton('2', callback_data='50')
    itm3 = InlineKeyboardButton('3', callback_data='51')
    itm4 = InlineKeyboardButton('4', callback_data='52')
    markup.add(itm1, itm2, itm3, itm4)

    return markup
def markup14():
    markup = InlineKeyboardMarkup(row_width=2)
    itm1 = InlineKeyboardButton('1', callback_data='53')
    itm2 = InlineKeyboardButton('2', callback_data='54')
    itm3 = InlineKeyboardButton('3', callback_data='55')
    itm4 = InlineKeyboardButton('4', callback_data='56')
    markup.add(itm1, itm2, itm3, itm4)

    return markup
def markup15():
    markup = InlineKeyboardMarkup(row_width=2)
    itm1 = InlineKeyboardButton('1', callback_data='57')
    itm2 = InlineKeyboardButton('2', callback_data='58')
    itm3 = InlineKeyboardButton('3', callback_data='59')
    itm4 = InlineKeyboardButton('4', callback_data='60')
    markup.add(itm1, itm2, itm3, itm4)

    return markup
def markup16():
    markup = InlineKeyboardMarkup(row_width=2)
    itm1 = InlineKeyboardButton('1', callback_data='61')
    itm2 = InlineKeyboardButton('2', callback_data='62')
    itm3 = InlineKeyboardButton('3', callback_data='63')
    itm4 = InlineKeyboardButton('4', callback_data='64')
    markup.add(itm1, itm2, itm3, itm4)

    return markup
def markup17():
    markup = InlineKeyboardMarkup(row_width=2)
    itm1 = InlineKeyboardButton('1', callback_data='65')
    itm2 = InlineKeyboardButton('2', callback_data='66')
    itm3 = InlineKeyboardButton('3', callback_data='67')
    itm4 = InlineKeyboardButton('4', callback_data='68')
    markup.add(itm1, itm2, itm3, itm4)

    return markup
def markup18():
    markup = InlineKeyboardMarkup(row_width=2)
    itm1 = InlineKeyboardButton('1', callback_data='69')
    itm2 = InlineKeyboardButton('2', callback_data='70')
    itm3 = InlineKeyboardButton('3', callback_data='71')
    itm4 = InlineKeyboardButton('4', callback_data='72')
    markup.add(itm1, itm2, itm3, itm4)

    return markup
def markup19():
    markup = InlineKeyboardMarkup(row_width=2)
    itm1 = InlineKeyboardButton('1.', callback_data='73')
    itm2 = InlineKeyboardButton('2', callback_data='73')
    itm3 = InlineKeyboardButton('3', callback_data='75')
    itm4 = InlineKeyboardButton('4', callback_data='76')
    markup.add(itm1, itm2, itm3, itm4)

    return markup
def markup20():
    markup = InlineKeyboardMarkup(row_width=2)
    itm1 = InlineKeyboardButton('1', callback_data='77')
    itm2 = InlineKeyboardButton('2', callback_data='78')
    itm3 = InlineKeyboardButton('3', callback_data='79')
    itm4 = InlineKeyboardButton('4', callback_data='80')
    markup.add(itm1, itm2, itm3, itm4)

    return markup
def markup21():
    markup = InlineKeyboardMarkup(row_width=2)
    itm1 = InlineKeyboardButton('1', callback_data='81')
    itm2 = InlineKeyboardButton('2', callback_data='82')
    itm3 = InlineKeyboardButton('3', callback_data='83')
    itm4 = InlineKeyboardButton('4', callback_data='84')
    markup.add(itm1, itm2, itm3, itm4)

    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привіт. Цей бот повинен розрахувати бали депресії за шкалою Бека.', reply_markup=buttom())

@bot.message_handler(content_types=['text'])
def count(message):
    global points
    if message.text == 'Розпочати!':
        points = 0
        bot.send_message(message.chat.id, 'Вам потрібно обрати твердження, яке найбільше вам підходить')
        bot.send_message(message.chat.id, 'Питання 1:Сум')
        bot.send_message(message.chat.id, '\n 1.Я не почуваюся засмученим, сумним.\n 2. Мені сумно час від часу.\n 3. Я постійно почуваюся засмученим.\n 4. Я настільки засмучений і нещасливий, що це здається нестерпним.',reply_markup=markup1())
    elif message.text == 'Результати!':
        if points <= 13:
            bot.send_message(message.chat.id,"Депресивних симптомів немає. З вашим психічним здоров'ям все гаразд.")
        elif points > 13 and points <= 19:
            bot.send_message(message.chat.id, "Можлива легка депресія (субдепресія).Субдепресія властива психічно "
                                              "здоровим людям, які не обділеним інтелектом, які мають певні досить "
                                              "високі життєві домагання, але зіткнулися з перешкодами, що стали для "
                                              "них нездоланними. Детальніше можете ознайомитись "
                                              "тут: "
                                              "https://www.kozaky.org.ua/chomu-vinikaye-subdepressivnoe-stan-i-yak-z-nim-borotisya/")
        if points > 19 and points <= 28:
            bot.send_message(message.chat.id, "Помірна депресія.Про помірну депресію можна говорити за наявності 6 і "
                                              "більше симптомів, які супроводжуються значною втратою працездатності. "
                                              "Якщо легка депресія триває принаймні 2 роки, то можна говорити про "
                                              "наявність у пацієнта дистимії.За умови діагностики депресії легкого "
                                              "ступеня і раннього початку рекомендують активне спостереження фахівця.")
        elif points > 28:
            bot.send_message(message.chat.id, "Тяжка депресія. Чим більше баллів, тим важча депрссія.(29-63).Тяжкі "
                                              "форми депресії характеризуються так званою «депресивною тріадою»:"
                                              " зниженням настрою, загальмованістю мислення та руховою загальмованістю."
                                              "Депресивний настрій у деяких випадках може бути нормальною тимчасовою "
                                              "реакцією на життєві події, як, наприклад, втрата близької людини. "
                                              "Депресія може бути симптомом деяких соматичних захворювань та побічним "
                                              "ефектом деяких препаратів та лікування.Якщо ваше самопочуття не зміниться,"
                                              "то зверніться до спеціоліста.")
        bot.send_message(message.chat.id,'Шкала депресії Бека є однозначним діагностичним інструментом. Вона лише одне '
                                         'із ключових обстежень, які проводить лікар, щоб виявити психічний розлад.'
                                         'Якщо у вас погані результати, то не займайтеся самолікуванням та зверніться '
                                         'до професійного лікаря.')
    if message.text == 'Інструкція':
        bot.send_message(message.chat.id, "Уважно прочитайте 21 групу тверджень. У кожній позначте той пункт, який "
                                          "найбільш повно відображає ваш стан протягом останніх двох тижнів, включаючи "
                                          "сьогоднішній день. Якщо в одній із груп вам складно визначитися між "
                                          "двома-трьома варіантами, вибирайте той, за який налічується більше балів. "
                                          "Як правило, проходження тесту займає не більше 10 хвилин.Після проходження "
                                          "21 питання натисніть або напишіть Результатти!")

@bot.callback_query_handler(func=lambda c: True)
def questions(call):
    global points
    if call.data == '1':
        points += 0
        bot.send_message(call.from_user.id, 'Питання 2:Ставлення до майбутнього')
        bot.send_message(call.from_user.id,'1.Майбутнє не здається мені страшним.\n2.Я почав перейматися майбутнім частіше, ніж раніше.\n3.Я не чекаю нічого хорошого.\n4.Здається, моє майбутнє безнадійне. Все стає лише гіршим.',reply_markup=markup2())
    elif call.data == '2':
        points += 1
        bot.send_message(call.from_user.id, 'Питання 2:Ставлення до майбутнього')
        bot.send_message(call.from_user.id,'1.Майбутнє не здається мені страшним.\n2.Я почав перейматися майбутнім частіше, ніж раніше.\n3.Я не чекаю нічого хорошого.\n4.Здається, моє майбутнє безнадійне. Все стає лише гіршим.',reply_markup=markup2())
    if call.data == '3':
        points += 2
        bot.send_message(call.from_user.id, 'Питання 2:Ставлення до майбутнього')
        bot.send_message(call.from_user.id,'1.Майбутнє не здається мені страшним.\n2.Я почав перейматися майбутнім частіше, ніж раніше.\n3.Я не чекаю нічого хорошого.\n4.Здається, моє майбутнє безнадійне. Все стає лише гіршим.',reply_markup=markup2())
    elif call.data == '4':
        points += 3
        bot.send_message(call.from_user.id, 'Питання 2:Ставлення до майбутнього')
        bot.send_message(call.from_user.id,'1.Майбутнє не здається мені страшним.\n2.Я почав перейматися майбутнім частіше, ніж раніше.\n3.Я не чекаю нічого хорошого.\n4.Здається, моє майбутнє безнадійне. Все стає лише гіршим.',reply_markup=markup2())
    if call.data == '5':
        points += 0
        bot.send_message(call.from_user.id, 'Питання 3:Минулі невдачі')
        bot.send_message(call.from_user.id,'1.Мене навряд чи можна назвати невдахою.\n2.Провали та невдачі трапляються зі мною частіше, ніж з іншими людьми.\n3.У моєму житті було безліч невдач і розчарувань.\n4.Я повний невдаха.', reply_markup=markup3())
    elif call.data == '6':
        points += 1
        bot.send_message(call.from_user.id, 'Питання 3:Минулі невдачі')
        bot.send_message(call.from_user.id,'1.Мене навряд чи можна назвати невдахою.\n2.Провали та невдачі трапляються зі мною частіше, ніж з іншими людьми.\n3.У моєму житті було безліч невдач і розчарувань.\n4.Я повний невдаха.', reply_markup=markup3())
    if call.data == '7':
        points += 2
        bot.send_message(call.from_user.id, 'Питання 3:Минулі невдачі')
        bot.send_message(call.from_user.id,'1.Мене навряд чи можна назвати невдахою.\n2.Провали та невдачі трапляються зі мною частіше, ніж з іншими людьми.\n3.У моєму житті було безліч невдач і розчарувань.\n4.Я повний невдаха.', reply_markup=markup3())
    elif call.data == '8':
        points += 3
        bot.send_message(call.from_user.id, 'Питання 3:Минулі невдачі')
        bot.send_message(call.from_user.id,'1.Мене навряд чи можна назвати невдахою.\n2.Провали та невдачі трапляються зі мною частіше, ніж з іншими людьми.\n3.У моєму житті було безліч невдач і розчарувань.\n4.Я повний невдаха.', reply_markup=markup3())
    if call.data == '9':
        points += 0
        bot.send_message(call.from_user.id, 'Питання 4:Задоволення від життя', )
        bot.send_message(call.from_user.id, '1.Я цілком задоволений життям.\n2.Раніше я отримував більше задоволення від того, що відбувається.\n3.Я перестав радіти навіть тим речам, які робили мене щасливим раніше.\n4.Моє життя жахливе, і немає жодного просвіту.', reply_markup=markup4())
    elif call.data == '10':
        points += 1
        bot.send_message(call.from_user.id, 'Питання 4:Задоволення від життя')
        bot.send_message(call.from_user.id,'1.Я цілком задоволений життям.\n2.Раніше я отримував більше задоволення від того, що відбувається.\n3.Я перестав радіти навіть тим речам, які робили мене щасливим раніше.\n4.Моє життя жахливе, і немає жодного просвіту.',reply_markup=markup4())
    if call.data == '11':
        points += 2
        bot.send_message(call.from_user.id, 'Питання 4:Задоволення від життя')
        bot.send_message(call.from_user.id,'1.Я цілком задоволений життям.\n2.Раніше я отримував більше задоволення від того, що відбувається.\n3.Я перестав радіти навіть тим речам, які робили мене щасливим раніше.\n4.Моє життя жахливе, і немає жодного просвіту.',reply_markup=markup4())
    elif call.data == '12':
        points += 3
        bot.send_message(call.from_user.id, 'Питання 4:Задоволення від життя')
        bot.send_message(call.from_user.id,'1.Я цілком задоволений життям.\n2.Раніше я отримував більше задоволення від того, що відбувається.\n3.Я перестав радіти навіть тим речам, які робили мене щасливим раніше.\n4.Моє життя жахливе, і немає жодного просвіту.',reply_markup=markup4())
    if call.data == '13':
        points += 0
        bot.send_message(call.from_user.id, 'Питання 5:Почуття провини')
        bot.send_message(call.from_uae.id, '1.Я не відчуваю якоїсь особливої провини ні перед ким і ні за що.\n2.Доволі часто я почуваюся винним за те, що міг би зробити, але не зробив.\n3.Я відчуваю провину дуже часто.\n4.Постійно відчуваю, що перед усіма винний.',reply_markup=markup5())
    elif call.data == '14':
        points += 1
        bot.send_message(call.from_user.id, 'Питання 5:Почуття провини')
        bot.send_message(call.from_user.id,'1.Я не відчуваю якоїсь особливої провини ні перед ким і ні за що.\n2.Доволі часто я почуваюся винним за те, що міг би зробити, але не зробив.\n3.Я відчуваю провину дуже часто.\n4.Постійно відчуваю, що перед усіма винний.',reply_markup=markup5())
    if call.data == '15':
        points += 2
        bot.send_message(call.from_user.id, 'Питання 5:Почуття провини')
        bot.send_message(call.from_user.id,'1.Я не відчуваю якоїсь особливої провини ні перед ким і ні за що.\n2.Доволі часто я почуваюся винним за те, що міг би зробити, але не зробив.\n3.Я відчуваю провину дуже часто.\n4.Постійно відчуваю, що перед усіма винний.',reply_markup=markup5())
    elif call.data == '16':
        points += 3
        bot.send_message(call.from_user.id, 'Питання 5:Почуття провини')
        bot.send_message(call.from_user.id,'1.Я не відчуваю якоїсь особливої провини ні перед ким і ні за що.\n2.Доволі часто я почуваюся винним за те, що міг би зробити, але не зробив.\n3.Я відчуваю провину дуже часто.\n4.Постійно відчуваю, що перед усіма винний.',reply_markup=markup5())
    if call.data == '17':
        points += 0
        bot.send_message(call.from_user.id, 'Питання 6:Очікування покарання')
        bot.send_message(call.from_user.id, '1.Я не робив нічого такого, за що мене варто було б покарати.\n2.Мені є за що бути покараним.\n3.Я постійно живу в очікуванні кари.\n4.Я вже покараний за все, що зробив.',reply_markup=markup6())
    elif call.data == '18':
        points += 1
        bot.send_message(call.from_user.id, 'Питання 6:Очікування покарання')
        bot.send_message(call.from_user.id,
                         '1.Я не робив нічого такого, за що мене варто було б покарати.\n2.Мені є за що бути покараним.\n3.Я постійно живу в очікуванні кари.\n4.Я вже покараний за все, що зробив.',reply_markup=markup6())
    if call.data == '19':
        points += 2
        bot.send_message(call.from_user.id, 'Питання 6:Очікування покарання')
        bot.send_message(call.from_user.id,
                         '1.Я не робив нічого такого, за що мене варто було б покарати.\n2.Мені є за що бути покараним.\n3.Я постійно живу в очікуванні кари.\n4.Я вже покараний за все, що зробив.',reply_markup=markup6())
    elif call.data == '20':
        points += 3
        bot.send_message(call.from_user.id, 'Питання 6:Очікування покарання')
        bot.send_message(call.from_user.id,
                         '1.Я не робив нічого такого, за що мене варто було б покарати.\n2.Мені є за що бути покараним.\n3.Я постійно живу в очікуванні кари.\n4.Я вже покараний за все, що зробив.',reply_markup=markup6())
    if call.data == '21':
        points += 0
        bot.send_message(call.from_user.id, 'Питання 7:Ставлення до себе')
        bot.send_message(call.from_iser.id, '1.Я ставлюся до себе як завжди.\n2.Здається, я втратив впевненість у собі.\n3.Я розчарований у собі.\n4.Я себе просто ненавиджу.',reply_markup=markup7())
    elif call.data == '22':
        points += 1
        bot.send_message(call.from_user.id, 'Питання 7:Ставлення до себе')
        bot.send_message(call.from_user.id,
                         '1.Я ставлюся до себе як завжди.\n2.Здається, я втратив впевненість у собі.\n3.Я розчарований у собі.\n4.Я себе просто ненавиджу.',
                         reply_markup=markup7())
    if call.data == '23':
        points += 2
        bot.send_message(call.from_user.id, 'Питання 7:Ставлення до себе')
        bot.send_message(call.from_user.id,
                         '1.Я ставлюся до себе як завжди.\n2.Здається, я втратив впевненість у собі.\n3.Я розчарований у собі.\n4.Я себе просто ненавиджу.',
                         reply_markup=markup7())
    elif call.data == '24':
        points += 3
        bot.send_message(call.from_user.id, 'Питання 7:Ставлення до себе')
        bot.send_message(call.from_user.id,
                         '1.Я ставлюся до себе як завжди.\n2.Здається, я втратив впевненість у собі.\n3.Я розчарований у собі.\n4.Я себе просто ненавиджу.',
                         reply_markup=markup7())
    if call.data == '25':
        points += 0
        bot.send_message(call.from_user.id, 'Питання 8:Самокритичність')
        bot.send_message(call.from_user.id, '1.Знаю, що загалом я не гірший за інших.\n2.Я бачу у собі більше недоліків, ніж раніше.\n3.Я знаю всі свої недоліки і нещадно критикую себе за них.\n4.Я один суцільний недолік. Тільки я винен у всьому поганому, що відбувається довкола.',reply_markup=markup8())
    elif call.data == '26':
        points += 1
        bot.send_message(call.from_user.id, 'Питання 8:Самокритичність')
        bot.send_message(call.from_user.id,
                         '1.Знаю, що загалом я не гірший за інших.\n2.Я бачу у собі більше недоліків, ніж раніше.\n3.Я знаю всі свої недоліки і нещадно критикую себе за них.\n4.Я один суцільний недолік. Тільки я винен у всьому поганому, що відбувається довкола.',
                         reply_markup=markup8())
    if call.data == '27':
        points += 2
        bot.send_message(call.from_user.id, 'Питання 8:Самокритичність')
        bot.send_message(call.from_user.id,
                         '1.Знаю, що загалом я не гірший за інших.\n2.Я бачу у собі більше недоліків, ніж раніше.\n3.Я знаю всі свої недоліки і нещадно критикую себе за них.\n4.Я один суцільний недолік. Тільки я винен у всьому поганому, що відбувається довкола.',
                         reply_markup=markup8())
    elif call.data == '28':
        points += 3
        bot.send_message(call.from_user.id, 'Питання 8:Самокритичність')
        bot.send_message(call.from_user.id,
                         '1.Знаю, що загалом я не гірший за інших.\n2.Я бачу у собі більше недоліків, ніж раніше.\n3.Я знаю всі свої недоліки і нещадно критикую себе за них.\n4.Я один суцільний недолік. Тільки я винен у всьому поганому, що відбувається довкола.',
                         reply_markup=markup8())
    if call.data == '29':
        points += 0
        bot.send_message(call.from_user.id, 'Питання 9:Суїцидальні думки')
        bot.send_message(call.from_user.id,'1.Я ніколи не думав накласти на себе руки, це не мій варіант вирішення проблем.\n2.Іноді у мене проскакують думки про самогубство, але вони випадкові, я не планую це робити.\n3.Регулярно думаю, що самогубство було б непоганим виходом.\n4.Я відчуваю полегшення, покінчивши з цим усім. Чекаю лише, коли трапиться нагода.',reply_markup=markup9())
    elif call.data == '30':
        points += 1
        bot.send_message(call.from_user.id, 'Питання 9:Суїцидальні думки')
        bot.send_message(call.from_user.id,
                         '1.Я ніколи не думав накласти на себе руки, це не мій варіант вирішення проблем.\n2.Іноді у мене проскакують думки про самогубство, але вони випадкові, я не планую це робити.\n3.Регулярно думаю, що самогубство було б непоганим виходом.\n4.Я відчуваю полегшення, покінчивши з цим усім. Чекаю лише, коли трапиться нагода.',
                         reply_markup=markup9())
    if call.data == '31':
        points += 2
        bot.send_message(call.from_user.id, 'Питання 9:Суїцидальні думки')
        bot.send_message(call.from_user.id,
                         '1.Я ніколи не думав накласти на себе руки, це не мій варіант вирішення проблем.\n2.Іноді у мене проскакують думки про самогубство, але вони випадкові, я не планую це робити.\n3.Регулярно думаю, що самогубство було б непоганим виходом.\n4.Я відчуваю полегшення, покінчивши з цим усім. Чекаю лише, коли трапиться нагода.',
                         reply_markup=markup9())
    elif call.data == '32':
        points += 3
        bot.send_message(call.from_user.id, 'Питання 9:Суїцидальні думки')
        bot.send_message(call.from_user.id,
                         '1.Я ніколи не думав накласти на себе руки, це не мій варіант вирішення проблем.\n2.Іноді у мене проскакують думки про самогубство, але вони випадкові, я не планую це робити.\n3.Регулярно думаю, що самогубство було б непоганим виходом.\n4.Я відчуваю полегшення, покінчивши з цим усім. Чекаю лише, коли трапиться нагода.',
                         reply_markup=markup9())
    if call.data == '33':
        points += 0
        bot.send_message(call.from_user.id, 'Питання 10:Бажання плакати')
        bot.send_message(call.from_user.id,'1.Якщо я іноді й плачу, то явно не більше, ніж раніше.\n2.Зараз я плачу частіше, ніж раніше.\n3.Плачу майже постійно.\n4.Мені хочеться плакати, але я вже не можу.',reply_markup=markup10())
    elif call.data == '34':
        points += 1
        bot.send_message(call.from_user.id, 'Питання 10:Бажання плакати')
        bot.send_message(call.from_user.id,
                         '1.Якщо я іноді й плачу, то явно не більше, ніж раніше.\n2.Зараз я плачу частіше, ніж раніше.\n3.Плачу майже постійно.\n4.Мені хочеться плакати, але я вже не можу.',
                         reply_markup=markup10())
    if call.data == '35':
        points += 2
        bot.send_message(call.from_user.id, 'Питання 10:Бажання плакати')
        bot.send_message(call.from_user.id,
                         '1.Якщо я іноді й плачу, то явно не більше, ніж раніше.\n2.Зараз я плачу частіше, ніж раніше.\n3.Плачу майже постійно.\n4.Мені хочеться плакати, але я вже не можу.',
                         reply_markup=markup10())
    elif call.data == '36':
        points += 3
        bot.send_message(call.from_user.id, 'Питання 10:Бажання плакати')
        bot.send_message(call.from_user.id,
                         '1.Якщо я іноді й плачу, то явно не більше, ніж раніше.\n2.Зараз я плачу частіше, ніж раніше.\n3.Плачу майже постійно.\n4.Мені хочеться плакати, але я вже не можу.',
                         reply_markup=markup10())
    if call.data == '37':
        points += 0
        bot.send_message(call.from_user.id, 'Питання 11:Занепокоєння, нервозність')
        bot.send_message(call.from_user.id,'1.Я спокійний, як завжди.\n2.Я почуваюся більш неспокійним, ніж зазвичай.\n3.Постійно відчуваю нервозність, смикаюсь по дрібницях.\n4.Я настільки розвинений, що мені доводиться весь час рухатися або робити щось, інакше я просто збожеволію.',reply_markup=markup11())
    elif call.data == '38':
        points += 1
        bot.send_message(call.from_user.id, 'Питання 11:Занепокоєння, нервозність')
        bot.send_message(call.from_user.id,
                         '1.Я спокійний, як завжди.\n2.Я почуваюся більш неспокійним, ніж зазвичай.\n3.Постійно відчуваю нервозність, смикаюсь по дрібницях.\n4.Я настільки розвинений, що мені доводиться весь час рухатися або робити щось, інакше я просто збожеволію.',
                         reply_markup=markup11())
    if call.data == '39':
        points += 2
        bot.send_message(call.from_user.id, 'Питання 11:Занепокоєння, нервозність')
        bot.send_message(call.from_user.id,
                         '1.Я спокійний, як завжди.\n2.Я почуваюся більш неспокійним, ніж зазвичай.\n3.Постійно відчуваю нервозність, смикаюсь по дрібницях.\n4.Я настільки розвинений, що мені доводиться весь час рухатися або робити щось, інакше я просто збожеволію.',
                         reply_markup=markup11())
    elif call.data == '40':
        points += 3
        bot.send_message(call.from_user.id, 'Питання 11:Занепокоєння, нервозність')
        bot.send_message(call.from_user.id,
                         '1.Я спокійний, як завжди.\n2.Я почуваюся більш неспокійним, ніж зазвичай.\n3.Постійно відчуваю нервозність, смикаюсь по дрібницях.\n4.Я настільки розвинений, що мені доводиться весь час рухатися або робити щось, інакше я просто збожеволію.',
                         reply_markup=markup11())
    if call.data == '41':
        points += 0
        bot.send_message(call.from_user.id, 'Питання 12:Втрата інтересів')
        bot.send_message(call.from_user.id,'1.Мені, як і раніше, цікаві інші люди, у мене є захоплення.\n2.Я почав менше цікавитися тим, що відбувається довкола.\n3.З іншими людьми мені нудно, вони дратують.\n4.Я втратив інтерес до всього.',reply_markup=markup12())
    elif call.data == '42':
        points += 1
        bot.send_message(call.from_user.id, 'Питання 12:Втрата інтересів')
        bot.send_message(call.from_user.id,
                         '1.Мені, як і раніше, цікаві інші люди, у мене є захоплення.\n2.Я почав менше цікавитися тим, що відбувається довкола.\n3.З іншими людьми мені нудно, вони дратують.\n4.Я втратив інтерес до всього.',
                         reply_markup=markup12())
    if call.data == '43':
        points += 2
        bot.send_message(call.from_user.id, 'Питання 12:Втрата інтересів')
        bot.send_message(call.from_user.id,
                         '1.Мені, як і раніше, цікаві інші люди, у мене є захоплення.\n2.Я почав менше цікавитися тим, що відбувається довкола.\n3.З іншими людьми мені нудно, вони дратують.\n4.Я втратив інтерес до всього.',
                         reply_markup=markup12())
    elif call.data == '44':
        points += 3
        bot.send_message(call.from_user.id, 'Питання 12:Втрата інтересів')
        bot.send_message(call.from_user.id,
                         '1.Мені, як і раніше, цікаві інші люди, у мене є захоплення.\n2.Я почав менше цікавитися тим, що відбувається довкола.\n3.З іншими людьми мені нудно, вони дратують.\n4.Я втратив інтерес до всього.',
                         reply_markup=markup12())
    if call.data == '45':
        points += 0
        bot.send_message(call.from_user.id, 'Питання 13:Здатність приймати рішення')
        bot.send_message(call.from_user.id,'1.Я приймаю рішення так само, як і раніше.\n2.Мені стало складніше щось вирішувати, я частіше сумніваюсь і хотів би, щоби хтось узяв відповідальність на себе.\n3.Кожне рішення дається мені важко.\n4.Я не хочу і не можу нічого вирішувати.',reply_markup=markup15())
    elif call.data == '46':
        points += 1
        bot.send_message(call.from_user.id, 'Питання 13:Здатність приймати рішення')
        bot.send_message(call.from_user.id,
                         '1.Я приймаю рішення так само, як і раніше.\n2.Мені стало складніше щось вирішувати, я частіше сумніваюсь і хотів би, щоби хтось узяв відповідальність на себе.\n3.Кожне рішення дається мені важко.\n4.Я не хочу і не можу нічого вирішувати.',
                         reply_markup=markup15())
    if call.data == '47':
        points += 2
        bot.send_message(call.from_user.id, 'Питання 13:Здатність приймати рішення')
        bot.send_message(call.from_user.id,
                         '1.Я приймаю рішення так само, як і раніше.\n2.Мені стало складніше щось вирішувати, я частіше сумніваюсь і хотів би, щоби хтось узяв відповідальність на себе.\n3.Кожне рішення дається мені важко.\n4.Я не хочу і не можу нічого вирішувати.',
                         reply_markup=markup15())
    elif call.data == '48':
        points += 3
        bot.send_message(call.from_user.id, 'Питання 13:Здатність приймати рішення')
        bot.send_message(call.from_user.id,
                         '1.Я приймаю рішення так само, як і раніше.\n2.Мені стало складніше щось вирішувати, я частіше сумніваюсь і хотів би, щоби хтось узяв відповідальність на себе.\n3.Кожне рішення дається мені важко.\n4.Я не хочу і не можу нічого вирішувати.',
                         reply_markup=markup15())
    if call.data == '49':
        points += 0
        bot.send_message(call.from_user.id, 'Питання 14:Власна потреба')
        bot.send_message(call.from_user.id,'1.Я все ще потрібний і іншим, і самому собі.\n2.В мені щось надломилося і все частіше здається, що я нікому не потрібний.\n3.Я почуваюся нікчемним проти іншими.\n4.Я абсолютно нікому не потрібний.',reply_markup=markup14())
    elif call.data == '50':
        points += 1
        bot.send_message(call.from_user.id, 'Питання 14:Власна потреба')
        bot.send_message(call.from_user.id,
                         '1.Я все ще потрібний і іншим, і самому собі.\n2.В мені щось надломилося і все частіше здається, що я нікому не потрібний.\n3.Я почуваюся нікчемним проти іншими.\n4.Я абсолютно нікому не потрібний.',
                         reply_markup=markup14())
    if call.data == '51':
        points += 2
        bot.send_message(call.from_user.id, 'Питання 14:Власна потреба')
        bot.send_message(call.from_user.id,
                         '1.Я все ще потрібний і іншим, і самому собі.\n2.В мені щось надломилося і все частіше здається, що я нікому не потрібний.\n3.Я почуваюся нікчемним проти іншими.\n4.Я абсолютно нікому не потрібний.',
                         reply_markup=markup14())
    elif call.data == '52':
        points += 3
        bot.send_message(call.from_user.id, 'Питання 14:Власна потреба')
        bot.send_message(call.from_user.id,
                         '1.Я все ще потрібний і іншим, і самому собі.\n2.В мені щось надломилося і все частіше здається, що я нікому не потрібний.\n3.Я почуваюся нікчемним проти іншими.\n4.Я абсолютно нікому не потрібний.',
                         reply_markup=markup14())
    if call.data == '53':
        points += 0
        bot.send_message(call.from_user.id, 'Питання 15:Оцінка внутрішньої енергії')
        bot.send_message(call.from_user.id,'1.Я енергійний як завжди.\n2. Останнім часом у мене менше енергії, ніж було раніше.\n3.Мені не вистачає сил, щоб робити те, що я маю.\n4.У мене немає сил ні на що.',reply_markup=markup15())
    elif call.data == '54':
        points += 1
        bot.send_message(call.from_user.id, 'Питання 15:Оцінка внутрішньої енергії')
        bot.send_message(call.from_user.id,
                         '1.Я енергійний як завжди.\n2. Останнім часом у мене менше енергії, ніж було раніше.\n3.Мені не вистачає сил, щоб робити те, що я маю.\n4.У мене немає сил ні на що.',
                         reply_markup=markup15())
    if call.data == '55':
        points += 2
        bot.send_message(call.from_user.id, 'Питання 15:Оцінка внутрішньої енергії')
        bot.send_message(call.from_user.id,
                         '1.Я енергійний як завжди.\n2. Останнім часом у мене менше енергії, ніж було раніше.\n3.Мені не вистачає сил, щоб робити те, що я маю.\n4.У мене немає сил ні на що.',
                         reply_markup=markup15())
    elif call.data == '56':
        points += 3
        bot.send_message(call.from_user.id, 'Питання 15:Оцінка внутрішньої енергії')
        bot.send_message(call.from_user.id,
                         '1.Я енергійний як завжди.\n2. Останнім часом у мене менше енергії, ніж було раніше.\n3.Мені не вистачає сил, щоб робити те, що я маю.\n4.У мене немає сил ні на що.',
                         reply_markup=markup15())
    if call.data == '57':
        points += 0
        bot.send_message(call.from_user.id, 'Питання 16:Режим сну')
        bot.send_message(call.from_user.id,'1.Я сплю як завжди.\n2.Я почав спати більше чи менше, ніж раніше.\n3.Я сплю набагато більше (менше) звичайного.\n4.Я готовий спати більшу частину дня. Або навпаки: я часто прокидаюсь серед ночі і потім довго не можу заснути.',reply_markup=markup16())
    elif call.data == '58':
        points += 1
        bot.send_message(call.from_user.id, 'Питання 16:Режим сну')
        bot.send_message(call.from_user.id,
                         '1.Я сплю як завжди.\n2.Я почав спати більше чи менше, ніж раніше.\n3.Я сплю набагато більше (менше) звичайного.\n4.Я готовий спати більшу частину дня. Або навпаки: я часто прокидаюсь серед ночі і потім довго не можу заснути.',
                         reply_markup=markup16())
    if call.data == '59':
        points += 2
        bot.send_message(call.from_user.id, 'Питання 16:Режим сну')
        bot.send_message(call.from_user.id,
                         '1.Я сплю як завжди.\n2.Я почав спати більше чи менше, ніж раніше.\n3.Я сплю набагато більше (менше) звичайного.\n4.Я готовий спати більшу частину дня. Або навпаки: я часто прокидаюсь серед ночі і потім довго не можу заснути.',
                         reply_markup=markup16())
    elif call.data == '60':
        points += 3
        bot.send_message(call.from_user.id, 'Питання 16:Режим сну')
        bot.send_message(call.from_user.id,
                         '1.Я сплю як завжди.\n2.Я почав спати більше чи менше, ніж раніше.\n3.Я сплю набагато більше (менше) звичайного.\n4.Я готовий спати більшу частину дня. Або навпаки: я часто прокидаюсь серед ночі і потім довго не можу заснути.',
                         reply_markup=markup16())
    if call.data == '61':
        points += 0
        bot.send_message(call.from_user.id, 'Питання 17:Дратівливість')
        bot.send_message(call.from_user.id,'1.Я не більш дратівливий, ніж зазвичай.\n2.Я почав дратуватися легше, ніж раніше.\n3.Регулярно ловлю себе на тому, що все бісить.\n4.Постійно почуваюся роздратованим, навіть коли приводу, здавалося б, немає.',reply_markup=markup17())
    elif call.data == '62':
        points += 1
        bot.send_message(call.from_user.id, 'Питання 17:Дратівливість')
        bot.send_message(call.from_user.id,
                         '1.Я не більш дратівливий, ніж зазвичай.\n2.Я почав дратуватися легше, ніж раніше.\n3.Регулярно ловлю себе на тому, що все бісить.\n4.Постійно почуваюся роздратованим, навіть коли приводу, здавалося б, немає.',
                         reply_markup=markup17())
    if call.data == '63':
        points += 2
        bot.send_message(call.from_user.id, 'Питання 17:Дратівливість')
        bot.send_message(call.from_user.id,
                         '1.Я не більш дратівливий, ніж зазвичай.\n2.Я почав дратуватися легше, ніж раніше.\n3.Регулярно ловлю себе на тому, що все бісить.\n4.Постійно почуваюся роздратованим, навіть коли приводу, здавалося б, немає.',
                         reply_markup=markup17())
    elif call.data == '64':
        points += 3
        bot.send_message(call.from_user.id, 'Питання 17:Дратівливість')
        bot.send_message(call.from_user.id,
                         '1.Я не більш дратівливий, ніж зазвичай.\n2.Я почав дратуватися легше, ніж раніше.\n3.Регулярно ловлю себе на тому, що все бісить.\n4.Постійно почуваюся роздратованим, навіть коли приводу, здавалося б, немає.',
                         reply_markup=markup17())
    if call.data == '65':
        points += 0
        bot.send_message(call.from_user.id, 'Питання 18:Апетит')
        bot.send_message(call.from_user.id,'1.Я їм стільки ж, як завжди.\n2. Мій апетит трохи змінився: ловлю себе на тому, що їм більше чи менше, ніж раніше.\n3.Мій апетит набагато знизився (підвищився), ніж було до цього.\n4.У мене зовсім немає апетиту. Або навпаки: я постійно хочу їсти.',reply_markup=markup18())
    elif call.data == '66':
        points += 1
        bot.send_message(call.from_user.id, 'Питання 18:Апетит')
        bot.send_message(call.from_user.id,
                         '1.Я їм стільки ж, як завжди.\n2. Мій апетит трохи змінився: ловлю себе на тому, що їм більше чи менше, ніж раніше.\n3.Мій апетит набагато знизився (підвищився), ніж було до цього.\n4.У мене зовсім немає апетиту. Або навпаки: я постійно хочу їсти.',
                         reply_markup=markup18())
    if call.data == '67':
        points += 2
        bot.send_message(call.from_user.id, 'Питання 18:Апетит')
        bot.send_message(call.from_user.id,
                         '1.Я їм стільки ж, як завжди.\n2. Мій апетит трохи змінився: ловлю себе на тому, що їм більше чи менше, ніж раніше.\n3.Мій апетит набагато знизився (підвищився), ніж було до цього.\n4.У мене зовсім немає апетиту. Або навпаки: я постійно хочу їсти.',
                         reply_markup=markup18())
    elif call.data == '68':
        points += 3
        bot.send_message(call.from_user.id, 'Питання 18:Апетит')
        bot.send_message(call.from_user.id,
                         '1.Я їм стільки ж, як завжди.\n2. Мій апетит трохи змінився: ловлю себе на тому, що їм більше чи менше, ніж раніше.\n3.Мій апетит набагато знизився (підвищився), ніж було до цього.\n4.У мене зовсім немає апетиту. Або навпаки: я постійно хочу їсти.',
                         reply_markup=markup18())
    if call.data == '69':
        points += 0
        bot.send_message(call.from_user.id, 'Питання 19:Концентрація уваги')
        bot.send_message(call.from_user.id,'1.Мені легко сконцентруватися на тій чи іншій задачі.\n2. Останнім часом виникли деякі проблеми з концентрацією.\n3.Мені складно зосередитись на чомусь довше, ніж на кілька хвилин.\n4.Я виявив, що не можу сконцентруватися взагалі.',reply_markup=markup19())
    elif call.data == '70':
        points += 1
        bot.send_message(call.from_user.id, 'Питання 19:Концентрація уваги')
        bot.send_message(call.from_user.id,
                         '1.Мені легко сконцентруватися на тій чи іншій задачі.\n2. Останнім часом виникли деякі проблеми з концентрацією.\n3.Мені складно зосередитись на чомусь довше, ніж на кілька хвилин.\n4.Я виявив, що не можу сконцентруватися взагалі.',
                         reply_markup=markup19())
    if call.data == '71':
        points += 2
        bot.send_message(call.from_user.id, 'Питання 19:Концентрація уваги')
        bot.send_message(call.from_user.id,
                         '1.Мені легко сконцентруватися на тій чи іншій задачі.\n2. Останнім часом виникли деякі проблеми з концентрацією.\n3.Мені складно зосередитись на чомусь довше, ніж на кілька хвилин.\n4.Я виявив, що не можу сконцентруватися взагалі.',
                         reply_markup=markup19())
    elif call.data == '72':
        points += 3
        bot.send_message(call.from_user.id, 'Питання 19:Концентрація уваги')
        bot.send_message(call.from_user.id,
                         '1.Мені легко сконцентруватися на тій чи іншій задачі.\n2. Останнім часом виникли деякі проблеми з концентрацією.\n3.Мені складно зосередитись на чомусь довше, ніж на кілька хвилин.\n4.Я виявив, що не можу сконцентруватися взагалі.',
                         reply_markup=markup19())
    if call.data == '73':
        points += 0
        bot.send_message(call.from_user.id, 'Питання 20:Втома')
        bot.send_message(call.from_user.id,'1.Я втомлююсь так само, як завжди, нічого не змінилося.\n2.Я почав втомлюватися швидше, ніж зазвичай.\n3.Я ще впораюся, але все частіше ловлю себе на тому, що відмовляюся від деяких звичних справ (спорту, зустрічей із друзями, поїздок), тому що у мене просто немає на них сил.\n4.Здається, я навіть прокидаюся вже втомленим.',reply_markup=markup20())
    elif call.data == '74':
        points += 1
        bot.send_message(call.from_user.id, 'Питання 20:Втома')
        bot.send_message(call.from_user.id,
                         '1.Я втомлююсь так само, як завжди, нічого не змінилося.\n2.Я почав втомлюватися швидше, ніж зазвичай.\n3.Я ще впораюся, але все частіше ловлю себе на тому, що відмовляюся від деяких звичних справ (спорту, зустрічей із друзями, поїздок), тому що у мене просто немає на них сил.\n4.Здається, я навіть прокидаюся вже втомленим.',
                         reply_markup=markup20())
    if call.data == '75':
        points += 2
        bot.send_message(call.from_user.id, 'Питання 20:Втома')
        bot.send_message(call.from_user.id,
                         '1.Я втомлююсь так само, як завжди, нічого не змінилося.\n2.Я почав втомлюватися швидше, ніж зазвичай.\n3.Я ще впораюся, але все частіше ловлю себе на тому, що відмовляюся від деяких звичних справ (спорту, зустрічей із друзями, поїздок), тому що у мене просто немає на них сил.\n4.Здається, я навіть прокидаюся вже втомленим.',
                         reply_markup=markup20())
    elif call.data == '76':
        points += 3
        bot.send_message(call.from_user.id, 'Питання 20:Втома')
        bot.send_message(call.from_user.id,
                         '1.Я втомлююсь так само, як завжди, нічого не змінилося.\n2.Я почав втомлюватися швидше, ніж зазвичай.\n3.Я ще впораюся, але все частіше ловлю себе на тому, що відмовляюся від деяких звичних справ (спорту, зустрічей із друзями, поїздок), тому що у мене просто немає на них сил.\n4.Здається, я навіть прокидаюся вже втомленим.',
                         reply_markup=markup20())
    if call.data == '77':
        points += 0
        bot.send_message(call.from_user.id, 'Питання 21:Інтерес до сексу')
        bot.send_message(call.from_user.id,'1.Моє лібідо останнім часом не змінилося, все як завжди.\n2.Секс цікавить мене трохи менше, ніж раніше.\n3. Думаю про секс дуже рідко, він відійшов на десятий план.\n4.Я повністю втратив інтерес до інтиму.',reply_markup=markup21())
    elif call.data == '78':
        points += 1
        bot.send_message(call.from_user.id, 'Питання 21:Інтерес до сексу')
        bot.send_message(call.from_user.id,
                         '1.Моє лібідо останнім часом не змінилося, все як завжди.\n2.Секс цікавить мене трохи менше, ніж раніше.\n3. Думаю про секс дуже рідко, він відійшов на десятий план.\n4.Я повністю втратив інтерес до інтиму.',
                         reply_markup=markup21())
    if call.data == '79':
        points += 2
        bot.send_message(call.from_user.id, 'Питання 21:Інтерес до сексу')
        bot.send_message(call.from_user.id,
                         '1.Моє лібідо останнім часом не змінилося, все як завжди.\n2.Секс цікавить мене трохи менше, ніж раніше.\n3. Думаю про секс дуже рідко, він відійшов на десятий план.\n4.Я повністю втратив інтерес до інтиму.',
                         reply_markup=markup21())
    elif call.data == '80':
        points += 3
        bot.send_message(call.from_user.id, 'Питання 21:Інтерес до сексу')
        bot.send_message(call.from_user.id,
                         '1.Моє лібідо останнім часом не змінилося, все як завжди.\n2.Секс цікавить мене трохи менше, ніж раніше.\n3. Думаю про секс дуже рідко, він відійшов на десятий план.\n4.Я повністю втратив інтерес до інтиму.',
                         reply_markup=markup21())
    if call.data == '81':
        points += 0
        bot.send_message(call.from_user.id, 'Натисни або напиши "Результати!"')
    elif call.data == '82':
        points += 1
        bot.send_message(call.from_user.id, 'Натисни або напиши "Результати!"')
    if call.data == '83':
        points += 2
        bot.send_message(call.from_user.id, 'Натисни або напиши "Результати!"')
    elif call.data == '84':
        points += 3
        bot.send_message(call.from_user.id, 'Натисни або напиши "Результати!"')

bot.polling(none_stop=True)