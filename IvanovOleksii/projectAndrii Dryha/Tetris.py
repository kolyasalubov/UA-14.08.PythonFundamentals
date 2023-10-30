import pygame
import random
from collections import defaultdict

FPS = 5
WIDTH_RECT=25
HEIGHT_RECT=25
DELTA_STEP_Y=HEIGHT_RECT
DELTA_STEP_X=WIDTH_RECT
font_size1 = 28
font_size2 = 36
cleans = 0
score = 0
score_increment = 10
pygame.init()
screen_width = 10*WIDTH_RECT
screen_height = 20*HEIGHT_RECT
screen = pygame.display.set_mode((1.7*screen_width, screen_height))


SCREEN_COLOR = (153, 176, 134)
COLOR = (0, 0, 0)
ALPHA_COLOR = (134, 151, 116)

rows = int(screen_height/HEIGHT_RECT)
cols = int(screen_width/WIDTH_RECT)

# draws action screen
def draw_squares(screen):
    screen.fill(SCREEN_COLOR)
    for row in range(rows):
        for col in range(cols):
            pygame.draw.rect(screen, ALPHA_COLOR, [col * WIDTH_RECT, row*HEIGHT_RECT, WIDTH_RECT, HEIGHT_RECT], 2)
            pygame.draw.rect(screen, ALPHA_COLOR, [col * WIDTH_RECT+WIDTH_RECT/5, row*HEIGHT_RECT+HEIGHT_RECT/5, \
                                                    WIDTH_RECT-0.4*WIDTH_RECT, HEIGHT_RECT-0.4*HEIGHT_RECT])

# draws preview screen
mySurface = pygame.Surface((4*WIDTH_RECT, 2*HEIGHT_RECT))

def draw_squares_outer(mySurface):
    mySurface.fill(SCREEN_COLOR)
    for row in range(rows):
        for col in range(cols):
            pygame.draw.rect(mySurface, ALPHA_COLOR, [col * WIDTH_RECT, row*HEIGHT_RECT, WIDTH_RECT, HEIGHT_RECT], 2)
            pygame.draw.rect(mySurface, ALPHA_COLOR, [col * WIDTH_RECT+WIDTH_RECT/5, row*HEIGHT_RECT+HEIGHT_RECT/5, \
                                                       WIDTH_RECT-0.4*WIDTH_RECT, HEIGHT_RECT-0.4*HEIGHT_RECT])
    screen.blit(mySurface,(12*WIDTH_RECT,13*HEIGHT_RECT))


# coords of the rectangles
COORD_LIST_F1 = [[3*WIDTH_RECT, -HEIGHT_RECT], [4*WIDTH_RECT, -HEIGHT_RECT], 
                 [5*WIDTH_RECT, -HEIGHT_RECT], [6*WIDTH_RECT, -HEIGHT_RECT]]
COORD_LIST_F2 = [[4*WIDTH_RECT, -HEIGHT_RECT], [5*WIDTH_RECT, -2*HEIGHT_RECT], 
                 [5*WIDTH_RECT, -HEIGHT_RECT], [6*WIDTH_RECT, -2*HEIGHT_RECT]]
COORD_LIST_F3 = [[4*WIDTH_RECT, -2*HEIGHT_RECT], [5*WIDTH_RECT, -2*HEIGHT_RECT], 
                 [5*WIDTH_RECT, -HEIGHT_RECT], [6*WIDTH_RECT, -HEIGHT_RECT]]
COORD_LIST_F4 = [[4*WIDTH_RECT, -HEIGHT_RECT], [5*WIDTH_RECT, -2*HEIGHT_RECT], 
                 [5*WIDTH_RECT, -HEIGHT_RECT], [6*WIDTH_RECT, -HEIGHT_RECT]]
COORD_LIST_F5 = [[4*WIDTH_RECT, -2*HEIGHT_RECT], [4*WIDTH_RECT, -HEIGHT_RECT], 
                 [5*WIDTH_RECT, -HEIGHT_RECT], [5*WIDTH_RECT, -2*HEIGHT_RECT]]
COORD_LIST_F6 = [[4*WIDTH_RECT, -HEIGHT_RECT], [6*WIDTH_RECT, -HEIGHT_RECT], 
                 [5*WIDTH_RECT, -HEIGHT_RECT], [6*WIDTH_RECT, -2*HEIGHT_RECT]]
COORD_LIST_F7 = [[4*WIDTH_RECT, -2*HEIGHT_RECT], [4*WIDTH_RECT, -HEIGHT_RECT], 
                 [5*WIDTH_RECT, -HEIGHT_RECT], [6*WIDTH_RECT, -HEIGHT_RECT]]
COORD_LIST = random.choice([COORD_LIST_F1, 
                            COORD_LIST_F2, 
                            COORD_LIST_F3, 
                            COORD_LIST_F4, 
                            COORD_LIST_F5, 
                            COORD_LIST_F6, 
                            COORD_LIST_F7])
COORD_LIST_F1_OUTER = [[x[0]+9*WIDTH_RECT, x[1]+15*HEIGHT_RECT] for x in COORD_LIST_F1]
COORD_LIST_F2_OUTER = [[x[0]+9*WIDTH_RECT, x[1]+15*HEIGHT_RECT] for x in COORD_LIST_F2]
COORD_LIST_F3_OUTER = [[x[0]+9*WIDTH_RECT, x[1]+15*HEIGHT_RECT] for x in COORD_LIST_F3]
COORD_LIST_F4_OUTER = [[x[0]+9*WIDTH_RECT, x[1]+15*HEIGHT_RECT] for x in COORD_LIST_F4]
COORD_LIST_F5_OUTER = [[x[0]+9*WIDTH_RECT, x[1]+15*HEIGHT_RECT] for x in COORD_LIST_F5]
COORD_LIST_F6_OUTER = [[x[0]+9*WIDTH_RECT, x[1]+15*HEIGHT_RECT] for x in COORD_LIST_F6]
COORD_LIST_F7_OUTER = [[x[0]+9*WIDTH_RECT, x[1]+15*HEIGHT_RECT] for x in COORD_LIST_F7]
COORD_X1=COORD_LIST[0][0]
COORD_Y1=COORD_LIST[0][1]
COORD_X2=COORD_LIST[1][0]
COORD_Y2=COORD_LIST[1][1]
COORD_X3=COORD_LIST[2][0]
COORD_Y3=COORD_LIST[2][1]
COORD_X4=COORD_LIST[3][0]
COORD_Y4=COORD_LIST[3][1]
COORD_LIST_OUTER = random.choice([COORD_LIST_F1_OUTER, 
                            COORD_LIST_F2_OUTER, 
                            COORD_LIST_F3_OUTER, 
                            COORD_LIST_F4_OUTER, 
                            COORD_LIST_F5_OUTER, 
                            COORD_LIST_F6_OUTER, 
                            COORD_LIST_F7_OUTER])
COORD_X1_OUT=COORD_LIST_OUTER[0][0]
COORD_Y1_OUT=COORD_LIST_OUTER[0][1]
COORD_X2_OUT=COORD_LIST_OUTER[1][0]
COORD_Y2_OUT=COORD_LIST_OUTER[1][1]
COORD_X3_OUT=COORD_LIST_OUTER[2][0]
COORD_Y3_OUT=COORD_LIST_OUTER[2][1]
COORD_X4_OUT=COORD_LIST_OUTER[3][0]
COORD_Y4_OUT=COORD_LIST_OUTER[3][1]
COORD_LIST_X = [COORD_X1, COORD_X2, COORD_X3, COORD_X4]
COORD_LIST_Y = [COORD_Y1, COORD_Y2, COORD_Y3, COORD_Y4]

rect_landed = False
clock = pygame.time.Clock()
# list of landed rectangles
landed_rectangles = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()


    ## draw the text display

    # constant text
    font = pygame.font.SysFont("Arial", font_size1)

    txtsurf1 = font.render("Next", True, COLOR)
    txtsurf2 = font.render("Level", True, COLOR)
    txtsurf3 = font.render("Cleans", True, COLOR)
    txtsurf4 = font.render("Score", True, COLOR)

    # counter text
    font_num = pygame.font.Font("AndriiDryha\Final_Project\Fonts\DS-DIGIB.TTF", font_size2)

    txtnumsurf1 = font_num.render("888888", True, ALPHA_COLOR)
    txtnumsurf2 = font_num.render("888888", True, ALPHA_COLOR)
    txtnumsurf3 = font_num.render("1", True, COLOR)

    # score counter
    num1 = "O"
    num2 = " "
    num3 = " "
    num4 = " "
    num5 = " "
    num6 = " "
    num_list = [num1, num2, num3, num4, num5, num6]
    score_list = list(str(score))
    for i in range(len(score_list)):
        if score_list[i] == "0":
              score_list[i] = "O"


    if len(score_list) == len(num_list):
            [num1, num2, num3, num4, num5, num6] = \
               [score_list[-1], score_list[-2], score_list[-3], score_list[-4], score_list[-5], score_list[-6]]
    elif len(score_list)+1 == len(num_list):
            [num1, num2, num3, num4, num5] = [score_list[-1], score_list[-2], score_list[-3], score_list[-4], score_list[-5]]
    elif len(score_list)+2 == len(num_list):
            [num1, num2, num3, num4] = [score_list[-1], score_list[-2], score_list[-3], score_list[-4]]
    elif len(score_list)+3 == len(num_list):
            [num1, num2, num3] = [score_list[-1], score_list[-2], score_list[-3]]
    elif len(score_list)+4 == len(num_list):
            [num1, num2] = [score_list[-1], score_list[-2]]
    elif len(score_list)+5 == len(num_list):
            num1 = score_list[-1]

    # counter of cleans
    num_1 = "O"
    num_2 = " "
    num_3 = " "
    num_4 = " "
    num_5 = " "
    num_6 = " "
    num_list_ = [num_1, num_2, num_3, num_4, num_5, num_6]
    cleans_list =  list(str(cleans))
    for i in range(len(cleans_list)):
        if cleans_list[i] == "0":
              cleans_list[i] = "O"

    if len(cleans_list)-2 == len(num_list_):
            [num_1, num_2, num_3, num_4, num_5, num_6] = \
               [cleans_list[-3], cleans_list[-4], cleans_list[-5], cleans_list[-6], cleans_list[-7], cleans_list[-8]]
    elif len(cleans_list)-1 == len(num_list_):
            [num_1, num_2, num_3, num_4, num_5] = [cleans_list[-3], cleans_list[-4], cleans_list[-5], cleans_list[-6], cleans_list[-7]]
    elif len(cleans_list) == len(num_list_):
            [num_1, num_2, num_3, num_4] = [cleans_list[-3], cleans_list[-4], cleans_list[-5], cleans_list[-6]]
    elif len(cleans_list)+1 == len(num_list_):
            [num_1, num_2, num_3] = [cleans_list[-3], cleans_list[-4], cleans_list[-5]]
    elif len(cleans_list)+2 == len(num_list_):
            [num_1, num_2] = [cleans_list[-3], cleans_list[-4]]
    elif len(cleans_list)+3 == len(num_list_):
            num_1 = cleans_list[-3]
    
    
    
    numsurf1 = font_num.render(f"O", True, COLOR)
    numsurf2 = font_num.render(f"{num2}", True, COLOR)
    numsurf3 = font_num.render(f"{num3}", True, COLOR)
    numsurf4 = font_num.render(f"{num4}", True, COLOR)
    numsurf5 = font_num.render(f"{num5}", True, COLOR)
    numsurf6 = font_num.render(f"{num6}", True, COLOR)


    numsurf_1 = font_num.render(f"{num_1}", True, COLOR)
    numsurf_2 = font_num.render(f"{num_2}", True, COLOR)
    numsurf_3 = font_num.render(f"{num_3}", True, COLOR)
    numsurf_4 = font_num.render(f"{num_4}", True, COLOR)
    numsurf_5 = font_num.render(f"{num_5}", True, COLOR)
    numsurf_6 = font_num.render(f"{num_6}", True, COLOR)


    # motion and rotation
    if not rect_landed:
        keys = pygame.key.get_pressed()
        COORD_LIST_X = [COORD_X1, COORD_X2, COORD_X3, COORD_X4]
        COORD_LIST_Y = [COORD_Y1, COORD_Y2, COORD_Y3, COORD_Y4]

        #################### SECTION IN DEVELOPING ####################

        # SHIFT_LIST_X1 = [x-WIDTH_RECTANGLE for x in COORD_LIST_X]
        # SHIFT_LIST_X2 = [x+WIDTH_RECTANGLE for x in COORD_LIST_X]
        # LANDED_LIST_X = [x[0] for x in landed_rectangles]
        # LANDED_LIST_Y = [x[1] for x in landed_rectangles]
        # COLLISION_COORDS = [[x[0], x[1]] for x in landed_rectangles for n in COORD_LIST if x[1] == n[1]]
        # COLLISION_COORDS_X = [x[0] for x in COLLISION_COORDS]
        # if list(set(COORD_LIST_Y) & set(LANDED_LIST_Y)) == []:

        #################### SECTION IN DEVELOPING ####################

        if min(COORD_LIST_X, key=lambda i: i) > 0 and keys[pygame.K_LEFT]:
            COORD_X1 -= DELTA_STEP_X
            COORD_X2 -= DELTA_STEP_X
            COORD_X3 -= DELTA_STEP_X
            COORD_X4 -= DELTA_STEP_X
        if max(COORD_LIST_X, key=lambda i: i) < screen_width - WIDTH_RECT and keys[pygame.K_RIGHT]:
            COORD_X1 += DELTA_STEP_X
            COORD_X2 += DELTA_STEP_X
            COORD_X3 += DELTA_STEP_X
            COORD_X4 += DELTA_STEP_X
        COORD_LIST = [[COORD_X1, COORD_Y1], [COORD_X2, COORD_Y2], [COORD_X3, COORD_Y3], [COORD_X4, COORD_Y4]]
        origin = [COORD_X3, COORD_Y3]
        if event.type == pygame.KEYDOWN:        
            if max(COORD_LIST, key=lambda i: i) != origin \
                and screen_width - WIDTH_RECT > COORD_X3 > 0 \
                and COORD_Y3 < screen_height - HEIGHT_RECT and keys[pygame.K_UP]:
                COORD_X1 = origin[1] - COORD_LIST[0][1] + origin[0]
                COORD_Y1 = COORD_LIST[0][0] - origin[0] + origin[1]
                COORD_X2 = origin[1] - COORD_LIST[1][1] + origin[0]
                COORD_Y2 = COORD_LIST[1][0] - origin[0] + origin[1]
                COORD_X3 = origin[1] - COORD_LIST[2][1] + origin[0]
                COORD_Y3 = COORD_LIST[2][0] - origin[0] + origin[1]
                COORD_X4 = origin[1] - COORD_LIST[3][1] + origin[0]
                COORD_Y4 = COORD_LIST[3][0] - origin[0] + origin[1]

            #################### SECTION IN DEVELOPING ####################

            # Rotation case

            # if COORD_LIST != COORD_LIST_F5 and COORD_LIST == COORD_LIST_F1 \
            #     and screen_width - 2*WIDTH_RECTANGLE > COORD_X2 > 0 \
            #     and COORD_Y2 < screen_height - 2*HEIGHT_RECTANGLE and keys[pygame.K_UP]:
            #     origin = [COORD_X2, COORD_Y2]
            #     if COORD_Y3 == COORD_Y1 == COORD_Y2 == COORD_Y4:
            #         COORD_X1 = origin[1] - COORD_LIST[0][1] + origin[0]
            #         COORD_Y1 = COORD_LIST[0][0] - origin[0] + origin[1]
            #         COORD_X2 = origin[1] - COORD_LIST[1][1] + origin[0]
            #         COORD_Y2 = COORD_LIST[1][0] - origin[0] + origin[1]
            #         COORD_X3 = origin[1] - COORD_LIST[2][1] + origin[0]
            #         COORD_Y3 = COORD_LIST[2][0] - origin[0] + origin[1]
            #         COORD_X4 = origin[1] - COORD_LIST[3][1] + origin[0]
            #         COORD_Y4 = COORD_LIST[3][0] - origin[0] + origin[1]
            #     else:
            #         COORD_Y1 = origin[1] - COORD_LIST[0][0] + origin[0]
            #         COORD_X1 = COORD_LIST[0][1] - origin[1] + origin[0]
            #         COORD_Y1 = origin[1] - COORD_LIST[1][0] + origin[0]
            #         COORD_X1 = COORD_LIST[1][1] - origin[1] + origin[0]
            #         COORD_Y1 = origin[1] - COORD_LIST[2][0] + origin[0]
            #         COORD_X1 = COORD_LIST[2][1] - origin[1] + origin[0]
            #         COORD_Y1 = origin[1] - COORD_LIST[3][0] + origin[0]
            #         COORD_X1 = COORD_LIST[3][1] - origin[1] + origin[0]
                      
                      
        # Side collision case
             
        # if list(set(COORD_LIST_Y) & set(LANDED_LIST_Y)) != []:
        #         COLLISION_COORDS = [[x[0], x[1]] for x in landed_rectangles for n in COORD_LIST if x[1] == n[1]]
        #         # COLLISION_COORDS_X = [x[0] for x in COLLISION_COORDS]
        #         COORD_LIST_SHIFT_R = [[x[0]+WIDTH_RECTANGLE, x[1]] for x in COORD_LIST]
        #         COORD_LIST_SHIFT_L = [[x[0]-WIDTH_RECTANGLE, x[1]] for x in COORD_LIST]
        #         COLLISION_COORDS_L = [[x[0], x[1]] for x in COLLISION_COORDS if x in COORD_LIST_SHIFT_R]
        #         COLLISION_COORDS_R = [[x[0], x[1]] for x in COLLISION_COORDS if x in COORD_LIST_SHIFT_L]
        #         if COLLISION_COORDS_L != [] and COLLISION_COORDS_R != [] and keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
        #             # sleep(delay)
        #             pass
        #         elif COLLISION_COORDS_L != [] and keys[pygame.K_LEFT]:
        #             # sleep(delay)
        #             pass
        #         elif COLLISION_COORDS_R != [] and keys[pygame.K_RIGHT]:
        #             # sleep(delay) 
        #             pass
        #         elif COLLISION_COORDS_R != [] or min(COORD_LIST_X, key=lambda i: i) > 0 and keys[pygame.K_LEFT]:
        #             COORD_X1 += DELTA_STEP
        #             COORD_X2 += DELTA_STEP
        #             COORD_X3 += DELTA_STEP
        #             COORD_X4 += DELTA_STEP
        #         elif COLLISION_COORDS_L != [] or max(COORD_LIST_X, key=lambda i: i) < screen_width - WIDTH_RECTANGLE and keys[pygame.K_RIGHT]:
        #             COORD_X1 -= DELTA_STEP
        #             COORD_X2 -= DELTA_STEP
        #             COORD_X3 -= DELTA_STEP
        #             COORD_X4 -= DELTA_STEP   

            #################### SECTION IN DEVELOPING ####################



        # addition of landed rectangles' coords to the list
        for landed_rect in landed_rectangles:
            landed_rect = pygame.Rect(landed_rect[0], landed_rect[1], WIDTH_RECT, HEIGHT_RECT)
            falling_rect1 = pygame.Rect(COORD_X1, COORD_Y1+HEIGHT_RECT, WIDTH_RECT, HEIGHT_RECT)
            falling_rect2 = pygame.Rect(COORD_X2, COORD_Y2+HEIGHT_RECT, WIDTH_RECT, HEIGHT_RECT)
            falling_rect3 = pygame.Rect(COORD_X3, COORD_Y3+HEIGHT_RECT, WIDTH_RECT, HEIGHT_RECT)
            falling_rect4 = pygame.Rect(COORD_X4, COORD_Y4+HEIGHT_RECT, WIDTH_RECT, HEIGHT_RECT)
            falling_rect_list = [falling_rect1, falling_rect2, falling_rect3, falling_rect4]
            if landed_rect.collidelistall(falling_rect_list):
                rect_landed = True
                COORD_LIST = [[COORD_X1, COORD_Y1], [COORD_X2, COORD_Y2], [COORD_X3, COORD_Y3], [COORD_X4, COORD_Y4]]
                landed_rectangles.extend(COORD_LIST)
                break
            
          
     
        # motion down
        if not rect_landed:
            
            COORD_Y1 += DELTA_STEP_Y
            COORD_Y2 += DELTA_STEP_Y
            COORD_Y3 += DELTA_STEP_Y
            COORD_Y4 += DELTA_STEP_Y

            COORD_LIST_Y = [COORD_Y1, COORD_Y2, COORD_Y3, COORD_Y4]
            if max(COORD_LIST_Y, key=lambda i: i) + HEIGHT_RECT == screen_height:
                rect_landed = True
                COORD_LIST = [[COORD_X1, COORD_Y1], [COORD_X2, COORD_Y2], [COORD_X3, COORD_Y3], [COORD_X4, COORD_Y4]]
                landed_rectangles.extend(COORD_LIST)

    # creation of new figure when former one landed
    if rect_landed:
        COORD_LIST = [[x[0]-9*WIDTH_RECT, x[1]-15*HEIGHT_RECT] for x in COORD_LIST_OUTER]
        COORD_X1=COORD_LIST[0][0]
        COORD_Y1=COORD_LIST[0][1]
        COORD_X2=COORD_LIST[1][0]
        COORD_Y2=COORD_LIST[1][1]
        COORD_X3=COORD_LIST[2][0]
        COORD_Y3=COORD_LIST[2][1]
        COORD_X4=COORD_LIST[3][0]
        COORD_Y4=COORD_LIST[3][1]
        COORD_LIST_OUTER = random.choice([COORD_LIST_F1_OUTER, 
                            COORD_LIST_F2_OUTER, 
                            COORD_LIST_F3_OUTER, 
                            COORD_LIST_F4_OUTER, 
                            COORD_LIST_F5_OUTER, 
                            COORD_LIST_F6_OUTER, 
                            COORD_LIST_F7_OUTER])
        COORD_X1_OUT=COORD_LIST_OUTER[0][0]
        COORD_Y1_OUT=COORD_LIST_OUTER[0][1]
        COORD_X2_OUT=COORD_LIST_OUTER[1][0]
        COORD_Y2_OUT=COORD_LIST_OUTER[1][1]
        COORD_X3_OUT=COORD_LIST_OUTER[2][0]
        COORD_Y3_OUT=COORD_LIST_OUTER[2][1]
        COORD_X4_OUT=COORD_LIST_OUTER[3][0]
        COORD_Y4_OUT=COORD_LIST_OUTER[3][1]
        
        score += score_increment
        
        rect_landed = False
     #    print(landed_rectangles)

    screen.fill(SCREEN_COLOR)

    draw_squares(screen)
    draw_squares_outer(mySurface)

    # combustion of lines and displacement of upper rectangles 
    for landed_rect in landed_rectangles:
        slider_list = landed_rectangles
        line_count = []
        counter = defaultdict(int)
        for x in slider_list:
            counter[x[1]] += 1

        for name, number in sorted(counter.items(), key=lambda x: x[1], reverse=True):
            if number == screen_width/WIDTH_RECT:
                line_count.append(name)
                slider_list = [item for item in slider_list if item[1] != name]
        lines = line_count
        if line_count != []:
            slider_list = list(map(lambda x: [x[0],x[1]+(max(line_count)-x[1])] \
                                if min(line_count) < x[1] < max(line_count) \
                                      else [x[0],x[1]], slider_list))
            slider_list = list(map(lambda x: [x[0],x[1]+len(line_count)*HEIGHT_RECT] \
                                if x[1] < min(line_count) else [x[0],x[1]], slider_list))
            # print(line_count)
            # print(max(line_count))
        landed_rectangles = []
        if len(lines) > 0:
            score += len(lines)*10*score_increment - score_increment
            cleans += float(len(lines))
            # print(cleans)
            # print(list(str(cleans)))
        landed_rectangles.extend(slider_list)
        pygame.draw.rect(screen, COLOR, [landed_rect[0], landed_rect[1], WIDTH_RECT, HEIGHT_RECT], 2)
        pygame.draw.rect(screen, COLOR, [landed_rect[0]+WIDTH_RECT/5, landed_rect[1]+HEIGHT_RECT/5, WIDTH_RECT-0.4*WIDTH_RECT, HEIGHT_RECT-0.4*HEIGHT_RECT])
        

    pygame.draw.rect(screen, COLOR, [COORD_X1_OUT, COORD_Y1_OUT, WIDTH_RECT, HEIGHT_RECT], 2)
    pygame.draw.rect(screen, COLOR, [COORD_X1_OUT+WIDTH_RECT/5, COORD_Y1_OUT+HEIGHT_RECT/5, WIDTH_RECT-0.4*WIDTH_RECT, HEIGHT_RECT-0.4*HEIGHT_RECT])
    pygame.draw.rect(screen, COLOR, [COORD_X2_OUT, COORD_Y2_OUT, WIDTH_RECT, HEIGHT_RECT], 2)
    pygame.draw.rect(screen, COLOR, [COORD_X2_OUT+WIDTH_RECT/5, COORD_Y2_OUT+HEIGHT_RECT/5, WIDTH_RECT-0.4*WIDTH_RECT, HEIGHT_RECT-0.4*HEIGHT_RECT])
    pygame.draw.rect(screen, COLOR, [COORD_X3_OUT, COORD_Y3_OUT, WIDTH_RECT, HEIGHT_RECT], 2)
    pygame.draw.rect(screen, COLOR, [COORD_X3_OUT+WIDTH_RECT/5, COORD_Y3_OUT+HEIGHT_RECT/5, WIDTH_RECT-0.4*WIDTH_RECT, HEIGHT_RECT-0.4*HEIGHT_RECT])
    pygame.draw.rect(screen, COLOR, [COORD_X4_OUT, COORD_Y4_OUT, WIDTH_RECT, HEIGHT_RECT], 2)
    pygame.draw.rect(screen, COLOR, [COORD_X4_OUT+WIDTH_RECT/5, COORD_Y4_OUT+HEIGHT_RECT/5, WIDTH_RECT-0.4*WIDTH_RECT, HEIGHT_RECT-0.4*HEIGHT_RECT])
    pygame.draw.rect(screen, COLOR, [COORD_X1, COORD_Y1, WIDTH_RECT, HEIGHT_RECT], 2)
    pygame.draw.rect(screen, COLOR, [COORD_X1+WIDTH_RECT/5, COORD_Y1+HEIGHT_RECT/5, WIDTH_RECT-0.4*WIDTH_RECT, HEIGHT_RECT-0.4*HEIGHT_RECT])
    pygame.draw.rect(screen, COLOR, [COORD_X2, COORD_Y2, WIDTH_RECT, HEIGHT_RECT], 2)
    pygame.draw.rect(screen, COLOR, [COORD_X2+WIDTH_RECT/5, COORD_Y2+HEIGHT_RECT/5, WIDTH_RECT-0.4*WIDTH_RECT, HEIGHT_RECT-0.4*HEIGHT_RECT])
    pygame.draw.rect(screen, COLOR, [COORD_X3, COORD_Y3, WIDTH_RECT, HEIGHT_RECT], 2)
    pygame.draw.rect(screen, COLOR, [COORD_X3+WIDTH_RECT/5, COORD_Y3+HEIGHT_RECT/5, WIDTH_RECT-0.4*WIDTH_RECT, HEIGHT_RECT-0.4*HEIGHT_RECT])
    pygame.draw.rect(screen, COLOR, [COORD_X4, COORD_Y4, WIDTH_RECT, HEIGHT_RECT], 2)
    pygame.draw.rect(screen, COLOR, [COORD_X4+WIDTH_RECT/5, COORD_Y4+HEIGHT_RECT/5, WIDTH_RECT-0.4*WIDTH_RECT, HEIGHT_RECT-0.4*HEIGHT_RECT])

    
    screen.blit(txtsurf1,(11*WIDTH_RECT, 12*HEIGHT_RECT - txtsurf1.get_height() / 2))
    screen.blit(txtsurf2,(11*WIDTH_RECT, 8*HEIGHT_RECT - txtsurf1.get_height() / 2))
    screen.blit(txtsurf3,(11*WIDTH_RECT, 3*HEIGHT_RECT + txtsurf1.get_height() / 2))
    screen.blit(txtsurf4,(11*WIDTH_RECT, 1*HEIGHT_RECT - txtsurf1.get_height() / 2))
    screen.blit(txtnumsurf1,(12*WIDTH_RECT, 2.5*HEIGHT_RECT - txtnumsurf1.get_height() / 2))
    screen.blit(txtnumsurf2,(12*WIDTH_RECT, 6*HEIGHT_RECT - txtnumsurf1.get_height() / 2))



    screen.blit(numsurf1,(12*WIDTH_RECT + txtnumsurf1.get_width()*5/6, 2.5*HEIGHT_RECT - txtnumsurf1.get_height() / 2))
    screen.blit(numsurf2,(12*WIDTH_RECT + txtnumsurf1.get_width()*4/6, 2.5*HEIGHT_RECT - txtnumsurf1.get_height() / 2))
    screen.blit(numsurf3,(12*WIDTH_RECT + txtnumsurf1.get_width()*3/6, 2.5*HEIGHT_RECT - txtnumsurf1.get_height() / 2))
    screen.blit(numsurf4,(12*WIDTH_RECT + txtnumsurf1.get_width()*2/6, 2.5*HEIGHT_RECT - txtnumsurf1.get_height() / 2))
    screen.blit(numsurf5,(12*WIDTH_RECT + txtnumsurf1.get_width()*1/6, 2.5*HEIGHT_RECT - txtnumsurf1.get_height() / 2))
    screen.blit(numsurf6,(12*WIDTH_RECT, 2.5*HEIGHT_RECT - 30 / 2))

    

    screen.blit(numsurf_1,(12*WIDTH_RECT + txtnumsurf2.get_width()*5/6, 6*HEIGHT_RECT - txtnumsurf2.get_height() / 2))
    screen.blit(numsurf_2,(12*WIDTH_RECT + txtnumsurf2.get_width()*4/6, 6*HEIGHT_RECT - txtnumsurf2.get_height() / 2))
    screen.blit(numsurf_3,(12*WIDTH_RECT + txtnumsurf2.get_width()*3/6, 6*HEIGHT_RECT - txtnumsurf2.get_height() / 2))
    screen.blit(numsurf_4,(12*WIDTH_RECT + txtnumsurf2.get_width()*2/6, 6*HEIGHT_RECT - txtnumsurf2.get_height() / 2))
    screen.blit(numsurf_5,(12*WIDTH_RECT + txtnumsurf2.get_width()*1/6, 6*HEIGHT_RECT - txtnumsurf2.get_height() / 2))
    screen.blit(numsurf_6,(12*WIDTH_RECT, 6*HEIGHT_RECT - txtnumsurf2.get_height() / 2))

    screen.blit(txtnumsurf3,(12*WIDTH_RECT + txtnumsurf2.get_width()*5.5/6, 9*HEIGHT_RECT))
    
    
    pygame.display.update()

    pygame.time.Clock().tick(FPS)

######################################################################################

# import random
# from collections import defaultdict

# COORD_LIST_F1 = [[75, -25], [100, -25], [125, -25], [150, -25]]
# COORD_LIST_F2 = [[100, -25], [125, -25], [125, -50], [150, -50]]
# COORD_LIST_F3 = [[100, -50], [125, -50], [125, -25], [150, -25]]
# COORD_LIST_F4 = [[100, -25], [125, -25], [125, -50], [150, -25]]
# COORD_LIST_F5 = [[100, -50], [100, -25], [125, -25], [125, -50]]
# COORD_LIST_F6 = [[100, -25], [125, -25], [150, -25], [150, -50]]
# COORD_LIST_F7 = [[100, -50], [100, -25], [125, -25], [150, -25]]
# COORD_LIST = random.choice([COORD_LIST_F1, COORD_LIST_F2, COORD_LIST_F3, COORD_LIST_F4, COORD_LIST_F5, COORD_LIST_F6, COORD_LIST_F7])
# COORD_X1=COORD_LIST[0][0]
# COORD_Y1=COORD_LIST[0][1]
# COORD_X2=COORD_LIST[1][0]
# COORD_Y2=COORD_LIST[1][1]
# COORD_X3=COORD_LIST[2][0]
# COORD_Y3=COORD_LIST[2][1]
# COORD_X4=COORD_LIST[3][0]
# COORD_Y4=COORD_LIST[3][1]
# # # # print(COORD_LIST)


# # #********************************************
# # # elements of 2 massives with common Y coord 
# # COLLISION_COORDS = [[x[0], x[1]] for x in list1 for n in list2 if x[1] == n[1]]

# list56 = [[4, 2], [8, 8], [5, 10], [10, 7], [3, 7], [9, 1], [4, 6], [1, 7], [8, 9], [1, 8], [0, 8], [2, 10]]
# # list56= [[4, 2], [8, 8], [5, 10], [10, 7]]
# print(list56)
# line_count = []
# print(line_count)
# #********************************
# # find elements with their indexes 
# counter = defaultdict(int)
# for x in list56:
#     counter[x[1]] += 1

# for name, number in sorted(counter.items(), key=lambda x: x[1], reverse=True):
#     # delete definite count of elements using their indexes
#     if number == 3:
#         line_count.append(name)
#         list56 = [item for item in list56 if item[1] != name]

#     # print(name, number)
#         print(list56)
# # Y's of deleted elements
#         print(line_count)

# # move elements with Y > Y of deleted elements
#         list56 = list(map(lambda x: [x[0],x[1]-len(line_count)] if x[1] > max(line_count) else [x[0],x[1]], list56))
# line_count = []

# print(list56)
# print(line_count)
# #*******************************
# print(list1)
# # index + element
# for count, i in enumerate(list1): 
#     print (count, i)

# # delite all elements with Y = 10
# list1 = [item for item in list1 if item[1] != 10]

# #*********************************












    

