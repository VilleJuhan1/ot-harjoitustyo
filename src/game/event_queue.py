import pygame


class EventQueue:
    """Keeps track of the keyboard presses and the possible exit inside the game
    """

    def get(self):
        """Returns a button press or an exit

        Returns:
            A pygame.event such as a KEY.DOWN or EXIT
        """
        return pygame.event.get()
