import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800  # Height of the window
WHITE = (255, 255, 255)
BLACK = (30, 30, 30)
LIGHT_GRAY = (240, 240, 240)
BUTTON_COLOR = (70, 130, 180)
BUTTON_HOVER_COLOR = (100, 150, 200)
FONT_SIZE = 30
LARGE_FONT_SIZE = 50
CARD_COLOR = (255, 255, 255)
SHADOW_COLOR = (200, 200, 200)

# Business class
class Business:
    def __init__(self, name, base_cost, base_income):
        self.name = name
        self.level = 1
        self.base_cost = base_cost
        self.base_income = base_income
        self.upgrade_cost = base_cost * 2

    def upgrade(self):
        if self.level < 10:  # Increased maximum level
            self.level += 1
            self.upgrade_cost *= 2  # Double the upgrade cost for the next level

    def income(self):
        return self.base_income * (2 ** (self.level - 1))  # Dynamic income based on level

# Game variables
money = 0
prestige_points = 0
income_multiplier = 1.0
businesses = [
    Business("Coffee Shop", 10, 1),
    Business("Bakery", 20, 2),
    Business("Restaurant", 50, 5),
    Business("Clothing Store", 30, 3),
    Business("Tech Startup", 100, 10),
    Business("Real Estate", 200, 20)
]

# Achievements tracking
achievements = []
achievements_reached = set()

def check_achievements():
    global achievements_reached
    if money >= 100 and "Reached $100" not in achievements_reached:
        achievements.append("Reached $100")
        achievements_reached.add("Reached $100")
    if money >= 1000 and "Reached $1000" not in achievements_reached:
        achievements.append("Reached $1000")
        achievements_reached.add("Reached $1000")
    if all(b.level == 10 for b in businesses) and "Max Level All Businesses" not in achievements_reached:
        achievements.append("Max Level All Businesses")
        achievements_reached.add("Max Level All Businesses")
    if prestige_points > 0 and "Prestige Points Earned" not in achievements_reached:
        achievements.append("Prestige Points Earned")
        achievements_reached.add("Prestige Points Earned")
    if money >= 5000 and "Reached $5000" not in achievements_reached:
        achievements.append("Reached $5000")
        achievements_reached.add("Reached $5000")
    if any(b.level == 10 for b in businesses) and "One Business at Max Level" not in achievements_reached:
        achievements.append("One Business at Max Level")
        achievements_reached.add("One Business at Max Level")
    if len(achievements) > 5 and "Collector of Achievements" not in achievements_reached:
        achievements.append("Collector of Achievements")
        achievements_reached.add("Collector of Achievements")

# Function to reset the game for prestige points
def reset_for_prestige():
    global money, prestige_points, income_multiplier
    if all(b.level == 10 for b in businesses):
        prestige_points += 1
        income_multiplier *= 1.002  # Increase income by 0.2%
        money = 0
        for business in businesses:
            business.level = 1
            business.upgrade_cost = business.base_cost * 2

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tycoon Game")

# Load fonts
font = pygame.font.Font(None, FONT_SIZE)
large_font = pygame.font.Font(None, LARGE_FONT_SIZE)

# Function to draw text
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect(center=(x, y))
    surface.blit(textobj, textrect)

# Function to draw a button
def draw_button(text, x, y, width, height, color=BUTTON_COLOR):
    button_rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, color, button_rect, border_radius=10)
    draw_text(text, font, WHITE, screen, x + width // 2, y + height // 2)
    return button_rect

# Function to draw a business card
def draw_business_card(business, x, y):
    card_rect = pygame.Rect(x, y, 240, 200)
    pygame.draw.rect(screen, CARD_COLOR, card_rect, border_radius=10)
    pygame.draw.rect(screen, SHADOW_COLOR, card_rect.move(5, 5), border_radius=10)
    draw_text(f"{business.name}", font, BLACK, screen, x + 120, y + 30)
    draw_text(f"Level: {business.level}", font, BLACK, screen, x + 120, y + 70)
    draw_text(f"Income: ${int(business.income() * income_multiplier)}/s", font, BLACK, screen, x + 120, y + 100)
    draw_text(f"Upgrade Cost: ${business.upgrade_cost}", font, BLACK, screen, x + 120, y + 130)

# Main game loop
clock = pygame.time.Clock()
while True:
    screen.fill(LIGHT_GRAY)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Collect income every second
    money += sum(business.income() * income_multiplier for business in businesses) / 60  # 60 FPS

    # Check achievements
    check_achievements()

    # Display money and prestige points prominently
    draw_text(f"Money: ${int(money)}", large_font, BLACK, screen, SCREEN_WIDTH // 2, 40)
    draw_text(f"Prestige Points: {prestige_points}", font, BLACK, screen, SCREEN_WIDTH // 2, 80)

    # Display businesses in two rows with three businesses each
    num_columns = 3
    card_height = 200
    spacing = 20
    for i, business in enumerate(businesses):
        col = i % num_columns
        row = i // num_columns
        x_offset = 20 + col * (260)  # Space out columns
        y_offset = 100 + row * (card_height + spacing)  # Space out rows

        # Move the second row down by an additional 50 pixels
        if row == 1:
            y_offset += 50

        draw_business_card(business, x_offset, y_offset)

        # Button to upgrade business directly below the card
        upgrade_button = draw_button("Upgrade", x_offset + 50, y_offset + card_height + 10, 140, 40)

        # Change button color on hover
        mouse_pos = pygame.mouse.get_pos()
        if upgrade_button.collidepoint(mouse_pos):
            upgrade_button = draw_button("Upgrade", x_offset + 50, y_offset + card_height + 10, 140, 40, BUTTON_HOVER_COLOR)

        # Handle button click
        if event.type == pygame.MOUSEBUTTONDOWN:
            if upgrade_button.collidepoint(mouse_pos) and money >= business.upgrade_cost:
                money -= business.upgrade_cost
                business.upgrade()

    # Button for resetting the game for prestige
    prestige_button = draw_button("Prestige", SCREEN_WIDTH - 150, SCREEN_HEIGHT - 100, 120, 40)

    if prestige_button.collidepoint(mouse_pos):
        prestige_button = draw_button("Prestige", SCREEN_WIDTH - 150, SCREEN_HEIGHT - 100, 120, 40, BUTTON_HOVER_COLOR)

    if event.type == pygame.MOUSEBUTTONDOWN:
        if prestige_button.collidepoint(mouse_pos):
            reset_for_prestige()

    # Draw achievements just above the footer
    draw_text("Achievements:", font, BLACK, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100)
    for idx, achievement in enumerate(achievements):
        draw_text(achievement, font, BLACK, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT - 70 + idx * 30)

    # Draw a footer
    footer_rect = pygame.Rect(0, SCREEN_HEIGHT - 50, SCREEN_WIDTH, 50)
    pygame.draw.rect(screen, BLACK, footer_rect)
    draw_text("Click 'Upgrade' to enhance your businesses!", font, WHITE, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT - 25)

    # Update the display
    pygame.display.flip()
    clock.tick(60)
