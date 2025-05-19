from PIL import ImageGrab

def check_game_status() -> bool:
    x1, y1 = 89, 319
    x2, y2 = x1 + 1, y1 + 1
    screenshot = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    pixel = screenshot.getpixel((0, 0))
    
    return pixel == (244, 47, 47)