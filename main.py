import pygame
import random

size_of_window_x = 340
size_of_window_y = 40 + 30 * 25

pygame.init()
pygame.font.init()
pygame.display.set_caption("Loptice")
window = pygame.display.set_mode((size_of_window_x, size_of_window_y))

block_images = []
block_images.append(pygame.image.load("media\BLOCK_RED.png").convert_alpha())
block_images.append(pygame.image.load("media\BLOCK_BLUE.png").convert_alpha())
block_images.append(pygame.image.load("media\BLOCK_PURPLE.png").convert_alpha())
block_images.append(pygame.image.load("media\BLOCK_ORANGE.png").convert_alpha())
block_images.append(pygame.image.load("media\BLOCK_GREEN.png").convert_alpha())

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)


class Figure:
    def __init__(self, X, Y, ind):
        self.x = X
        self.y = Y
        self.positions = []
        self.current_rotation = 0
        self.num_rotations = 0
        self.block_img = block_images[ind]
        self.color_index = ind

    def change_pos(self, dx, dy, num_hor, num_ver, field, k):
        i = self.current_rotation

        for j in range(len(self.positions[i])):
            if self.positions[i][j][1] + dy >= num_ver:
                return True

        for j in range(len(self.positions[i])):
            n_x = self.positions[i][j][0]
            n_y = self.positions[i][j][1] + dy
            if field[n_x][n_y] != k and field[n_x][n_y] != -1:
                return True

        for j in range(len(self.positions[i])):
            if self.positions[i][j][1] + dy < 0:
                return False

        for j in range(len(self.positions[i])):
            if self.positions[i][j][0] + dx < 0 or self.positions[i][j][0] + dx >= num_hor:
                return False

            n_x = self.positions[i][j][0] + dx
            n_y = self.positions[i][j][1]
            if field[n_x][n_y] != k and field[n_x][n_y] != -1:
                return False

        for i in range(len(self.positions)):
            for j in range(len(self.positions[i])):
                self.positions[i][j][0] += dx
                self.positions[i][j][1] += dy

        return False

    def rotate(self, num_hor, num_ver, field, k):
        f = (self.current_rotation + 1) % self.num_rotations
        for j in range(len(self.positions[f])):
            if self.positions[f][j][0] < 0 or self.positions[f][j][0] >= num_hor:
                return
            if self.positions[f][j][1] < 0 or self.positions[f][j][1] >= num_ver:
                return

        for j in range(len(self.positions[f])):
            n_x = self.positions[f][j][0]
            n_y = self.positions[f][j][1]
            if field[n_x][n_y] != k and field[n_x][n_y] != -1:
                return True

        self.current_rotation = (self.current_rotation + 1) % self.num_rotations


class Figure1(Figure):
    def __init__(self, X, Y, ind):
        super().__init__(X, Y, ind)
        self.initialise_pos(self.x, self.y)

    def initialise_pos(self, X, Y):
        self.positions.append([[X, Y], [X, Y + 1], [X + 1, Y], [X + 1, Y + 1]])
        self.num_rotations = len(self.positions)


class Figure2(Figure):
    def __init__(self, X, Y, ind):
        super().__init__(X, Y, ind)
        self.initialise_pos(self.x, self.y)

    def initialise_pos(self, X, Y):
        self.positions.append([[X, Y], [X, Y - 1], [X - 1, Y], [X + 1, Y]])
        self.positions.append([[X, Y], [X, Y + 1], [X, Y - 1], [X + 1, Y]])
        self.positions.append([[X, Y], [X, Y + 1], [X + 1, Y], [X - 1, Y]])
        self.positions.append([[X, Y], [X, Y + 1], [X, Y - 1], [X - 1, Y]])
        self.num_rotations = len(self.positions)


class Figure3(Figure):
    def __init__(self, X, Y, ind):
        super().__init__(X, Y, ind)
        self.initialise_pos(self.x, self.y)

    def initialise_pos(self, X, Y):
        self.positions.append([[X, Y], [X - 1, Y], [X + 1, Y], [X + 2, Y]])
        self.positions.append([[X, Y], [X, Y - 1], [X, Y + 1], [X, Y + 2]])
        self.positions.append([[X, Y], [X - 1, Y], [X - 2, Y], [X + 1, Y]])
        self.positions.append([[X, Y], [X, Y - 1], [X, Y - 2], [X, Y + 1]])
        self.num_rotations = len(self.positions)


class Figure4(Figure):
    def __init__(self, X, Y, ind):
        super().__init__(X, Y, ind)
        self.initialise_pos(self.x, self.y)

    def initialise_pos(self, X, Y):
        self.positions.append([[X, Y], [X - 1, Y], [X + 1, Y], [X - 1, Y - 1]])
        self.positions.append([[X, Y], [X, Y - 1], [X, Y + 1], [X + 1, Y - 1]])
        self.positions.append([[X, Y], [X - 1, Y], [X + 1, Y], [X + 1, Y + 1]])
        self.positions.append([[X, Y], [X, Y - 1], [X, Y + 1], [X - 1, Y + 1]])
        self.num_rotations = len(self.positions)


class Figure5(Figure):
    def __init__(self, X, Y, ind):
        super().__init__(X, Y, ind)
        self.initialise_pos(self.x, self.y)

    def initialise_pos(self, X, Y):
        self.positions.append([[X, Y], [X - 1, Y], [X + 1, Y], [X + 1, Y - 1]])
        self.positions.append([[X, Y], [X, Y - 1], [X, Y + 1], [X + 1, Y + 1]])
        self.positions.append([[X, Y], [X - 1, Y], [X + 1, Y], [X - 1, Y + 1]])
        self.positions.append([[X, Y], [X, Y - 1], [X, Y + 1], [X - 1, Y - 1]])
        self.num_rotations = len(self.positions)


class Figure6(Figure):
    def __init__(self, X, Y, ind):
        super().__init__(X, Y, ind)
        self.initialise_pos(self.x, self.y)

    def initialise_pos(self, X, Y):
        self.positions.append([[X, Y], [X - 1, Y], [X, Y + 1], [X + 1, Y + 1]])
        self.positions.append([[X, Y], [X, Y + 1], [X + 1, Y], [X + 1, Y - 1]])
        self.num_rotations = len(self.positions)


class Figure7(Figure):
    def __init__(self, X, Y, ind):
        super().__init__(X, Y, ind)
        self.initialise_pos(self.x, self.y)

    def initialise_pos(self, X, Y):
        self.positions.append([[X, Y], [X + 1, Y], [X, Y + 1], [X - 1, Y + 1]])
        self.positions.append([[X, Y], [X, Y + 1], [X - 1, Y], [X - 1, Y - 1]])
        self.num_rotations = len(self.positions)


class MainGame:
    def __init__(self):
        self.run = True
        self.need_new_figure = True
        self.end_game = False
        self.black_color = (0, 0, 0)
        self.block_bg_img = pygame.image.load("media\BLOCK.png").convert_alpha()
        self.text_surface = myfont.render('Score: 0', False, (0, 255, 255))
        self.end_text = myfont.render('GAME OVER', False, (0, 255, 255))
        self.figure = Figure7(4, 1, 0)
        self.bg_bonus = 20
        self.num_block_x = 10
        self.num_block_y = 25
        self.block_size = 30
        self.start_pos_x = 4
        self.start_pos_y = 1
        self.speed = 240
        self.figures_used = 0
        self.num_points = 0
        self.field = []
        self.field_color = []

    def draw_image(self, image, x, y):
        window.blit(image, (x, y))

    def render_text(self, num):
        self.text_surface = myfont.render('Score: ' + str(num), False, (0, 255, 255))

    def redraw(self):
        window.fill(self.black_color)

        if not self.end_game:

            for i in range(0, self.num_block_x):
                for j in range(0, self.num_block_y):
                    if self.field[i][j] == -1:
                        self.draw_image(self.block_bg_img, self.bg_bonus + i * self.block_size, self.bg_bonus + j *
                                        self.block_size)
                    else:
                        self.draw_image(block_images[self.field_color[i][j]], self.bg_bonus + i * self.block_size,
                                        self.bg_bonus + j * self.block_size)
            j = self.figure.current_rotation
            for i in range(0, len(self.figure.positions[j])):
                self.draw_image(self.figure.block_img, self.bg_bonus + self.figure.positions[j][i][0] * self.block_size,
                                self.bg_bonus + self.figure.positions[j][i][1] * self.block_size)
            self.draw_image(self.text_surface, self.bg_bonus + 10, self.bg_bonus)
        else:
            self.draw_image(self.end_text, self.bg_bonus + 10, self.bg_bonus)
        pygame.display.update()

    def new_figure(self):
        x = random.randrange(0, 7)
        col = random.randrange(0, 5)
        if x == 0:
            self.figure = Figure1(self.start_pos_x, self.start_pos_y, col)
        elif x == 1:
            self.figure = Figure2(self.start_pos_x, self.start_pos_y, col)
        elif x == 2:
            self.figure = Figure3(self.start_pos_x, self.start_pos_y, col)
        elif x == 3:
            self.figure = Figure4(self.start_pos_x, self.start_pos_y, col)
        elif x == 4:
            self.figure = Figure5(self.start_pos_x, self.start_pos_y, col)
        elif x == 5:
            self.figure = Figure6(self.start_pos_x, self.start_pos_y, col)
        elif x == 6:
            self.figure = Figure7(self.start_pos_x, self.start_pos_y, col)

    def create_field(self):
        self.field.clear()
        self.field_color.clear()
        for i in range(self.num_block_x):
            L1 = []
            L2 = []
            for j in range(self.num_block_y):
                L1.append(-1)
                L2.append(0)
            self.field.append(L1)
            self.field_color.append(L2)

    def place_figure(self):
        j = self.figure.current_rotation
        for i in range(0, len(self.figure.positions[j])):
            n_x = self.figure.positions[j][i][0]
            n_y = self.figure.positions[j][i][1]
            self.field[n_x][n_y] = self.figures_used
            self.field_color[n_x][n_y] = self.figure.color_index

    def check_for_points(self):
        l = []
        for j in range(self.num_block_y - 1, - 1, -1):
            w = True
            for i in range(0, self.num_block_x):
                if self.field[i][j] == -1:
                    w = False
            if w:
                l.append(j)

        ind1 = self.num_block_y - 1
        for ind2 in range(self.num_block_y - 1, -1, -1):
            if ind2 not in l:
                for i in range(0, self.num_block_x):
                    self.field[i][ind1] = self.field[i][ind2]
                    self.field_color[i][ind1] = self.field_color[i][ind2]

                ind1 -= 1

        self.num_points += len(l)
        self.render_text(self.num_points)

    def check_for_break(self, w):
        if w:
            self.need_new_figure = True
            self.place_figure()
            self.check_for_points()

    def check_for_end(self, w):
        if w:
            self.end_game = True

    def mainloop(self):
        cnt = 0
        self.create_field()

        while self.run:
            if not self.end_game:
                cnt += 1
                if cnt == self.speed:
                    w = self.figure.change_pos(0, 1, self.num_block_x, self.num_block_y, self.field, self.figures_used)
                    self.check_for_break(w)
                    cnt = 0

                if self.need_new_figure:
                    self.need_new_figure = False
                    self.new_figure()
                    self.figures_used += 1

                    w = self.figure.change_pos(0, 0, self.num_block_x, self.num_block_y, self.field, self.figures_used)
                    self.check_for_end(w)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        w = self.figure.change_pos(-1, 0, self.num_block_x, self.num_block_y, self.field,
                                                   self.figures_used)
                        self.check_for_break(w)

                    if event.key == pygame.K_d:
                        w = self.figure.change_pos(+1, 0, self.num_block_x, self.num_block_y, self.field,
                                                   self.figures_used)
                        self.check_for_break(w)

                    if event.key == pygame.K_w:
                        self.figure.rotate(self.num_block_x, self.num_block_y, self.field, self.figures_used)

                    if event.key == pygame.K_s:
                        self.speed /= 4
                        cnt = 0
                    if self.end_game and event.key == pygame.K_SPACE:
                        self.end_game = False
                        self.num_points = 0
                        self.create_field()
                        self.need_new_figure = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_s:
                        self.speed *= 4
                        cnt = 0

            self.redraw()


g = MainGame()
g.mainloop()
