from globals import *
from itertools import cycle

class Text:

    text_list = []
    text_redrawn = False
    text_in_progress = False
    blink_event = pygame.USEREVENT + 0
    pygame.time.set_timer(blink_event, 414)
    blinky = cycle(["■", " "])
    next_blink = next(blinky)
    show_tooltip = False
    text_timer = 0
    current_tooltip = None
    text_cursor = 0
    blank_text = FONT.render("", True, TERMINALGREEN)

    def __init__(self, text, x, y) -> None:
        self.text = text
        self.img = FONT.render("", True, TERMINALGREEN)
        self.x = x
        self.y = y
        self.next_update = 0
        self.typing_speed = 10 # Default: 10
        self.text_cursor = 0
        self.blank_text = FONT.render("", True, TERMINALGREEN)
        self.header_txt = FONT.render(None, False, TERMINALGREEN)
        Text.text_list.append(self)
        self.printed = False
        self.is_tooltip = True

    @classmethod
    def draw_tooltip(cls, tooltip):
        cls.current_tooltip = tooltip
        cls.current_tooltip.text_cursor = 0
        cls.text_timer = 5 # Tooltip timer
        if cls.text_timer <= 0:
            cls.current_tooltip.text_cursor = 0

    @classmethod
    def tooltip_listener(cls, delta):
        if cls.current_tooltip is not None:
            if cls.text_timer <= 0:
                cls.show_tooltip = False
                if cls.current_tooltip is not None:
                    cls.current_tooltip.text_cursor = 0
            else:
                cls.show_tooltip = True
                cls.text_timer -= delta
    
    def draw_text(self):
        clock = pygame.time.get_ticks()
        if self.is_tooltip is True:
            SCREEN.blit(self.blank_text, (self.x, self.y))
        else:
            SCREEN.blit(self.blank_text, (self.x, self.y))

        if (clock > self.next_update):
            self.next_update = clock + self.typing_speed
            if (self.text_cursor < len(self.text)):
                self.text_cursor += 1
                self.blank_text = FONT.render(self.text[0:self.text_cursor], False, TERMINALGREEN)
            else:
                self.printed = True

    def draw_text_instant(self):
        img = FONT.render(self.text, True, TERMINALGREEN)
        SCREEN.blit(img, (self.x, self.y))

    def draw_tooltip_text(self):
        clock = pygame.time.get_ticks()
        SCREEN.blit(self.blank_text, (self.x, self.y))
        if (clock > self.next_update):
            self.next_update = clock + self.typing_speed
            if (self.text_cursor < len(self.text)):
                self.text_cursor += 1
                self.blank_text = FONT.render(self.text[0:self.text_cursor] + Text.next_blink, False, TERMINALGREEN)
                SCREEN.blit(self.blank_text, (indent, X))
            else:
                self.printed = True

    @classmethod
    def blink_square(cls):
        if cls.show_tooltip == False:
            img = FONT.render("> " + cls.next_blink, True, TERMINALGREEN)
        else:
            if cls.current_tooltip is not None:
                img = FONT.render(cls.current_tooltip.text + cls.next_blink, True, TERMINALGREEN)
        SCREEN.blit(img, (indent, X))

    @classmethod
    def terminal_info(cls):
        robco_inc.draw_text_instant()
        copyright.draw_text_instant()
        server.draw_text_instant()

    @classmethod
    def header(cls):
        header.draw_text_instant()
        line.draw_text_instant()

    @classmethod
    def header_mt(cls):
        line_mt.draw_text_instant()
        for i in header_mt:
            i.draw_text_instant()
    
    @classmethod
    def draw_text_list(cls, list):
        Text.text_in_progress = True
        for i in list:
            if len(list) >= 1:
                list[0].draw_text()
                if len(list) >= 2 and list[0].text_cursor == len(list[0].text):
                    list[1].draw_text()
                    if len(list) >= 3 and list[1].text_cursor == len(list[1].text):
                        list[2].draw_text()
                        if len(list) >= 4 and list[2].text_cursor == len(list[2].text):
                            list[3].draw_text()
                            if len(list) >= 5 and list[3].text_cursor == len(list[3].text):
                                list[4].draw_text()
                                if len(list) >= 6 and list[4].text_cursor == len(list[4].text):
                                    list[5].draw_text()
                                    if len(list) >= 7 and list[5].text_cursor == len(list[5].text):
                                        list[6].draw_text()
                                        if len(list) >= 8 and list[6].text_cursor == len(list[6].text):
                                            list[7].draw_text()
                                            if len(list) >= 9 and list[7].text_cursor == len(list[7].text):
                                                list[8].draw_text()
                                                if len(list) >= 10 and list[8].text_cursor == len(list[8].text):
                                                    list[9].draw_text()
                                                    if len(list) >= 11 and list[9].text_cursor == len(list[9].text):
                                                        list[10].draw_text()
                                                        if len(list) >= 12 and list[10].text_cursor == len(list[10].text):
                                                            list[11].draw_text()
                                                            if len(list) >= 13 and list[11].text_cursor == len(list[11].text):
                                                                list[12].draw_text()
                                                                if len(list) >= 14 and list[12].text_cursor == len(list[12].text):
                                                                    list[13].draw_text()
                                                                    if len(list) >= 15 and list[13].text_cursor == len(list[13].text):
                                                                        list[14].draw_text()
                                                                        if len(list) >= 16 and list[14].text_cursor == len(list[14].text):
                                                                            list[15].draw_text()

        if list[-1].text_cursor == len(list[-1].text):
            Text.text_in_progress = False
            Text.text_redrawn = False

    @classmethod
    def redraw(cls):
        for i in cls.text_list:
            i.text_cursor = 0
            i.blank_text = FONT.render("", True, TERMINALGREEN)
            cls.text_redrawn = True


#-=Terminal Info=-#
robco_inc = Text("ROBCO INDUSTRIES UNIFIED OPERATING SYSTEM", indent+28+200, 25)
copyright = Text("COPYRIGHT 2075-2077 ROBCO INDUSTRIES", indent+65+200, 50)
server = Text("-Server 4-", indent+261+200, 75)

#-=Header=-#
header = Text("Царство Грелока (бета v.632)", indent, HEADER)
h_mt = Text("(Горный склон)", indent, HEADER)
h_mt_II = Text("Грелок ждет вас, сыпля богохульными", indent, HEADER+25)
h_mt_III = Text("ругательствами.", indent, HEADER+50)
header_mt = [h_mt, h_mt_II, h_mt_III]
line = Text("—" * 28, indent, LINE)
line_mt = Text("—" * 35, indent, LINE+50)

#-=Tooltips=-#
look_around = Text("> Вы осматриваетесь...", indent, X)
heading_north = Text("> Вы идете на север...", indent, X)
venture_north = Text("> Вы отправляетесь на север...", indent, X)
heading_south = Text("> Вы идете на юг....", indent, X)
retreating_south = Text("> Вы удаляетесь на юг....", indent, X)
heading_east = Text("> Вы идете на восток...", indent, X)
heading_west = Text("> Вы идете на запад...", indent, X)
debug = Text("> Debug Info", indent, X)

#-=Inventory Tooltips=-#
rusty_sword_inv = Text("> Ваше оружие. Ржавое, но бравое.", indent, X)
flask_inv = Text("> Маленькая фляжка, которую можно наполнить водой.", indent, X)
flask_blessed_inv = Text("> Ваша фляжка наполнена освященной водой.", indent, X)
zombie_head_inv = Text("> Этот запах не добавляет вам популярности...", indent, X)
refined_gemstone_inv = Text("> Великолепно ограненный драгоценный камень", indent, X)
magical_shard_inv = Text("> Драгоценный кристалл пульсирует светом...", indent, X)
magic_sword_inv = Text("> Зачарованное оружие должно убить Грелока", indent, X)
brass_key_inv = Text("> Ключ, переданный вам священником", indent, X)
raw_gem_inv = Text("> Этот драгоценный камень может пригодиться...", indent, X)


#-=Plains=-#
p_I = Text("Вы стоите на широкой равнине. Холмы", indent, TI)
p_II = Text("простираются к северу, где сгустившиеся", indent, TII)
p_III = Text("тучи клубятся вокруг зловещего пика.", indent, TIII)
p_IV = Text("Грунтовая дорога, идущая от одинокой", indent, TIV)
p_V = Text("церквушки на востоке, вьется по равнине, на", indent, TV)
p_VI = Text("которой вы находитесь, и приводит к", indent, TVI)
p_VII = Text("многолюдному городу на юге. Туманы", indent, TVII)
p_VIII = Text("клубятся над болотом на западе, там", indent, TVIII)
p_IX = Text("виднеется одинокая башня.", indent, TIX)
plains_text = [p_I, p_II, p_III, p_IV, p_V, p_VI, p_VII, p_VIII, p_IX]


#-=Town=-#
t_I = Text("Вы стоите на пыльной рыночной площади", indent, TI)
t_II = Text("тихого городка. Многие лавки и жилые дома", indent, TII)
t_III = Text("заброшены, а редкие прохожие", indent, TIII)
t_IV = Text("разговаривают шепотом, с опаской", indent, TIV)
t_V = Text("поглядывая на темнеющее на севере небо.", indent, TV)
t_VI = Text("Тишина разрывается лишь мерным", indent, TVI)
t_VII = Text("постукиванием молота по наковальне - в", indent, TVII)
t_VIII = Text("шатре неподалеку склонился над работой", indent, TVIII)
t_IX = Text("усатый кузнец.", indent, TIX)
# t_X = Text("", indent, TX)
t_XI = Text("Кузнец работает.", indent, TXI)
# t_XII = Text("", indent, TXII)
t_XIII = Text("Вы видите и священника неподалеку. Он", indent, TXIII)
t_XIV = Text("пьет.", indent, TXIV)
town_text = [t_I, t_II, t_III, t_IV, t_V, t_VI, t_VII, t_VIII, t_IX, t_XI, t_XIII, t_XIV]

#-=Smithy=-#
smithy_t = Text("> Вы подходите к кузнице...", indent, X)
sm_I = Text("Ваши глаза слезятся от дыма и липкого жара,", indent, TI)
sm_II = Text("наполняющих шатер. Человек-громадина", indent, TII)
sm_III = Text("вытирает пот с лысой головы и глядит на вас,", indent, TIII)
sm_IV = Text("не отрываясь от работы.", indent, TIV)
# sm_V = Text("", indent, TV)
sm_VI = Text('"Работы невпроворот теперь, из-за Грелока', indent, TVI)
sm_VII = Text("все до смерти напуганы. Мне нужно", indent, TVII)
sm_VIII = Text("выполнить заказы. Оставь меня,", indent, TVIII)
sm_IX = Text('незнакомец", - кузнец гонит вас из шатра, а', indent, TIX)
sm_X = Text("сам окунает раскаленную сталь в кадку с", indent, TX)
sm_XI = Text("водой, откуда с шипением вырывается", indent, TXI)
sm_XII = Text("облако пара.", indent, TXII)
smithy_a_dialogue = [sm_I, sm_II, sm_III, sm_IV, sm_VI, sm_VII, sm_VIII, sm_IX, sm_X, sm_XI, sm_XII]
#-=Part II=-#
sm_b_I = Text("Кузнец не привечает вас и собирается уже", indent, TI)
sm_b_II = Text("отослать прочь, когда вы достаете из сумки", indent, TII)
sm_b_III = Text("сверкающий драгоценный камень. Оружейник", indent, TIII)
sm_b_IV = Text("откладывает свой молот и крутит ус.", indent, TIV)
# sm_b_V = Text("", indent, TV)
sm_b_VI = Text('"Прекрасный камень, это так, - говорит он, с', indent, TVI)
sm_b_VII = Text("восхищением глядя на игру граней. - Что же", indent, TVII)
sm_b_VIII = Text('тебе нужно?"', indent, TVIII)
# sm_b_IX = Text("", indent, TIX)
sm_b_X = Text("Следуя подробным указаниям, кузнец", indent, TX)
sm_b_XI = Text("перековывает ваш ржавый меч и вставляет", indent, TXI)
sm_b_XII = Text("волшебный кристалл в середину лезвия.", indent, TXII)
smithy_b_dialogue = [sm_b_I, sm_b_II, sm_b_III, sm_b_IV, sm_b_VI, sm_b_VII, sm_b_VIII, sm_b_X, sm_b_XI, sm_b_XII]

#-=Priest=-#
priest_t = Text("> Вы подходите к духовному лицу...", indent, X)
pr_I = Text("Священник замечает ваше приближение и", indent, TI)
pr_II = Text("смотрит на вас поверх своей кружки.", indent, TII)
pr_III = Text('"Грелок идет, Бог нас оставил!" кричит он и', indent, TIII)
pr_IV = Text("тут же громко рыгает - его тошнит.", indent, TIV)
# pr_V = Text("", indent, TV)
pr_VI = Text("Задыхаясь от перегара, исходящего от", indent, TVI)
pr_VII = Text("собеседника, вы узнаете, что священник", indent, TVII)
pr_VIII = Text("бежал из расположенной неподалеку", indent, TVIII)
pr_IX = Text("часовни, где служил. Когда Грелок", indent, TIX)
pr_X = Text("обЪявился на горе, начали оживать", indent, TX)
pr_XI = Text("мертвецы на кладбище и прихожане", indent, TXI)
pr_XII = Text("перестали приходить в церковь.", indent, TXII)
# pr_XIII = Text("", indent, TXIII)
pr_XIV = Text('"Если ты избавишь часовню от зомби, -', indent, TXIV)
pr_XV = Text("говорит он, - я дам тебе ключ и ты сможешь", indent, TXV)
pr_XVI = Text('зайти в снадобницу".', indent, TXVI)
priest_a_dialogue = [pr_I, pr_II, pr_III, pr_IV, pr_VI, pr_VII, pr_VIII, pr_IX, pr_X, pr_XI, pr_XII, pr_XIV, pr_XV, pr_XVI]

#-=Priest Quest Completed=-#
pr_b_I = Text("Священник заплетающимся языком клянет", indent, TI)
pr_b_II = Text("зомби, осквернивших церковь. Вы", indent, TII)
pr_b_III = Text("открываете сумку и показываете ему", indent, TIII)
pr_b_IV = Text("отрезанную голову зомби.", indent, TIV)
# pr_b_V = Text("", indent, TV)
pr_b_VI = Text('"Хвала тебе! - говорит он, икая. Возможно,', indent, TVI)
pr_b_VII = Text('сила Грелока не так и велика!" С этими', indent, TVII)
pr_b_VIII = Text("словами он переворачивает графин и", indent, TVIII)
pr_b_IX = Text("швыряет его в камин, где тот взрывается", indent, TIX)
pr_b_X = Text("фиолетовым пламенем и тут же сгорает.", indent, TX)
# pr_b_XI = Text("", indent, TXI)
pr_b_XII = Text('"Я должен собрать правоверных, - он сует', indent, TXII)
pr_b_XIII = Text("медный ключ вам в руку. - Пожалуйста,", indent, TXIII)
pr_b_XIV = Text("возьми из моей часовни то, что сможет тебе", indent, TXIV)
pr_b_XV = Text('пригодиться".', indent, TXV)
pr_b_dialogue = [pr_b_I, pr_b_II, pr_b_III, pr_b_IV, pr_b_VI, pr_b_VII, pr_b_VIII, pr_b_IX, pr_b_X, pr_b_XII, pr_b_XIII, pr_b_XIV, pr_b_XV]

#-=Priest Final Dialogue=-#
pr_c_I = Text("Священник пьет воду, внимательно изучая", indent, TI)
pr_c_II = Text("увесистый фолиант в тисненом переплете,", indent, TII)
pr_c_III = Text("подвешенный на шею на толстом кожаном", indent, TIII)
pr_c_IV = Text("ремне. Он замечает вас только тогда, когда", indent, TIV)
pr_c_V = Text("вы подходите вплотную.", indent, TV)
# pr_c_VI = Text("", indent, TVI)
pr_c_VII = Text('"А, добрый друг! Открыл ли ты часовню? Я все', indent, TVII)
pr_c_VIII = Text("еще страдаю от последствий пьянства,", indent, TVIII)
pr_c_IX = Text("боюсь. Но скоро я соберу свой приход и сам", indent, TIX)
pr_c_X = Text('вернусь туда".', indent, TX)
pr_c_text = [pr_c_I, pr_c_II, pr_c_III, pr_c_IV, pr_c_V, pr_c_VII, pr_c_VIII, pr_c_IX, pr_c_X]


#-=Chapel=-#
c_I = Text("Вы стоите в конце грунтовой дороги, перед", indent, TI)
c_II = Text("вами маленькая часовня. Штукатурка", indent, TII)
c_III = Text("облезла, а в черепичной крыше зияют дыры.", indent, TIII)
c_IV = Text("Огромные дубовые двери заперты. Нигде не", indent, TIV)
c_V = Text("видно ни священника, ни прихожан.", indent, TV)
c_VI = Text("Потрескавшийся шпиль отбрасывает тень на", indent, TVI)
c_VII = Text("небольшое кладбище с покосившимися", indent, TVII)
c_VIII = Text("могильными плитами. Грунтовая дорога", indent, TVIII)
c_IX = Text("уходит на запад, идя по бескрайней", indent, TIX)
c_X = Text("равнине.", indent, TX)
# c_XI = Text("", indent, TXI)
c_XII = Text("Неподалеку бродит туда-сюда зомби.", indent, TXII)
c_XII_alt = Text("Двери часовни не заперты.", indent, TXII)
# c_XIII = Text("", indent, TXIII)
c_XIV = Text("Рядом вы видите открытую могилу.", indent, TXIV)
chapel_text = [c_I, c_II, c_III, c_IV, c_V, c_VI, c_VII, c_VIII, c_IX, c_X, c_XII, c_XIV]
#-=Grave=-#
grave_t = Text("> Ваш удар опрокидывает зомби в открытую могилу.", indent, X)
grave_t_II = Text("> Вы вглядываетесь в открытую могилу...", indent, X)
g_I = Text("На кладбище вы видите глубокую пустую", indent, TI)
g_II = Text("могилу. В отвратительной луже на её дне", indent, TII)
g_III = Text("плавают несколько опухших крыс.", indent, TIII)
g_III_alt = Text("плавают несколько опухших крыс и труп", indent, TIII)
g_IV = Text("Не упадите туда!", indent, TIV)
g_IV_alt = Text("зомби. Не упадите туда!", indent, TIV)
g_VI = Text("Гротескная голова зомби застряла в корнях", indent, TVI)
g_VII = Text("рядом с поверхностью земли. Вы кладёте", indent, TVII)
g_VIII = Text("голову в сумку в доказательство ваших", indent, TVIII)
g_VIX = Text("деяний.", indent, TIX)
grave_text = [g_I, g_II, g_III, g_IV]
grave_text_II = [g_VI, g_VII, g_VIII, g_VIX]
#-=Chapel inside=-#
chapel_t = Text("> Вы заходите в безлюдную часовню...", indent, X)
ch_I = Text("В проходящих сквозь высокие окна часовни", indent, TI)
ch_II = Text("окрашенных лучах света пляшут пылинки.", indent, TII)
ch_III = Text("Скамьи, кафедра проповедника и все", indent, TIII)
ch_IV = Text("остальное словно тонет в тумане. У входа", indent, TIV)
ch_V = Text("стоит глубокая чаша, до краев полна", indent, TV)
ch_VI = Text("освященной водой.", indent, TVI)
ch_VIII = Text("Воды здесь более чем достаточно, чтобы", indent, TVIII)
ch_IX = Text("заполнить вашу маленькую фляжку.", indent, TIX)
ch_text = [ch_I, ch_II, ch_III, ch_IV, ch_V, ch_VI, ch_VIII, ch_IX]


#-=Swamp=-#
bog_I = Text("Вы стоите на узкой каменной тропе, вокруг", indent, TI)
bog_II = Text("темное болото. Скальные пузыри всплывают", indent, TII)
bog_III = Text("на поверхность окружающей вас топи и тихо", indent, TIII)
bog_IV = Text("лопаются, обдавая ноги грязной слизью.", indent, TIV)
bog_V = Text("Стоящая перед вами невысокая каменная", indent, TV)
bog_VI = Text("башня будто клонится к земле. Двери не", indent, TVI)
bog_VII = Text("видно, а каменные стены гладкие, словно", indent, TVII)
bog_VIII = Text("полированные. Облик башни оживляет", indent, TVIII)
bog_IX = Text("балкон, расположенный примерно на", indent, TIX)
bog_X = Text("половине высоты строения. Пьянящий запах", indent, TX)
bog_XI = Text("фимиама смешивается с удушливым", indent, TXI)
bog_XII = Text("зловонием трясины. Каменная тропа", indent, TXII)
bog_XIII = Text("поворачивает на восток к широкой равнине", indent, TXIII)
bog_XIV = Text("за болотами.", indent, TXIV)
bog_I_b = Text("На балконе стоит волшебник и отчаянно", indent, TI)
bog_II_b = Text("жестикулирует.", indent, TII)
bog_text = [bog_I, bog_II, bog_III, bog_IV, bog_V, bog_VI, bog_VII, bog_VIII, bog_IX, bog_X, bog_XI, bog_XII, bog_XIII, bog_XIV]
bog_text_b = [bog_I_b, bog_II_b]

#-=Wizard Dialogue A=-#
wizard_t = Text("> Вы обращаетесь к волшебнику...", indent, X)
wizard_a_I = Text("Волшебник на балконе энергично машет вам", indent, TI)
wizard_a_II = Text('рукой. "Вы здесь, вы прибыли!" - восклицает он.', indent, TII)
wizard_a_III = Text("Возникает неловкая пауза, затем он с силой", indent, TIII)
wizard_a_IV = Text("тычет пальцем в хрустальный шар, чуть не", indent, TIV)
wizard_a_V = Text("скинув его в трясину.", indent, TV)
# wizard_a_VI = Text("", indent, TVI)
wizard_a_VII = Text('"Я видел, вы понимаете. Вы - тот, кому', indent, TVII)
wizard_a_VIII = Text("уготовано победить Грелока. Эге-гей! -", indent, TVIII)
wizard_a_IX = Text('Маленький человечек вспрыгивает на ограждение', indent, TIX)
wizard_a_X = Text('балкона, делая пируэт. - Пришло время мне', indent, TX)
wizard_a_XI = Text("выполнить свою роль. Бросьте мне драгоценный", indent, TXI)
wizard_a_XII = Text("камень!", indent, TXII)
# wizard_a_XIII = Text("", indent, TXIII)
wizard_a_XIV = Text('Волшебник морщит лоб: "Немного не в том', indent, TXIV)
wizard_a_XV = Text('порядке, так получается?', indent, TXV)
wizard_a_dialogue = [wizard_a_I, wizard_a_II, wizard_a_III, wizard_a_IV, wizard_a_V, wizard_a_VII, wizard_a_VIII, wizard_a_IX, wizard_a_X, wizard_a_XI, wizard_a_XII, wizard_a_XIV, wizard_a_XV]
#-=Part II=-#
wizard_aII_I = Text("Возвращайтесь, когда у вас будет", indent, TI)
wizard_aII_II = Text("могущественный драгоценный камень.", indent, TII)
wizard_aII_III = Text('И поскорее - мне никогда раньше не доводилось', indent, TIII)
wizard_aII_IV = Text('участвовать в выполнении пророчества!"', indent, TIV)
wizard_aII_dialogue = [wizard_aII_I, wizard_aII_II, wizard_aII_III, wizard_aII_IV]

#-=Wizard Dialogue B=-#
wizard_b_I = Text("Волшебник торопит вас, его рукава хлопают, как крылья:", indent, TI)
wizard_b_II = Text('"Идите! Найдите камень и возвращайтесь,', indent, TII)
wizard_b_III = Text('тогда я смогу сыграть свою роль!"', indent, TIII)
wizard_b_dialogue = [wizard_b_I, wizard_b_II, wizard_b_III]

#-=Wizard Dialogue C=-#
wizard_c_I = Text('"Эге-гей! Приближается убийца Грелока, и', indent, TI)
wizard_c_II = Text('камень в его руке - все, как я видел!" -', indent, TII)
wizard_c_III = Text("Остроконечная шляпа волшебника энергично", indent, TIII)
wizard_c_IV = Text("кивает вам, когда он указывает на вас", indent, TIV)
wizard_c_V = Text("пальцем. Неожиданно из пальца вырывается", indent, TV)
wizard_c_VI = Text("бледно-оранжевая световая дуга и, прежде", indent, TVI)
wizard_c_VII = Text("чем вы успеваете среагировать,", indent, TVII)
wizard_c_VIII = Text("захватывает камень из вашей сумки. Камень,", indent, TVIII)
wizard_c_IX = Text("покачиваясь, зависает  перед носом", indent, TIX)
wizard_c_X = Text("волшебника.", indent, TX)
# wizard_c_XI = Text("", indent, TXI)
wizard_c_XII = Text('"Сущность откройся, сила приди,', indent, TXII)
wizard_c_XIII = Text('форти-ди-ди!" - волшебник шлепает по', indent, TXIII)
wizard_c_XIV = Text("висящему в воздухе камню, отбрасывая его к", indent, TXIV)
wizard_c_XV = Text("гладкой стене башни. Вспышка света, камень", indent, TXV)
wizard_c_dialogue = [wizard_c_I, wizard_c_II, wizard_c_III, wizard_c_IV, wizard_c_V, wizard_c_VI, wizard_c_VII, wizard_c_VIII, wizard_c_IX, wizard_c_X, wizard_c_XII, wizard_c_XIII, wizard_c_XIV, wizard_c_XV]
#-=Part II=-#
wizard_cII_I = Text(" разбивается надвое, и обе части аккуратно", indent, TI)
wizard_cII_II = Text("приземляются в ладошки, подставленные", indent, TII)
wizard_cII_III = Text("подпрыгивающим волшебником.", indent, TIII)
# wizard_cII_IV = Text("", indent, TIV)
wizard_cII_V = Text('"Кристалл для меча. Вставьте его в железо, и', indent, TV)
wizard_cII_VI = Text("он найдет путь к черному сердцу Грелока.", indent, TVI)
wizard_cII_VII = Text("Возьмите остаток тоже. Вам понадобится", indent, TVII)
wizard_cII_VIII = Text('заплатить кузнецу за ковку меча". Он', indent, TVIII)
wizard_cII_IX = Text("кидает оба камня вниз, вы делаете шаг", indent, TIX)
wizard_cII_X = Text("вперед и ловите их.", indent, TX)
wizard_cII_dialogue = [wizard_cII_I, wizard_cII_II, wizard_cII_III, wizard_cII_V, wizard_cII_VI, wizard_cII_VII, wizard_cII_VIII, wizard_cII_IX, wizard_cII_X]

#-=Wizard Dialogue D=-#
wizard_d_I = Text('"Идите к кузнецу! Вставьте кристалл в меч и', indent, TI)
wizard_d_II = Text('одержите победу над Грелоком!" Волшебник', indent, TII)
wizard_d_III = Text("швыряет в вас несколько мелких камушков,", indent, TIII)
wizard_d_IV = Text("чтобы прогнать побыстрее, и скрывается в", indent, TIV)
wizard_d_V = Text("клубах разноцветного дыма.", indent, TV)
wizard_d_dialogue = [wizard_d_I, wizard_d_II, wizard_d_III, wizard_d_IV, wizard_d_V]


#-=Mountainside=-#
grelok_t = Text("> Ваше жалкое оружие бесполезно против Грелока.", indent, X)
raw_gem_t = Text("> Вы поднимаете необработанный драгоценный камень.", indent, X)
mt_I = Text("Вы стоите на скалистой, открытой ветрам", indent, TIII)
mt_II = Text("площадке на вершине горы. Тучи клубятся", indent, TIV)
mt_III = Text("над вами, поливая вас и редкую", indent, TV)
mt_IV = Text("растительность вокруг обильным дождем.", indent, TVI)
mt_V = Text("Много ниже, под горой, вплоть до горизонта", indent, TVII)
mt_VI = Text("простирается широкая равнина.", indent, TVIII)
# mt_VII = Text("", indent, TVIX)
mt_VIII = Text("Грелок ждет вас, сыпля богохульными", indent, TX)
mt_IX = Text("ругательствами.", indent, TXI)
# mt_X = Text("", indent, TXII)
mt_XI = Text("Ваш взгляд улавливает проблеск между", indent, TXIII)
mt_XII = Text("камнями.", indent, TXIV)
mt_text = [mt_I, mt_II, mt_III, mt_IV, mt_V, mt_VI, mt_VIII, mt_IX, mt_XI, mt_XII]

#-=Grelok Defeated=-#
grelok_defeated_a_I = Text("Вы обнажаете меч, Грелок наклоняет свою", indent, TIII)
grelok_defeated_a_II = Text("огромную, украшенную рогами голову и", indent, TIV)
grelok_defeated_a_III = Text("разражается хохотом. Вы стискиваете зубы", indent, TV)
grelok_defeated_a_IV = Text("и с размаха наносите могучий удар двумя", indent, TVI)
grelok_defeated_a_V = Text("руками, магическое лезвие пронзительно", indent, TVII)
grelok_defeated_a_VI = Text("звенит, и звук ясно слышен даже сквозь", indent, TVIII)
grelok_defeated_a_VII = Text("хриплый гогот монстра.", indent, TIX)
# grelok_defeated_a_VIII = Text("", indent, TX)
grelok_defeated_a_IX = Text("Вы бьете мечом с такой силой, что он", indent, TXI)
grelok_defeated_a_X = Text("вырывается из рук и летит прямо в разинутую", indent, TXII)
grelok_defeated_a_XI = Text("пасть чудовища, скрываясь из вида во тьме", indent, TXIII)
grelok_defeated_a_XII = Text("его глотки. Вы делаете шаг назад, когда", indent, TXIV)
grelok_defeated_a_XIII = Text("Грелок судорожно дергается, обрывая смех,", indent, TXV)
# grelok_defeated_a_XIV = Text("", indent, TXVI)
# grelok_defeated_a_XV = Text("", indent, TXVII)
grelok_defeated_a_text = [grelok_defeated_a_I, grelok_defeated_a_II, grelok_defeated_a_III, grelok_defeated_a_IV, grelok_defeated_a_V, grelok_defeated_a_VI, grelok_defeated_a_VII, grelok_defeated_a_IX, grelok_defeated_a_X, grelok_defeated_a_XI, grelok_defeated_a_XII, grelok_defeated_a_XIII]
#-=Part II=-#
grelok_defeated_b_I = Text(" и встает прямо. Еще момент, и он начинает", indent, TIII)
grelok_defeated_b_II = Text("хвататься за шею. Слышен приглушенный", indent, TIV)
grelok_defeated_b_III = Text("звон, идущий будто издалека.", indent, TV)
# grelok_defeated_b_IV = Text("", indent, TVI)
grelok_defeated_b_V = Text("Внезапно грудь Грелока взрывается", indent, TVII)
grelok_defeated_b_VI = Text("фонтаном вязкой зеленой жидкости. Звон", indent, TVIII)
grelok_defeated_b_VII = Text("слышен теперь ясно, и в то время, как из-под", indent, TIX)
grelok_defeated_b_VIII = Text("глубоко вгрызшегося в тело монстра острия", indent, TX)
grelok_defeated_b_IX = Text("магического меча льется густая кровь,", indent, TXI)
grelok_defeated_b_X = Text("тучи, окутывавшие пик, рассеиваются.", indent, TXII)
grelok_defeated_b_XI = Text("Грелок побежден!", indent, TXIII)
# grelok_defeated_b_XII = Text("", indent, TXIV)
grelok_defeated_b_XIII = Text("          КОНЕЦ", indent, TXV)
grelok_defeated_b_XIV = Text("   (Спасибо за игру!)", indent, TXVI)
# grelok_defeated_b_XV = Text("", indent, TXVII)
grelok_defeated_b_text = [grelok_defeated_b_I, grelok_defeated_b_II, grelok_defeated_b_III, grelok_defeated_b_V, grelok_defeated_b_VI, grelok_defeated_b_VII, grelok_defeated_b_VIII, grelok_defeated_b_IX, grelok_defeated_b_X, grelok_defeated_b_XI, grelok_defeated_b_XIII, grelok_defeated_b_XIV]
