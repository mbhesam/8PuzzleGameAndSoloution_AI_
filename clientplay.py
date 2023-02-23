import random
import easygui
import pygame


pygame.init()
pygame.font.init()

WIDTH = 600

win = pygame.display.set_mode((WIDTH, WIDTH))
TILE_SIZE = WIDTH // 3
font = pygame.font.SysFont("Arial", TILE_SIZE // 2)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Tile:
    def __init__(self, x, y, num, win):
        self.x = x
        self.y = y
        self.num = num
        self.win = win

    def draw(self):
        pygame.draw.rect(self.win, WHITE, (self.x, self.y, TILE_SIZE, TILE_SIZE))
        # Draw a border
        pygame.draw.rect(self.win, BLACK, (self.x, self.y, TILE_SIZE, TILE_SIZE), 5)
        text = font.render(str(self.num), True, BLACK)
        text_surf = text.get_rect(
            center=(self.x + TILE_SIZE // 2, self.y + TILE_SIZE // 2)
        )
        self.win.blit(text, text_surf)

    def update(self, tiles):
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            if (
                self.x < pos[0] < self.x + TILE_SIZE
                and self.y < pos[1] < self.y + TILE_SIZE
            ):
                self.move(tiles)

    def move(self, tiles):
        current = tiles.numbers.index(self.num)
        right = current + 1
        left = current - 1
        up = current - 3
        down = current + 3

        # Right
        if right < len(tiles.numbers) and right % 3 != 0 and tiles.numbers[right] == 0:
            tiles.numbers[right] = self.num
            tiles.numbers[current] = 0

        # Left
        elif left >= 0 and left % 3 != 2 and tiles.numbers[left] == 0:
            tiles.numbers[left] = self.num
            tiles.numbers[current] = 0

        # Up
        elif up >= 0 and tiles.numbers[up] == 0:
            tiles.numbers[up] = self.num
            tiles.numbers[current] = 0

        # Down
        elif down < len(tiles.numbers) and tiles.numbers[down] == 0:
            tiles.numbers[down] = self.num
            tiles.numbers[current] = 0

        tiles.make_tiles()

        if tiles.check_win():
            easygui.msgbox("You won! Press OK to play another Game.", "You won!")
            tiles.shuffle()


class Tiles:
    def __init__(self, win):
        self.win = win
        self.shuffle()

    def shuffle(self, nums=None):
        if nums:
            self.numbers = []
            if len(set(nums)) != len(nums):
                self.shuffle()
                return
            for i in nums:
                if 0 <= int(i) <= 8:
                    self.numbers.append(int(i))
        else:
            self.numbers = list(range(1, 9))
            random.shuffle(self.numbers)
            self.numbers.append(0)

        solvable = self.check_solvable(self.numbers)

        if not solvable:
            self.shuffle()

        self.make_tiles()

    def make_tiles(self):
        self.tiles = []
        for i, num in enumerate(self.numbers):
            if num != 0:
                self.tiles.append(
                    Tile(TILE_SIZE * (i % 3), TILE_SIZE * (i // 3), num, self.win)
                )

    def check_win(self):
        if self.numbers[-1] != 0:
            return False
        for i, num in enumerate(self.numbers[:-1]):
            if num != i + 1:
                return False

        return True

    def check_solvable(self, puzzle: list):
        inversions = 0
        puzzle = [i for i in puzzle if i != 0]

        for i in range(len(puzzle)):
            for j in range(i + 1, len(puzzle)):
                if puzzle[j] > puzzle[i]:
                    inversions += 1

        return inversions % 2 == 0

    def solve(self):
        random.choice(self.tiles).move()

    def draw(self):
        for tile in self.tiles:
            tile.draw()
            tile.update(self)

