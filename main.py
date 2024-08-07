from globals import *
from button import *
from music import *
from text import *

class Game:
    def __init__(self):
        pygame.display.set_caption(VERSION)
        pygame.display.set_icon(ICON)
        self.clock = pygame.time.Clock()
        self.running = True
        self.background_music_volume = 0.3
        self.background_music = Music(self.background_music_volume)
        self.channel1 = pygame.mixer.Channel(1)
        self.channel1.set_volume(.1)
        self.channel1.play(TERMINALHUM, -1)
        pygame.mixer.Sound.play(TERMINAL_FORWARD)
        self.channel2 = pygame.mixer.Channel(2)
        self.x = 1
        self.y = 1
        self.current_location = map[self.y][self.x]
        self.last_location = None
        self.inventory = [rusty_sword, flask, back]
        self.inventory_slot = len(self.inventory)
        self.inventoryOpen = False
        self.previous_time = time.time()
        self.delta_time = time.time() - self.previous_time
        self.fps_counter = False
        self.textDisplayed = False
        self.scroll_sound_timer = 0
        self.button_held_timer = 0
        self.blacksmith_dialogue = False
        self.priest_dialogue = False
        self.grave_text = False
        self.inside_chapel = False
        self.priest_current_dialogue = priest_a_dialogue
        self.smithy_current_dialogue = smithy_a_dialogue
        self.wizard_dialogue = False
        self.wizard_met = False
        self.wizard_current_dialogue = wizard_a_dialogue
        self.wizard_current_dialogue_next_page = wizard_aII_dialogue
        self.text_first_page = None
        self.text_second_page = None
        self.show_next_page = False
        pygame.mouse.set_visible(False)


    def run(self):
        while self.running:
            self.draw()
            self.update()
        self.close()

    def powerdown(self):
        fadeout = pygame.Surface((SCREENWIDTH, SCREENHEIGHT))
        fadeout = fadeout.convert()
        fadeout.fill("black")
        self.current_location = None
        self.inventoryOpen = False
        self.textDisplayed = False
        self.channel1.fadeout(500)
        pygame.mixer.music.fadeout(500)
        pygame.mixer.Sound.play(TERMINAL_POWERDOWN)
        self.cursor_img_rect = (0, 720)

        for i in range(255):
            fadeout.set_alpha(i)
            SCREEN.blit(fadeout, (0, 0))
            pygame.display.update()
        self.running = False

    def update(self):
        global lookAroundTown, lookAroundChapel, lookAroundMountainside, lookAroundSwamp, zombieSlain, priestQuest, brassKey, rawGemstone, defeatGrelok, wizardQuest, clicked, LANGUAGE, ROOT_INDEX, TOWN_INDEX, CHAPEL_INDEX, SWAMP_INDEX, MOUNTAINSIDE_INDEX, LOCATION, FULLSCREEN, SCREEN
        self.delta_time = time.time() - self.previous_time
        self.previous_time = time.time()
        pressed_key = pygame.key.get_pressed()
        Text.tooltip_listener(self.delta_time)
        Text.terminal_info()
        Text.blink_square()
        self.cursor_img_rect = pygame.mouse.get_pos()

        if self.textDisplayed == False:
            if pressed_key[K_UP]:
                if Button.index >= 1:
                    LOCATION[Button.index].kb_clicked = False
                    if Button.kb_input is True and self.button_held_timer == 0:
                        Button.index -= 1
                    Button.kb_input_on()
                    self.button_held_timer += self.delta_time
                    if self.button_held_timer >= 0.4:
                        Button.index -= 1
                        self.button_held_timer = 0.37
                    Button.kb_highlighted_button = LOCATION[Button.index]
                    LOCATION[Button.index].kb_clicked = True
                else:
                    Button.kb_input_on()
                    Button.kb_highlighted_button = LOCATION[Button.index]
                    LOCATION[Button.index].kb_clicked = True

            if pressed_key[K_DOWN]:
                if Button.index < len(LOCATION) -1:
                    LOCATION[Button.index].kb_clicked = False
                    if Button.kb_input is True and self.button_held_timer == 0:
                        Button.index += 1
                    Button.kb_input_on()
                    self.button_held_timer += self.delta_time
                    if self.button_held_timer >= 0.4:
                        Button.index += 1
                        self.button_held_timer = 0.37
                    Button.kb_highlighted_button = LOCATION[Button.index]
                    LOCATION[Button.index].kb_clicked = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.powerdown()

            if event.type == Text.blink_event:
                Text.next_blink = next(Text.blinky)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    Button.kb_input_off()
                    LOCATION[Button.index].kb_clicked = False

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if self.textDisplayed:
                        if self.show_next_page:
                            pygame.mixer.Sound.play(SELECT)
                            self.show_next_page = False
                        else:
                            pygame.mixer.Sound.play(SELECT)
                            self.textDisplayed = False
                            self.current_location = self.last_location
                            Text.redraw()
                    else:
                        if self.show_next_page:
                            self.show_next_page = False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if self.textDisplayed:
                        if self.show_next_page:
                            pygame.mixer.Sound.play(SELECT)
                            self.show_next_page = False
                        else:
                            pygame.mixer.Sound.play(SELECT)
                            self.textDisplayed = False
                            self.current_location = self.last_location
                            Text.redraw()
                            if Button.kb_input is True:
                                LOCATION[Button.index].kb_clicked = True
                    else:
                        if self.show_next_page:
                            self.show_next_page = False
                        Button.current_button.clicked = True

                elif event.key == pygame.K_m:
                    Music.pause()

                elif event.key == pygame.K_EQUALS:
                    Text.draw_tooltip(debug)
                    if self.background_music_volume + 0.05 <= 1:
                        debug.text = f"> Music volume: [{round(self.background_music_volume, 1)}]"
                        self.background_music_volume += 0.05
                        pygame.mixer.music.set_volume(self.background_music_volume)
                    else:
                        debug.text = f"> Music volume: [MAX]"
                        self.background_music_volume = 1
                        pygame.mixer.music.set_volume(1)

                elif event.key == pygame.K_MINUS:
                    Text.draw_tooltip(debug)
                    if self.background_music_volume - 0.05 >= 0:
                        debug.text = f"> Music volume: [{round(self.background_music_volume, 1)}]"
                        self.background_music_volume -= 0.05
                        pygame.mixer.music.set_volume(self.background_music_volume)
                    else:
                        debug.text = f"> Music volume: [OFF]"
                        self.background_music_volume = 0
                        pygame.mixer.music.set_volume(0)

                elif event.key == pygame.K_ESCAPE:
                    self.powerdown()

                elif event.key == pygame.K_l:
                    Text.draw_tooltip(debug)
                    if TEXT_SCROLL_SOUND.get_volume() == 0:
                        debug.text = "> Text scroll sound: [ON]"
                        TEXT_SCROLL_SOUND.set_volume(1)
                    else:
                        debug.text = "> Text scroll sound: [OFF]"
                        TEXT_SCROLL_SOUND.set_volume(0)

                elif event.key == pygame.K_n:
                    debug.text = f"> Loading track: [{self.background_music.track}]"
                    Text.draw_tooltip(debug)
                    self.background_music.track = (self.background_music.track+1) % len(self.background_music.tracks)
                    pygame.mixer.music.load(self.background_music.tracks[self.background_music.track]) 
                    pygame.mixer.music.play()  

                elif event.key == pygame.K_b:
                    Text.draw_tooltip(debug)
                    if SELECT.get_volume() == 0:
                        debug.text = "> Button sound: [ON]"
                        SELECT.set_volume(0.1)
                        SELECT_II.set_volume(0.1)
                    else:
                        debug.text = "> Button sound: [OFF]"
                        SELECT.set_volume(0)
                        SELECT_II.set_volume(0)

                elif event.key == pygame.K_h:
                    Text.draw_tooltip(debug)
                    if HOVER.get_volume() == 0:
                        debug.text = "> Button hover sound: [ON]"
                        HOVER.set_volume(0.1)
                    else:
                        debug.text = "> Button hover sound: [OFF]"
                        HOVER.set_volume(0)

                elif event.key == pygame.K_t:
                    Text.draw_tooltip(debug)
                    if TERMINALHUM.get_volume() == 0:
                        debug.text = "> Terminal hum: [ON]"
                        TERMINALHUM.set_volume(1)
                    else:
                        debug.text = "> Terminal hum: [OFF]"
                        TERMINALHUM.set_volume(0)

                elif event.key == pygame.K_w:
                    Text.draw_tooltip(debug)
                    if FULLSCREEN:
                        debug.text = "> Display mode: [WINDOWED]"
                        FULLSCREEN = False
                        SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
                    else:
                        debug.text = "> Display mode: [FULLSCREEN]"
                        FULLSCREEN = True
                        SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT), pygame.FULLSCREEN)

                elif event.key == pygame.K_f:
                    if self.fps_counter:
                        self.fps_counter = False
                    else:
                        self.fps_counter = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.button_held_timer = 0
                if event.key == pygame.K_DOWN:
                    self.button_held_timer = 0

            elif event.type == self.background_music.track_end:
                self.background_music.track = (self.background_music.track+1) % len(self.background_music.tracks)
                pygame.mixer.music.load(self.background_music.tracks[self.background_music.track]) 
                pygame.mixer.music.play()

###-=Plains=-###
        if self.current_location == "plains":
            LOCATION = plains
            self.move()
            Text.header()
            if inventory.y is not VI:
                inventory.y = VI
            if north.y is not II:
                north.y = II
            self.draw_list(plains)
            
            if pI.action:
                if defeatGrelok:
                    self.powerdown()
                else:
                    Text.draw_tooltip(look_around)
                    self.display_text()

            if north.action:
                Text.draw_tooltip(venture_north)
                self.change_location(mountainside, MOUNTAINSIDE_INDEX)
                self.go_north()

            if south.action:
                if lookAroundTown is True:
                    north.y = IV
                Text.draw_tooltip(heading_south)
                self.change_location(town, TOWN_INDEX)
                self.go_south()
                south.kb_clicked = False

            if east.action:
                if brass_key in self.inventory:
                    c_west.y = II
                self.change_location(chapel, CHAPEL_INDEX)
                self.go_east()

            if west.action:
                self.change_location(swamp, SWAMP_INDEX)
                self.go_west()

            if inventory.action:
                self.open_inventory()
###-=Town=-###
        if self.current_location == "town":
            LOCATION = town
            self.move()
            self.draw_list(town)
            Text.header()

            if lookAroundTown is True:
                inventory.y = V
                north.y = IV
            else:
                inventory.y = III

            if tI.action:
                self.display_text()
                self.blacksmith_dialogue = False
                self.priest_dialogue = False
                if lookAroundTown == False:
                    town.insert(1, smith)
                    town.insert(2, priest)
                    Text.draw_tooltip(look_around)
                    lookAroundTown = True

            if north.action:
                self.change_location(plains, ROOT_INDEX)
                self.go_north()
                Text.draw_tooltip(heading_north)

            if smith.action:
                self.priest_dialogue = False
                self.blacksmith_dialogue = True
                Text.draw_tooltip(smithy_t)
                self.display_text()
                if magical_shard in self.inventory:
                    self.smithy_current_dialogue = smithy_b_dialogue
                    self.inventory.remove(rusty_sword)
                    self.inventory.remove(refined_gemstone)
                    self.inventory.remove(magical_shard)
                    flask.y = I
                    flask_blessed.y = I
                    grelok.text = "> Ударить грелока магическим мечом"
                    if brass_key in self.inventory:
                        self.inventory.insert(1, magic_sword)
                        brass_key.y = III
                    elif zombie_head in self.inventory:
                        self.inventory.insert(2, magic_sword)
                        zombie_head.y = II
                        magic_sword.y = III
                    else:
                        self.inventory.insert(1, magic_sword)
                else:
                    self.smithy_current_dialogue = smithy_a_dialogue

            if priest.action:
                self.blacksmith_dialogue = False
                self.priest_dialogue = True
                Text.draw_tooltip(priest_t)
                self.display_text()
                if priestQuest is True:
                    if zombie_head in self.inventory:
                        self.inventory.remove(zombie_head)
                        chapel_text.insert(10, c_XII_alt)
                        c_XIV.y = TXIV
                        if raw_gemstone in self.inventory:
                            self.inventory.insert(2, brass_key)
                            brass_key.y = III
                            raw_gemstone.y = IV
                        elif refined_gemstone in self.inventory:
                            self.inventory.insert(4, brass_key)
                            refined_gemstone.y = III
                            magical_shard.y = IV
                            brass_key.y = V
                        elif magic_sword in self.inventory:
                            self.inventory.insert(2, brass_key)
                            magic_sword.y = II
                        else:
                            self.inventory.insert(2, brass_key)
                        brassKey = True
                        lookAroundChapel = False
                        chapel.remove(grave)
                        if Button.kb_input is True:
                            CHAPEL_INDEX = 1
                    else:
                        self.priest_current_dialogue = pr_c_text

            if inventory.action:
                self.open_inventory()
###-=Chapel=-###
        if self.current_location == "chapel":
            LOCATION = chapel
            self.move()
            self.draw_list(chapel)
            Text.header()

            if lookAroundChapel is True and brassKey is True:
                inventory.y = IV
                c_west.y = III
            elif brass_key in self.inventory:
                inventory.y = III
                c_west.y = II
            elif lookAroundChapel is True and zombieSlain is True:
                inventory.y = IV
                c_west.y = III
            elif lookAroundChapel is True:
                inventory.y = V
                c_west.y = IV
            else:
                inventory.y = III
                c_west.y = II

            if cI.action:
                Text.draw_tooltip(look_around)
                self.display_text()
                self.grave_text = False
                self.inside_chapel = False
                if lookAroundChapel == False and zombieSlain is True:
                    chapel.insert(1, c_chapel)
                    lookAroundChapel = True
                if lookAroundChapel == False and zombieSlain == False:
                    chapel.insert(1, zombie)
                    chapel.insert(2, grave)
                    lookAroundChapel = True

            if c_west.action:
                self.change_location(plains, ROOT_INDEX)
                self.go_west()

            if zombie.action:
                if zombieSlain == False:
                    chapel_text.remove(c_XII)
                    grave_text.remove(g_III)
                    grave_text.remove(g_IV)
                    grave_text.append(g_III_alt)
                    grave_text.append(g_IV_alt)
                    for i in grave_text_II:
                        grave_text.append(i)
                    c_XIV.y = TXII
                    grave.y = II
                    Text.draw_tooltip(grave_t)
                    zombieSlain = True
                    self.priest_current_dialogue = pr_b_dialogue
                    Button.remove_button(LOCATION, chapel, zombie)

            if grave.action:
                self.inside_chapel = False
                self.grave_text = True
                Text.draw_tooltip(grave_t_II)
                self.display_text()
                if priestQuest is True:
                    grave_text.remove(g_VI)
                    grave_text.remove(g_VII)
                    grave_text.remove(g_VIII)
                    grave_text.remove(g_VIX)
                else:
                    if magic_sword not in self.inventory:
                        self.inventory.insert(2, zombie_head)
                    if raw_gemstone in self.inventory:
                        raw_gemstone.y = IV
                    elif refined_gemstone in self.inventory:
                        refined_gemstone.y = IV
                        magical_shard.y = V
                    elif magic_sword in self.inventory:
                        self.inventory.insert(1, zombie_head)
                        magic_sword.y = III
                        zombie_head.y = II
                    priestQuest = True

            if c_chapel.action:
                self.inside_chapel = True
                Text.draw_tooltip(chapel_t)
                self.display_text()
                if brass_key in self.inventory and flask in self.inventory:
                    self.inventory.remove(flask)
                    if magic_sword in self.inventory:
                        self.inventory.insert(0, flask_blessed)
                    else:
                        self.inventory.insert(1, flask_blessed)

            if inventory.action:
                self.open_inventory()
###-=Swamp=-###
        if self.current_location == "swamp":
            LOCATION = swamp
            self.move()
            self.draw_list(swamp)
            Text.header()

            if lookAroundSwamp is True:
                inventory.y = IV
                s_east.y = III
            else:
                inventory.y = III

            if sI.action:
                Text.draw_tooltip(look_around)
                self.wizard_dialogue = False
                self.display_text()
                self.show_next_page = True
                if lookAroundSwamp == False:
                    swamp.insert(1, wizard)
                    lookAroundSwamp = True

            if wizard.action:
                Text.draw_tooltip(wizard_t)
                self.wizard_dialogue = True
                self.display_text()
                if rawGemstone is True:
                    if raw_gemstone in self.inventory:
                        self.show_next_page = True
                        self.wizard_current_dialogue = wizard_c_dialogue
                        self.wizard_current_dialogue_next_page = wizard_cII_dialogue
                        self.inventory.remove(raw_gemstone)
                        if brass_key in self.inventory:
                            self.inventory.insert(2, refined_gemstone)
                            self.inventory.insert(3, magical_shard)
                            brass_key.y = V
                        elif zombie_head in self.inventory:
                            self.inventory.insert(3, refined_gemstone)
                            self.inventory.insert(4, magical_shard)
                            refined_gemstone.y = IV
                            magical_shard.y = V
                        else:
                            self.inventory.insert(2, refined_gemstone)
                            self.inventory.insert(3, magical_shard)
                    else:
                        self.wizard_current_dialogue_next_page = wizard_d_dialogue
                else:
                    if self.wizard_met:
                        self.show_next_page = False
                        self.wizard_current_dialogue = wizard_b_dialogue
                        self.wizard_current_dialogue_next_page = wizard_b_dialogue
                    else:
                        self.show_next_page = True
                        self.wizard_current_dialogue = wizard_a_dialogue
                        self.wizard_current_dialogue_next_page = wizard_aII_dialogue
                    self.wizard_met = True

            if s_east.action:
                self.change_location(plains, ROOT_INDEX)
                self.go_east()

            if inventory.action:
                self.open_inventory()
###-=Mountainside=-###
        if self.current_location == "mountainside":
            LOCATION = mountainside
            self.move()
            self.draw_list(mountainside)
            Text.header_mt()

            if lookAroundMountainside is True and rawGemstone is True:
                m_south.y = IV
                inventory.y = V
            elif lookAroundMountainside is True:
                m_south.y = V
                inventory.y = VI
            else:
                inventory.y = IV

            if mI.action:
                Text.draw_tooltip(look_around)
                if defeatGrelok:
                    look_around.text = "> Спасибо за игру!"
                    self.change_location(plains, ROOT_INDEX)
                    self.go_south()
                else:
                    self.display_text()
                    if lookAroundMountainside == False:
                        mountainside.insert(1, grelok)
                        mountainside.insert(2, gemstone)
                        lookAroundMountainside = True

            if grelok.action:
                if magic_sword in self.inventory:
                    defeatGrelok = True
                    self.show_next_page = True
                    self.text_first_page = grelok_defeated_a_text
                    self.text_second_page = grelok_defeated_b_text
                    self.display_text()
                    Button.index = 0
                    ROOT_INDEX = 0
                    grelok.action = False
                    north.action = False
                    mountainside.clear()
                    plains.clear()
                    mI.text = "> ПОБЕДА!"
                    pI.text = "> Игра закончена"
                    mountainside.append(mI)
                    plains.append(pI)
                else:
                    Text.draw_tooltip(grelok_t)
                    if Button.kb_input is True:
                        LOCATION[Button.index].kb_clicked = True

            if gemstone.action:
                if rawGemstone == False:
                    Text.draw_tooltip(raw_gem_t)
                    if brass_key in self.inventory:
                        self.inventory.insert(3, raw_gemstone)
                        raw_gemstone.y = IV
                    elif zombie_head in self.inventory:
                        self.inventory.insert(3, raw_gemstone)
                        raw_gemstone.y = IV
                    else:
                        self.inventory.insert(2, raw_gemstone)
                    rawGemstone = True
                    mt_text.remove(mt_XI)
                    mt_text.remove(mt_XII)
                    Button.remove_button(LOCATION, mountainside, gemstone)

            if m_south.action:
                self.change_location(plains, ROOT_INDEX)
                self.go_south()
                Text.draw_tooltip(retreating_south)

            if inventory.action:
                self.open_inventory()
###-=Inventory=-###
        if self.inventoryOpen is True:
            LOCATION = self.inventory
            if self.last_location == "mountainside":
                Text.header_mt()
            else:
                Text.header()
            self.draw_list(self.inventory)

            if rusty_sword.action:
                Text.draw_tooltip(rusty_sword_inv)
            if flask.action:
                Text.draw_tooltip(flask_inv)
            if flask_blessed.action:
                Text.draw_tooltip(flask_blessed_inv)
            if zombie_head.action:
                Text.draw_tooltip(zombie_head_inv)
            if refined_gemstone.action:
                Text.draw_tooltip(refined_gemstone_inv)
            if magical_shard.action:
                Text.draw_tooltip(magical_shard_inv)
            if magic_sword.action:
                Text.draw_tooltip(magic_sword_inv)
            if brass_key.action:
                Text.draw_tooltip(brass_key_inv)
            if raw_gemstone.action:
                Text.draw_tooltip(raw_gem_inv)
        
            if back.action:
                if Button.kb_input is True:
                    back.kb_clicked = False
                    if self.last_location == "plains":
                        self.change_location(plains, ROOT_INDEX)
                    elif self.last_location == "town":
                        self.change_location(town, TOWN_INDEX)
                    elif self.last_location == "chapel":
                        self.change_location(chapel, CHAPEL_INDEX)
                    elif self.last_location == "swamp":
                        self.change_location(swamp, SWAMP_INDEX)
                    elif self.last_location == "mountainside":
                        self.change_location(mountainside, MOUNTAINSIDE_INDEX)
                    else:
                        Button.reset_index()
                self.close_inventory()
                Button.close_inventory()
                self.current_location = self.last_location
###-=Text=-###
        if self.textDisplayed is True:
            self.scroll_sound_timer -= self.delta_time
            if self.scroll_sound_timer <= 0 and Text.text_in_progress is True:
                self.channel2.set_volume(.1)
                self.channel2.play(TEXT_SCROLL_SOUND)
                self.scroll_sound_timer = 0.75
            if self.last_location != "mountainside":
                Text.header()
            else:
                Text.header_mt()

            if self.last_location == "plains":
                Text.draw_text_list(plains_text)

            elif self.last_location == "town":
                if self.blacksmith_dialogue is True:
                    Text.draw_text_list(self.smithy_current_dialogue)
                elif self.priest_dialogue is True:
                    Text.draw_text_list(self.priest_current_dialogue)
                else:
                    Text.draw_text_list(town_text)

            elif self.last_location == "chapel":
                if self.grave_text is True:
                    Text.draw_text_list(grave_text)
                elif self.inside_chapel is True:
                    Text.draw_text_list(ch_text)
                else:
                    Text.draw_text_list(chapel_text)

            elif self.last_location == "mountainside":
                if defeatGrelok:
                    if self.show_next_page:
                        Text.draw_text_list(grelok_defeated_a_text)
                    else:
                        Text.draw_text_list(grelok_defeated_b_text)
                else:
                    Text.draw_text_list(mt_text)

            elif self.last_location == "swamp":
                if self.wizard_dialogue is True:
                    if self.show_next_page:
                        Text.draw_text_list(self.wizard_current_dialogue)
                    else:
                        Text.draw_text_list(self.wizard_current_dialogue_next_page)
                else:
                    if self.show_next_page:
                        Text.draw_text_list(bog_text)
                    else:
                        Text.draw_text_list(bog_text_b)
        else:
            if Text.text_redrawn == False:
                Text.redraw()

        if self.cursor_img_rect is not None:
            SCREEN.blit(CURSOR, self.cursor_img_rect)

        if self.fps_counter:
            self.show_fps(SCREEN)

        pygame.display.update()
        self.clock.tick(FPS)

    def move(self):
        self.current_location = map[self.y][self.x]

    def draw_list(self, list):
        for button in list:
            button.draw_button()

    def draw(self):
        SCREEN.blit(BACKGROUND, BACKGROUND.get_rect())

    def change_location(self, destination, location_index):
        self.location_index_check()
        Button.index = location_index
        if Button.kb_input is True:
            destination[Button.index].kb_clicked = True

    def go_north(self):
        if self.y > 0:
            self.y -= 1
            self.move()

    def go_south(self):
        if self.y < map_y_len:
            self.y += 1
            self.move()

    def go_east(self):
        if self.x < map_x_len:
            Text.draw_tooltip(heading_east)
            self.x += 1
            self.move()

    def go_west(self):
        if self.x > 0:
            Text.draw_tooltip(heading_west)
            self.x -= 1
            self.move()

    def open_inventory(self):
        self.location_index_check()
        Button.index = 0
        Button.open_inventory()
        self.inventory_slot = len(self.inventory)

        if self.inventory_slot == 3:
            back.y = III
        elif self.inventory_slot == 4:
            back.y = IV
        elif self.inventory_slot == 5:
            back.y = V
        elif self.inventory_slot == 6:
            back.y = VI
        elif self.inventory_slot == 7:
            back.y = VII

        if self.current_location == "mountainside":
            for i in self.inventory:
                i.y += 50

        if Button.kb_input is True:
            self.inventory[Button.index].kb_clicked = True

        self.inventoryOpen = True
        self.last_location = self.current_location
        self.current_location = ""

    def close_inventory(self):
        if self.last_location == "mountainside":
            for i in self.inventory:
                i.y -= 50
        self.inventoryOpen = False 

    def location_index_check(self):
        global ROOT_INDEX, TOWN_INDEX, CHAPEL_INDEX, SWAMP_INDEX, MOUNTAINSIDE_INDEX
        if self.current_location == "plains":
            ROOT_INDEX = Button.index
        elif self.current_location == "town":
            TOWN_INDEX = Button.index
        elif self.current_location == "chapel":
            CHAPEL_INDEX = Button.index
        elif self.current_location == "swamp":
            SWAMP_INDEX = Button.index
        elif self.current_location == "mountainside":
            MOUNTAINSIDE_INDEX = Button.index

    def display_text(self):
        self.textDisplayed = True
        self.last_location = self.current_location
        self.current_location = ""

    def show_fps(self, display):
        global FONT, TERMINALGREEN
        self.text = FONT.render(str(round(self.clock.get_fps())), False, (TERMINALGREEN))
        display.blit(self.text, (1230, 10))

    def close(self):
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Game()
    game.run()
