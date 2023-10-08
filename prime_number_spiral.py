import pygame
import sys
import math


class PrimeSpiral:
    """Simple class to manage the prime spiral"""
    def __init__(self):
        """Initialize assets"""
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.bg_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        self.dot_color = (255, 255, 255)
        self.line_color = (50, 50, 50)

        pygame.display.set_caption("Prime Spiral")

        self.current_x, self.current_y = self.screen_width / 2, self.screen_height / 2
        self.last_prime_x, self.last_prime_y = -1, -1
        # Change this number for zoomed in/out
        self.space_width = self.space_height = 5
        self.current_number, self.step = 2, 1
        self.dot_rect = pygame.Rect(0, 0, 2, 2)
        self.dot_rect.x = self.current_x
        self.dot_rect.y = self.current_y

        self._create_spiral()

    def run_game(self):
        """Creates the main loop for the game"""
        while True:
            self._check_events()

    def _check_events(self):
        """Checks keyboard presses"""
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

    def _create_spiral(self):
        """Creates the prime spiral"""
        self.screen.fill(self.bg_color)
        while 0 <= self.current_x <= self.screen_width or 0 <= self.current_y <= self.screen_height:
            for i in range(math.ceil(self.step/2)):
                if self.step % 4 == 1:
                    self.current_x += self.space_width
                elif self.step % 4 == 2:
                    self.current_y -= self.space_height
                elif self.step % 4 == 3:
                    self.current_x -= self.space_width
                else:
                    self.current_y += self.space_height
                self.dot_rect.x = self.current_x
                self.dot_rect.y = self.current_y
                if is_prime(self.current_number):
                    pygame.draw.rect(self.screen, self.dot_color, self.dot_rect)
                    # if self.last_prime_x != -1:
                    #     pygame.draw.line(self.screen, self.line_color,
                    #             (self.last_prime_x, self.last_prime_y),
                    #             (self.current_x, self.current_y))
                    # self.last_prime_x, self.last_prime_y = self.current_x, self.current_y
                self.current_number += 1
            self.step += 1
        pygame.display.flip()


def is_prime(number):
    """Checks if number is prime"""
    for i in range(2, int(math.sqrt(number)+1)):
        if number % i == 0:
            return False
    return True


if __name__ == "__main__":
    # Create an instance of the game and run it"""
    game = PrimeSpiral()
    game.run_game()
