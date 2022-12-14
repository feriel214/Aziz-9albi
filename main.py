from experta import *
from pywebio.input import *
from pywebio.output import *
import pygame
import time


class Aziz_Kalby(Fact):
    "Info sur Aziz Kalby"
    pass


class Azizy_decision(KnowledgeEngine):

    @Rule(
        Aziz_Kalby(أسمر_مسرار=True),
        Aziz_Kalby(عينيه_شهل_و_عندو_شلاغم=True),
        Aziz_Kalby(ضامر=False))
    def بالي_بيك(self):
        img = open('balybik.jpg', 'rb').read()
        put_table([
            [put_markdown(" # ممممممم `بالي بيك` لا مشا لا جاء ههه ❤️ ")],
            [put_image(img, width='500px', height='400px')],
        ])
        pygame.init()
        song = pygame.mixer.Sound("love.mp3")
        song.play()
        time.sleep(3)

    @Rule(
        Aziz_Kalby(مزيان=True),
        Aziz_Kalby(_عندو_جڨوارو_برشا_فلوس=True),
        Aziz_Kalby(عينيه_شهل_و_عندو_شلاغم=False))
    def سامي_فهري(self):
        img = open('semyfehry.jpg', 'rb').read()
        put_table([
            [put_markdown(" # هههه سامي الفهري ينجح 🎬")],
            [put_image(img, width='500px', height='400px')],
        ])
        pygame.init()
        song = pygame.mixer.Sound("love.mp3")
        song.play()
        time.sleep(3)
        #print("هههه سامي الفهري ينجح 🎬")
        # image = img.imread('semyfehry.jpg')
        # plt.imshow(image)
        # plt.show()

    @Rule(
        Aziz_Kalby(ضامر=True),
        Aziz_Kalby(طويل_أبيض=True),
        Aziz_Kalby(بدنو_مزيان=True),
        Aziz_Kalby(_عندو_جڨوارو_برشا_فلوس=False))
    def نضال_سعدي(self):
        img = open('nidhal.jpg', 'rb').read()
        put_table([
            [put_markdown(" # نضال السعدي 🫠💙💋 أما صوري عندو شكون 🤦‍♀️")],
            [put_image(img, width='500px', height='400px')],
        ])
        pygame.init()
        song = pygame.mixer.Sound("love.mp3")
        song.play()
        time.sleep(3)

    @Rule(
        Aziz_Kalby(ضحكتو_حلوة=True),
        Aziz_Kalby(شعرو_كورلي=True),
        Aziz_Kalby(ضامر=False))
    def فرجاني_ساسي(self):
        img = open('ferjenisassi.jpg', 'rb').read()
        put_table([
            [put_markdown(" # هاهاها فرجاني ساسي يواتيك اضرب عندك ⚽️")],
            [put_image(img, width='500px', height='400px')],
        ])
        pygame.init()
        song = pygame.mixer.Sound("love.mp3")
        song.play()
        time.sleep(3)

    @Rule(
        Aziz_Kalby(يعرف_يطيب=True),
        Aziz_Kalby(طويل_أبيض=True),
        Aziz_Kalby(أسمر_مسرار=False))
    def بوراك(self):
        img = open('bourak.jpg', 'rb').read()
        put_table([
            [put_markdown(
                " # هههه يا حلوفة تحبو يطيبلك أي للا تدلل  الشاف بوراك 👨‍🍳")],
            [put_image(img, width='500px', height='400px')],
        ])
        pygame.init()
        song = pygame.mixer.Sound("love.mp3")
        song.play()
        time.sleep(3)

    @Rule(
        Aziz_Kalby(ضحكتو_حلوة=True),
        Aziz_Kalby(طويل_أبيض=True),
        Aziz_Kalby(أسمر_مسرار=False))
    def ضافر_عابدين(self):
        img = open('dhafer.jpg', 'rb').read()
        put_table([
            [put_markdown(" # ظافر العابدين و يوفا الحب 🙈❤️")],
            [put_image(img, width='500px', height='400px')],
        ])
        pygame.init()
        song = pygame.mixer.Sound("love.mp3")
        song.play()
        time.sleep(3)

    @Rule(
        Aziz_Kalby(ضامر=True),
        Aziz_Kalby(أسمر_مسرار=True),
        Aziz_Kalby(طويل_أبيض=False))
    def دالي_تونسي(self):
        img = open('daly.jpg', 'rb').read()
        put_table([
            [put_markdown(" # جو جو جو محمد علي التونسي يهبل 💗")],
            [put_image(img, width='500px', height='400px')],
        ])
        pygame.init()
        song = pygame.mixer.Sound("love.mp3")
        song.play()
        time.sleep(3)

    @Rule(
        Aziz_Kalby(ضامر=True),
        Aziz_Kalby(مزيان=True),
        Aziz_Kalby(طويل_أبيض=False))
    def جعفور(self):
        img = open('jaafour.jpg', 'rb').read()
        put_table([
            [put_markdown(" # هههه جعفور يهني 🤡😂")],
            [put_image(img, width='500px', height='400px')],
        ])
        pygame.init()
        song = pygame.mixer.Sound("love.mp3")
        song.play()
        time.sleep(3)

    @Rule(
        Aziz_Kalby(طويل_أبيض=True),
        Aziz_Kalby(عينيه_شهل_و_عندو_شلاغم=True),
        Aziz_Kalby(أسمر_مسرار=False))
    def خالد_هويسة(self):
        img = open('khalouda.jpg', 'rb').read()
        put_table([
            [put_markdown(" # اقوى ممثل فيك يا تونس خالد هويسة 😍")],
            [put_image(img, width='500px', height='400px')],
        ])
        pygame.init()
        song = pygame.mixer.Sound("love.mp3")
        song.play()
        time.sleep(3)

    @Rule(
        Aziz_Kalby(أسمر_مسرار=True),
        Aziz_Kalby(شعرو_كورلي=True))
    def حنبعل(self):
        img = open('hanabal.jpg', 'rb').read()
        put_table([
            [put_markdown(" # محبوب الجماهير حنبعل المجبري زين و عين ♥️")],
            [put_image(img, width='500px', height='400px')],
        ])
        pygame.init()
        song = pygame.mixer.Sound("love.mp3")
        song.play()
        time.sleep(3)

    @Rule(
        Aziz_Kalby(أسمر_مسرار=True),
        Aziz_Kalby(عينيه_شهل_و_عندو_شلاغم=True),
        Aziz_Kalby(مزيان=True),
        Aziz_Kalby(_عندو_جڨوارو_برشا_فلوس=True),
        Aziz_Kalby(ضامر=True),
        Aziz_Kalby(طويل_أبيض=True),
        Aziz_Kalby(بدنو_مزيان=True),
        Aziz_Kalby(ضحكتو_حلوة=True),
        Aziz_Kalby(يعرف_يطيب=True),
        Aziz_Kalby(شعرو_كورلي=True))
    def حنبعل(self):
        img = open('citrou.jpg', 'rb').read()
        put_table([
            [put_markdown(
                " # هههه إلي يحسب وحدو يفضلو ، طلعتلك قرعة المرة هاذي 🎃😹")],
            [put_image(img, width='500px', height='400px')],
        ])
        pygame.init()
        song1 = pygame.mixer.Sound("lough.mp3")
        song1.play()
        time.sleep(4)


engine = Azizy_decision()
engine.reset()

m1 = False
m2 = False
m3 = False
m4 = False
m5 = False
m6 = False
m7 = False
m8 = False
m9 = False
m10 = False
img = open('aziz_kalbi.PNG', 'rb').read()
put_table([
    [put_markdown(
        " # مرحبا بيك ان شاء اللله فرحتك, أيا  `عروسة`, جاوب ب أي ولا لا يلاااا  ")],
    [put_image(img, width='500px', height='400px')],
])
test1 = input("أسمر_مسرار")
if test1 == "oui":
    m1 = True
test2 = input("عينيه_شهل_عندو_شلاغم ")
if test2 == "oui":
    m2 = True
test3 = input("مزيان ")
if test3 == "oui":
    m3 = True
test4 = input("_عندو_جڨوارو_برشا_فلوس ")
if test4 == "oui":
    m4 = True
test5 = input("ضامر ")
if test5 == "oui":
    m5 = True
test6 = input("طويل_أبيض ")
if test6 == "oui":
    m6 = True
test7 = input("بدنو_مزيان ")
if test7 == "oui":
    m7 = True
test8 = input("ضحكتو_حلوة ")
if test8 == "oui":
    m8 = True
test9 = input("شعرو_كورلي ")
if test9 == "oui":
    m9 = True
test10 = input("يعرف_يطيب ")
if test10 == "oui":
    m10 = True
put_markdown('# اووووووو..... لقينالك راجل زغرط هاي  💍👑👰💃 ')


def show_again():
    class Aziz_Kalby(Fact):
        "Info sur la voiture"
        pass

    class Azizy_decision(KnowledgeEngine):

        @Rule(
            Aziz_Kalby(أسمر_مسرار=True),
            Aziz_Kalby(عينيه_شهل_و_عندو_شلاغم=True),
            Aziz_Kalby(ضامر=False))
        def بالي_بيك(self):
            img = open('balybik.jpg', 'rb').read()
            put_table([
                [put_markdown(" # ممممممم `بالي بيك` لا مشا لا جاء ههه ❤️ ")],
                [put_image(img, width='500px', height='400px')],
            ])
            pygame.init()
            song = pygame.mixer.Sound("love.mp3")
            song.play()
            time.sleep(3)

        @Rule(
            Aziz_Kalby(مزيان=True),
            Aziz_Kalby(_عندو_جڨوارو_برشا_فلوس=True),
            Aziz_Kalby(عينيه_شهل_و_عندو_شلاغم=False))
        def سامي_فهري(self):
            img = open('semyfehry.jpg', 'rb').read()
            put_table([
                [put_markdown(" # هههه سامي الفهري ينجح 🎬")],
                [put_image(img, width='500px', height='400px')],
            ])
            pygame.init()
            song = pygame.mixer.Sound("love.mp3")
            song.play()
            time.sleep(3)
            # print("هههه سامي الفهري ينجح 🎬")
            # image = img.imread('semyfehry.jpg')
            # plt.imshow(image)
            # plt.show()

        @Rule(
            Aziz_Kalby(ضامر=True),
            Aziz_Kalby(طويل_أبيض=True),
            Aziz_Kalby(بدنو_مزيان=True),
            Aziz_Kalby(_عندو_جڨوارو_برشا_فلوس=False))
        def نضال_سعدي(self):
            img = open('nidhal.jpg', 'rb').read()
            put_table([
                [put_markdown(" # نضال السعدي 🫠💙💋 أما صوري عندو شكون 🤦‍♀️")],
                [put_image(img, width='500px', height='400px')],
            ])
            pygame.init()
            song = pygame.mixer.Sound("love.mp3")
            song.play()
            time.sleep(3)

        @Rule(
            Aziz_Kalby(ضحكتو_حلوة=True),
            Aziz_Kalby(شعرو_كورلي=True),
            Aziz_Kalby(ضامر=False))
        def فرجاني_ساسي(self):
            img = open('ferjenisassi.jpg', 'rb').read()
            put_table([
                [put_markdown(" # هاهاها فرجاني ساسي يواتيك اضرب عندك ⚽️")],
                [put_image(img, width='500px', height='400px')],
            ])
            pygame.init()
            song = pygame.mixer.Sound("love.mp3")
            song.play()
            time.sleep(3)

        @Rule(
            Aziz_Kalby(يعرف_يطيب=True),
            Aziz_Kalby(طويل_أبيض=True),
            Aziz_Kalby(أسمر_مسرار=False))
        def بوراك(self):
            img = open('bourak.jpg', 'rb').read()
            put_table([
                [put_markdown(
                    " # هههه يا حلوفة تحبو يطيبلك أي للا تدلل  الشاف بوراك 👨‍🍳")],
                [put_image(img, width='500px', height='400px')],
            ])
            pygame.init()
            song = pygame.mixer.Sound("love.mp3")
            song.play()
            time.sleep(3)

        @Rule(
            Aziz_Kalby(ضحكتو_حلوة=True),
            Aziz_Kalby(طويل_أبيض=True),
            Aziz_Kalby(أسمر_مسرار=False))
        def ضافر_عابدين(self):
            img = open('dhafer.jpg', 'rb').read()
            put_table([
                [put_markdown(" # ظافر العابدين و يوفا الحب 🙈❤️")],
                [put_image(img, width='500px', height='400px')],
            ])
            pygame.init()
            song = pygame.mixer.Sound("love.mp3")
            song.play()
            time.sleep(3)

        @Rule(
            Aziz_Kalby(ضامر=True),
            Aziz_Kalby(أسمر_مسرار=True),
            Aziz_Kalby(طويل_أبيض=False))
        def دالي_تونسي(self):
            img = open('daly.jpg', 'rb').read()
            put_table([
                [put_markdown(" # جو جو جو محمد علي التونسي يهبل 💗")],
                [put_image(img, width='500px', height='400px')],
            ])
            pygame.init()
            song = pygame.mixer.Sound("love.mp3")
            song.play()
            time.sleep(3)

        @Rule(
            Aziz_Kalby(ضامر=True),
            Aziz_Kalby(مزيان=True),
            Aziz_Kalby(طويل_أبيض=False))
        def جعفور(self):
            img = open('jaafour.jpg', 'rb').read()
            put_table([
                [put_markdown(" # هههه جعفور يهني 🤡😂")],
                [put_image(img, width='500px', height='400px')],
            ])
            pygame.init()
            song = pygame.mixer.Sound("love.mp3")
            song.play()
            time.sleep(3)

        @Rule(
            Aziz_Kalby(طويل_أبيض=True),
            Aziz_Kalby(عينيه_شهل_و_عندو_شلاغم=True),
            Aziz_Kalby(أسمر_مسرار=False))
        def خالد_هويسة(self):
            img = open('khalouda.jpg', 'rb').read()
            put_table([
                [put_markdown(" # اقوى ممثل فيك يا تونس خالد هويسة 😍")],
                [put_image(img, width='500px', height='400px')],
            ])
            pygame.init()
            song = pygame.mixer.Sound("love.mp3")
            song.play()
            time.sleep(3)

        @Rule(
            Aziz_Kalby(أسمر_مسرار=True),
            Aziz_Kalby(شعرو_كورلي=True))
        def حنبعل(self):
            img = open('hanabal.jpg', 'rb').read()
            put_table([
                [put_markdown(" # محبوب الجماهير حنبعل المجبري زين و عين ♥️")],
                [put_image(img, width='500px', height='400px')],
            ])
            pygame.init()
            song = pygame.mixer.Sound("love.mp3")
            song.play()
            time.sleep(3)

        @Rule(
            Aziz_Kalby(أسمر_مسرار=True),
            Aziz_Kalby(عينيه_شهل_و_عندو_شلاغم=True),
            Aziz_Kalby(مزيان=True),
            Aziz_Kalby(_عندو_جڨوارو_برشا_فلوس=True),
            Aziz_Kalby(ضامر=True),
            Aziz_Kalby(طويل_أبيض=True),
            Aziz_Kalby(بدنو_مزيان=True),
            Aziz_Kalby(ضحكتو_حلوة=True),
            Aziz_Kalby(يعرف_يطيب=True),
            Aziz_Kalby(شعرو_كورلي=True))
        def حنبعل(self):
            img = open('citrou.jpg', 'rb').read()
            put_table([
                [put_markdown(
                    " # هههه إلي يحسب وحدو يفضلو ، طلعتلك قرعة المرة هاذي 🎃😹")],
                [put_image(img, width='500px', height='400px')],
            ])
            pygame.init()
            song1 = pygame.mixer.Sound("lough.mp3")
            song1.play()
            time.sleep(3)

    engine = Azizy_decision()
    engine.reset()

    m1 = False
    m2 = False
    m3 = False
    m4 = False
    m5 = False
    m6 = False
    m7 = False
    m8 = False
    m9 = False
    m10 = False
    img = open('aziz_kalbi.PNG', 'rb').read()
    put_table([
        [put_markdown(
            " # مرحبا بيك ان شاء اللله فرحتك, أيا  `عروسة`, جاوب ب أي ولا لا يلاااا  ")],
        [put_image(img, width='500px', height='400px')],
    ])
    test1 = input("أسمر_مسرار")
    if test1 == "oui":
        m1 = True
    test2 = input("عينيه_شهل_عندو_شلاغم ")
    if test2 == "oui":
        m2 = True
    test3 = input("مزيان ")
    if test3 == "oui":
        m3 = True
    test4 = input("_عندو_جڨوارو_برشا_فلوس ")
    if test4 == "oui":
        m4 = True
    test5 = input("ضامر ")
    if test5 == "oui":
        m5 = True
    test6 = input("طويل_أبيض ")
    if test6 == "oui":
        m6 = True
    test7 = input("بدنو_مزيان ")
    if test7 == "oui":
        m7 = True
    test8 = input("ضحكتو_حلوة ")
    if test8 == "oui":
        m8 = True
    test9 = input("شعرو_كورلي ")
    if test9 == "oui":
        m9 = True
    test10 = input("يعرف_يطيب ")
    if test10 == "oui":
        m10 = True
    put_markdown('# اووووووو..... لقينالك راجل زغرط هاي  💍👑👰💃 ')
    engine.declare(Aziz_Kalby(أسمر_مسرار=m1,
                              عينيه_شهل_و_عندو_شلاغم=m2,
                              مزيان=m3,
                              _عندو_جڨوارو_برشا_فلوس=m4,
                              ضامر=m5,
                              طويل_أبيض=m6,
                              بدنو_مزيان=m7,
                              ضحكتو_حلوة=m8,
                              شعرو_كورلي=m9,
                              يعرف_يطيب=m10
                              ))
    engine.run()
    put_button("عجبتني،نعاودوها 😍", onclick=lambda: show_again(),
               color='info', outline=True)


engine.declare(Aziz_Kalby(أسمر_مسرار=m1,
                          عينيه_شهل_و_عندو_شلاغم=m2,
                          مزيان=m3,
                          _عندو_جڨوارو_برشا_فلوس=m4,
                          ضامر=m5,
                          طويل_أبيض=m6,
                          بدنو_مزيان=m7,
                          ضحكتو_حلوة=m8,
                          شعرو_كورلي=m9,
                          يعرف_يطيب=m10
                          ))
engine.run()
put_button("عجبتني،نعاودوها 😍", onclick=lambda: show_again(),
           small=None, color='info', outline=True)
