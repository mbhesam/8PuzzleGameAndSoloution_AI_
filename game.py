import clientplay
import easygui
import pygame
WIDTH = 600
win = pygame.display.set_mode((WIDTH, WIDTH))
tiles = clientplay.Tiles(win)
if __name__ == '__main__':
    while True:
        win.fill((128, 128, 128))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    tiles.shuffle()
                elif event.key == pygame.K_e:
                    nums = easygui.multenterbox(
                        f"Replace Empty cell with 0. If what you entered is not valid or is not solvable it will generate a random one.",
                        fields=[str(i) for i in range(1, 10)],
                    )
                    tiles.shuffle(nums)
                elif event.key == pygame.K_s:
                    tiles.solve()
        tiles.draw()
        pygame.display.flip()
