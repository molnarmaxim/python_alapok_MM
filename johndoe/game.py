import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
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
    def __init__(self, name, base_cost, base_income, level=0):
        self.name = name
        self.level = level  # Start with a given level
        self.base_cost = base_cost
        self.base_income = base_income
        self.upgrade_cost = self.calculate_upgrade_cost()

    def calculate_upgrade_cost(self):
        return self.base_cost * (1.5 ** self.level)

    def upgrade(self):
        if self.level < 10:
            self.level += 1
            self.upgrade_cost = self.calculate_upgrade_cost()
            self.base_income *= 1.5  # Increase income by 50%

    def income(self):
        return self.base_income * (1.2 ** self.level) if self.level > 0 else 0  # No income if level 0

# Game variables
money = 0
prestige_points = 0
income_multiplier = 1.0
upgrade_animation = []
current_event = None
event_duration = 0
bonus_active = False
bonus_duration = 0

# Initialize businesses, Coffee Shop starts at level 1
businesses = [
    Business("Coffee Shop", 50, 2, level=1),  # Coffee Shop starts at level 1
    Business("Bakery", 100, 1),                # No income until upgraded
    Business("Restaurant", 200, 5),            # No income until upgraded
    Business("Clothing Store", 150, 2),        # No income until upgraded
    Business("Tech Startup", 500, 10),         # No income until upgraded
    Business("Real Estate", 1000, 20)          # No income until upgraded
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
        income_multiplier *= 1.002
        money = 0
        for business in businesses:
            business.level = 0  # Reset to level 0
            business.upgrade_cost = business.calculate_upgrade_cost()

# Function to trigger random events
def trigger_random_event():
    global current_event, event_duration
    event_type = random.choice(["Market Boom", "Market Crash"])
    if event_type == "Market Boom":
        current_event = "Market Boom: Income +50%!"
        event_duration = 300
    elif event_type == "Market Crash":
        current_event = "Market Crash: Income -30%!"
        event_duration = 300

# Function to trigger random bonuses
def trigger_random_bonus():
    global bonus_active, bonus_duration
    bonus_active = True
    bonus_duration = 180  # lasts for 3 minutes in frames

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
    draw_text(f"Income: ${int(business.income())}/s", font, BLACK, screen, x + 120, y + 100)
    draw_text(f"Upgrade Cost: ${int(business.upgrade_cost)}", font, BLACK, screen, x + 120, y + 130)

# Function to animate upgrade completion
def animate_upgrade():
    upgrade_animation.append({"pos": [SCREEN_WIDTH // 2 + 150, 40], "alpha": 255})

# Main game loop
clock = pygame.time.Clock()
income_rate = 0.1  # Adjust this value to control income frequency
frames_since_last_event = 0
frames_since_last_bonus = 0

while True:
    screen.fill(LIGHT_GRAY)

    # Handle events
    mouse_pos = pygame.mouse.get_pos()
    mouse_clicked = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_clicked = True

    # Continuous income generation
    income_multiplier_effect = 1.0
    if current_event == "Market Boom":
        income_multiplier_effect = 1.5
    elif current_event == "Market Crash":
        income_multiplier_effect = 0.7

    if bonus_active:
        income_multiplier_effect *= 1.2  # 20% bonus to income

    # Calculate income from the Coffee Shop only
    income = businesses[0].income() * income_multiplier_effect * income_rate
    money += income

    # Update animation positions and alpha
    for anim in upgrade_animation[:]:
        anim["pos"][1] -= 1  # Move up
        anim["alpha"] -= 5   # Fade out
        if anim["alpha"] <= 0:
            upgrade_animation.remove(anim)

    # Check achievements
    check_achievements()

    # Display money and prestige points prominently
    draw_text(f"Money: ${int(money)}", large_font, BLACK, screen, SCREEN_WIDTH // 2, 40)

    # Display upgrade animation next to the money display
    for anim in upgrade_animation:
        draw_text(f"+$ for Upgrade!", large_font, (0, 255, 0), screen, anim["pos"][0], anim["pos"][1])

    draw_text(f"Prestige Points: {prestige_points}", font, BLACK, screen, SCREEN_WIDTH // 2, 80)

    # Display current event above the businesses
    if current_event:
        draw_text(current_event, font, (255, 0, 0), screen, SCREEN_WIDTH // 2, 650)

    # Display businesses in two rows with three businesses each
    num_columns = 3
    card_height = 200
    spacing = 20
    for i, business in enumerate(businesses):
        col = i % num_columns
        row = i // num_columns
        x_offset = 20 + col * (260)
        y_offset = 100 + row * (card_height + spacing)

        if row == 1:
            y_offset += 50

        draw_business_card(business, x_offset, y_offset)

        # Button to upgrade business directly below the card
        upgrade_button = draw_button("Upgrade", x_offset + 50, y_offset + card_height + 10, 140, 40)

        # Change button color on hover
        if upgrade_button.collidepoint(mouse_pos):
            draw_button("Upgrade", x_offset + 50, y_offset + card_height + 10, 140, 40, BUTTON_HOVER_COLOR)

        # Handle button click
        if mouse_clicked and upgrade_button.collidepoint(mouse_pos) and money >= business.upgrade_cost:
            money -= business.upgrade_cost
            business.upgrade()
            animate_upgrade()

    # Button for resetting the game for prestige
    prestige_button = draw_button("Prestige", SCREEN_WIDTH - 150, SCREEN_HEIGHT - 100, 120, 40)

    if prestige_button.collidepoint(mouse_pos):
        draw_button("Prestige", SCREEN_WIDTH - 150, SCREEN_HEIGHT - 100, 120, 40, BUTTON_HOVER_COLOR)

    if mouse_clicked and prestige_button.collidepoint(mouse_pos):
        reset_for_prestige()

    # Trigger random events and bonuses
    frames_since_last_event += 1
    frames_since_last_bonus += 1
    if frames_since_last_event >= 600:
        trigger_random_event()
        frames_since_last_event = 0
    if frames_since_last_bonus >= 1200:
        trigger_random_bonus()
        frames_since_last_bonus = 0

    # Manage bonus duration
    if bonus_active:
        bonus_duration -= 1
        if bonus_duration <= 0:
            bonus_active = False

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
