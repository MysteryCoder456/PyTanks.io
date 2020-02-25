import pygame


def text(win, content, text_size, color, position):
    """Render Text

    Arguments:
        win {pygame.Surface} -- The surface to display the text on
        content {str} -- The stuff to display
        text_size {int} -- Size of the text
        color {tuple} -- Color of the text
        position {tuple} -- Position of the text on the surface
    """
    font = pygame.font.SysFont('Arial', text_size)
    screen_text = font.render(content, True, color)
    size = screen_text.get_size()
    position = (position[0] - size[0]/2, position[1] - size[1]/2)
    win.blit(screen_text, position)
