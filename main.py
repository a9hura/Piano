import pygame
import piano_lists as pl # импортируем данные из piano_lists
from pygame import mixer

pygame.init()
pygame.mixer.set_num_channels(50) # Максимальное количество каналов воспроизведения звука

# Шрифты
l_font = pygame.font.Font('assets/TildaSans-ExtraBold.ttf', 48)
m_font = pygame.font.Font('assets/TildaSans-ExtraBold.ttf', 28)
s_font = pygame.font.Font('assets/TildaSans-ExtraBold.ttf', 16)
xs_font = pygame.font.Font('assets/TildaSans-ExtraBold.ttf', 10)

fps = 60
timer = pygame.time.Clock()
WIDTH = 52 * 35
HEIGHT = 400
screen = pygame.display.set_mode([WIDTH, HEIGHT])

white_sounds, black_sounds = [], [] # массивы с загруженными звуками
active_whites, active_blacks = [], [] # массивы, отвечающие за отображение нажатых клавиш

left_oct = 4 # начальное положение левой руки
right_oct = 5 # начальное положение правой руки

left_hand = pl.left_hand
right_hand = pl.right_hand
piano_notes = pl.piano_notes
white_notes = pl.white_notes
black_notes = pl.black_notes
black_labels = pl.black_labels # для отображения текста на черных клавишах

# Загружаем все звуки для мгновенного воспроизведения
for i in range(len(white_notes)):
    white_sounds.append(mixer.Sound(f'assets\\notes\\{white_notes[i]}.wav'))

for i in range(len(black_notes)):
    black_sounds.append(mixer.Sound(f'assets\\notes\\{black_notes[i]}.wav'))

pygame.display.set_caption("Симулятор пианино")


def draw_piano(whites, blacks):
    white_rects = []
    for i in range(52):
        # Белая клавиша
        rect = pygame.draw.rect(screen, 'white', [i * 35, HEIGHT - 300, 35, 300], 0, 4)
        white_rects.append(rect)
        # Черная рамка клавиши
        pygame.draw.rect(screen, 'black', [i * 35, HEIGHT - 300, 35, 300], 1, 4)
        # Названия нот на белых клавишах
        key_name = s_font.render(white_notes[i], True, 'black')
        screen.blit(key_name, (i * 35 + 3, HEIGHT - 20))

    skip_count = 0
    last_skip = 2
    skip_track = 2
    black_rects = []

    for i in range(36):
        rect = pygame.draw.rect(screen, 'black', [23 + (i * 35) + (skip_count * 35), HEIGHT - 300, 24, 200], 0, 5)
        # Алгоритм отрисовки нажатия на черную клавишу
        for j in range(len(blacks)):
            if blacks[j][0] == i:
                if blacks[j][1] > 0:
                    pygame.draw.rect(screen, 'green', [23 + (i * 35) + (skip_count * 35), HEIGHT - 300, 24, 200], 2, 5)
                    blacks[j][1] -= 1

        key_name = xs_font.render(black_labels[i], True, 'white')
        screen.blit(key_name, (25 + (i * 35) + (skip_count * 35), HEIGHT - 120))
        black_rects.append(rect)

        # Алгоритм для правильного расположения черных клавиш
        skip_track += 1
        if last_skip == 2 and skip_track == 3:
            last_skip = 3
            skip_track = 0
            skip_count += 1
        elif last_skip == 3 and skip_track == 2:
            last_skip = 2
            skip_track = 0
            skip_count += 1
    # Алгоритм отрисовки нажатия на белую клавишу
    for i in range(len(whites)):
        if whites[i][1] > 0:
            j = whites[i][0]
            pygame.draw.rect(screen, 'green', [j * 35, HEIGHT - 100, 35, 100], 2, 5)
            whites[i][1] -= 1

    return white_rects, black_rects, whites, blacks

# Функция для отображения рабочей октавы
def draw_hands(rightOct, leftOct, rightHand, leftHand):
    # Левая рука
    pygame.draw.rect(screen, 'dark gray', [(leftOct * 245) - 175, HEIGHT - 60, 245, 30], 0, 4)
    pygame.draw.rect(screen, 'black', [(leftOct * 245) - 175, HEIGHT - 60, 245, 30], 2, 4)

    text = s_font.render(leftHand[0], True, 'white')
    screen.blit(text, ((leftOct * 245) - 162, HEIGHT - 55))
    text = s_font.render(leftHand[2], True, 'white')
    screen.blit(text, ((leftOct * 245) - 128, HEIGHT - 55))
    text = s_font.render(leftHand[4], True, 'white')
    screen.blit(text, ((leftOct * 245) - 93, HEIGHT - 55))
    text = s_font.render(leftHand[5], True, 'white')
    screen.blit(text, ((leftOct * 245) - 58, HEIGHT - 55))
    text = s_font.render(leftHand[7], True, 'white')
    screen.blit(text, ((leftOct * 245) - 23, HEIGHT - 55))
    text = s_font.render(leftHand[9], True, 'white')
    screen.blit(text, ((leftOct * 245) + 12, HEIGHT - 55))
    text = s_font.render(leftHand[11], True, 'white')
    screen.blit(text, ((leftOct * 245) + 45, HEIGHT - 55))

    text = s_font.render(leftHand[1], True, 'black')
    screen.blit(text, ((leftOct * 245) - 145, HEIGHT - 55))
    text = s_font.render(leftHand[3], True, 'black')
    screen.blit(text, ((leftOct * 245) - 111, HEIGHT - 55))
    text = s_font.render(leftHand[6], True, 'black')
    screen.blit(text, ((leftOct * 245) - 41, HEIGHT - 55))
    text = s_font.render(leftHand[8], True, 'black')
    screen.blit(text, ((leftOct * 245) - 6, HEIGHT - 55))
    text = s_font.render(leftHand[10], True, 'black')
    screen.blit(text, ((leftOct * 245) + 31, HEIGHT - 55))
    # Правая рука
    pygame.draw.rect(screen, 'dark gray', [(rightOct * 245) - 175, HEIGHT - 60, 245, 30], 0, 4)
    pygame.draw.rect(screen, 'black', [(rightOct * 245) - 175, HEIGHT - 60, 245, 30], 2, 4)

    text = s_font.render(rightHand[0], True, 'white')
    screen.blit(text, ((rightOct * 245) - 162, HEIGHT - 55))
    text = s_font.render(rightHand[2], True, 'white')
    screen.blit(text, ((rightOct * 245) - 127, HEIGHT - 55))
    text = s_font.render(rightHand[4], True, 'white')
    screen.blit(text, ((rightOct * 245) - 92, HEIGHT - 55))
    text = s_font.render(rightHand[5], True, 'white')
    screen.blit(text, ((rightOct * 245) - 58, HEIGHT - 55))
    text = s_font.render(rightHand[7], True, 'white')
    screen.blit(text, ((rightOct * 245) - 20, HEIGHT - 55))
    text = s_font.render(rightHand[9], True, 'white')
    screen.blit(text, ((rightOct * 245) + 11, HEIGHT - 55))
    text = s_font.render(rightHand[11], True, 'white')
    screen.blit(text, ((rightOct * 245) + 47, HEIGHT - 55))

    text = s_font.render(rightHand[1], True, 'black')
    screen.blit(text, ((rightOct * 245) - 145, HEIGHT - 55))
    text = s_font.render(rightHand[3], True, 'black')
    screen.blit(text, ((rightOct * 245) - 110, HEIGHT - 55))
    text = s_font.render(rightHand[6], True, 'black')
    screen.blit(text, ((rightOct * 245) - 40, HEIGHT - 55))
    text = s_font.render(rightHand[8], True, 'black')
    screen.blit(text, ((rightOct * 245) - 5, HEIGHT - 55))
    text = s_font.render(rightHand[10], True, 'black')
    screen.blit(text, ((rightOct * 245) + 30, HEIGHT - 55))


def draw_title_bar():
    instruction_text = m_font.render('Стрелки вверх/вниз для смены левой руки', True, 'black')
    screen.blit(instruction_text, (WIDTH - 800, 10))
    instruction_text2 = m_font.render('Стрелки влево/вправо для смены правой руки', True, 'black')
    screen.blit(instruction_text2, (WIDTH - 800, 50))

    title_text = l_font.render('Симулятор фортепиано', True, 'white')
    screen.blit(title_text, (298, 18))
    title_text = l_font.render('Симулятор фортепиано', True, 'black')
    screen.blit(title_text, (300, 20))


run = True
while run:
    left_dict = {'Z': f'C{left_oct}',
                 'S': f'C#{left_oct}',
                 'X': f'D{left_oct}',
                 'D': f'D#{left_oct}',
                 'C': f'E{left_oct}',
                 'V': f'F{left_oct}',
                 'G': f'F#{left_oct}',
                 'B': f'G{left_oct}',
                 'H': f'G#{left_oct}',
                 'N': f'A{left_oct}',
                 'J': f'A#{left_oct}',
                 'M': f'B{left_oct}'}

    right_dict = {'R': f'C{right_oct}',
                  '5': f'C#{right_oct}',
                  'T': f'D{right_oct}',
                  '6': f'D#{right_oct}',
                  'Y': f'E{right_oct}',
                  'U': f'F{right_oct}',
                  '8': f'F#{right_oct}',
                  'I': f'G{right_oct}',
                  '9': f'G#{right_oct}',
                  'O': f'A{right_oct}',
                  '0': f'A#{right_oct}',
                  'P': f'B{right_oct}'}
    timer.tick(fps)
    screen.fill('gray')

    white_keys, black_keys, active_whites, active_blacks = draw_piano(active_whites, active_blacks)
    draw_hands(right_oct, left_oct, right_hand, left_hand)
    draw_title_bar()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


        # Обработка нажатия мышью
        if event.type == pygame.MOUSEBUTTONDOWN:
            black_key = False
            for i in range(len(black_keys)):
                if black_keys[i].collidepoint(event.pos):
                    black_sounds[i].play(0, 1000)
                    black_key = True
                    active_blacks.append([i, 30])
            for i in range(len(white_keys)):
                if white_keys[i].collidepoint(event.pos) and not black_key:
                    white_sounds[i].play(0, 3000)
                    active_whites.append([i, 30])


        if event.type == pygame.TEXTINPUT:
            # Обработка левой руки
            if event.text.upper() in left_dict:
                note = left_dict[event.text.upper()]
                if note[1] == '#':  # Если это черная клавиша
                    if note in black_labels:  # Проверяем, есть ли такая нота вообще?
                        index = black_labels.index(note)
                        black_sounds[index].play(0, 1000)
                        active_blacks.append([index, 30])
                else:  # Если это белая клавиша
                    if note in white_notes:  # Проверяем, есть ли такая нота вообще?
                        index = white_notes.index(note)
                        white_sounds[index].play(0, 3000)
                        active_whites.append([index, 30])
            # Обработка правой руки
            if event.text.upper() in right_dict:
                note = right_dict[event.text.upper()]
                if note[1] == '#':
                    if note in black_labels:  # ПРОВЕРКА
                        index = black_labels.index(note)
                        black_sounds[index].play(0, 1000)
                        active_blacks.append([index, 30])
                else:
                    if note in white_notes:  # ПРОВЕРКА
                        index = white_notes.index(note)
                        white_sounds[index].play(0, 3000)
                        active_whites.append([index, 30])


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if right_oct < 8:
                    right_oct += 1
            if event.key == pygame.K_LEFT:
                if right_oct > 0:
                    right_oct -= 1
            if event.key == pygame.K_UP:
                if left_oct < 8:
                    left_oct += 1
            if event.key == pygame.K_DOWN:
                if left_oct > 0:
                    left_oct -= 1

    pygame.display.flip()
pygame.quit()
