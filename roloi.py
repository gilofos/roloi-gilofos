import pygame
import math
import datetime

# Ρυθμίσεις Εμφάνισης
WIDTH, HEIGHT = 700, 700
CENTER = (WIDTH // 2, HEIGHT // 2)
BG_COLOR = (240, 240, 240)  # Απαλό γκρι φόντο
CLOCK_FACE = (255, 255, 255) # Καθαρό λευκό καντράν

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Luxury Clock - ΓΗΛΟΦΟΣ")

# Γραμματοσειρές
font_text = pygame.font.SysFont("Georgia", 32, italic=True, bold=True)
font_nums = pygame.font.SysFont("Times New Roman", 35)

def draw_clock():
    # 1. Εξωτερικό Στεφάνι
    pygame.draw.circle(screen, (40, 40, 40), CENTER, 310, 10)
    pygame.draw.circle(screen, CLOCK_FACE, CENTER, 300)
    
    # 2. Γραμμές Λεπτών/Ωρών (Ticks)
    for i in range(60):
        angle = math.radians(i * 6 - 90)
        line_len = 20 if i % 5 == 0 else 10
        thickness = 4 if i % 5 == 0 else 1
        start_x = CENTER[0] + 280 * math.cos(angle)
        start_y = CENTER[1] + 280 * math.sin(angle)
        end_x = CENTER[0] + 300 * math.cos(angle)
        end_y = CENTER[1] + 300 * math.sin(angle)
        pygame.draw.line(screen, (50, 50, 50), (start_x, start_y), (end_x, end_y), thickness)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill(BG_COLOR)
    draw_clock()
    
    # Λήψη Ώρας
    now = datetime.datetime.now()
    # Sweep κίνηση για τα δευτερόλεπτα
    sec_angle = (now.second + now.microsecond / 1000000.0) * 6
    min_angle = (now.minute * 6) + (now.second * 0.1)
    hour_angle = (now.hour % 12 * 30) + (now.minute * 0.5)

    # Σχεδίαση Ωροδείκτη & Λεπτοδείκτη (Κομψοί μαύροι δείκτες)
    for ang, length, width, color in [(hour_angle, 180, 8, (20, 20, 20)), (min_angle, 250, 5, (40, 40, 40))]:
        rad = math.radians(ang - 90)
        end = (CENTER[0] + length * math.cos(rad), CENTER[1] + length * math.sin(rad))
        pygame.draw.line(screen, color, CENTER, end, width)

    # ΔΕΥΤΕΡΟΛΕΠΤΟΔΕΙΧΤΗΣ ΜΕ "ΓΗΛΟΦΟΣ"
    sec_rad = math.radians(sec_angle - 90)
    
    # Η λέξη ξαπλωτή πάνω στον δείκτη
    text_surf = font_text.render("ΓΗΛΟΦΟΣ", True, (180, 0, 0)) # Βαθύ κόκκινο
    # Περιστροφή ώστε να είναι παράλληλη με τον δείκτη (-90)
    rotated_text = pygame.transform.rotate(text_surf, -sec_angle - 90)
    
    # Θέση της λέξης (πιο κοντά στην άκρη)
    dist = 160 
    text_x = CENTER[0] + dist * math.cos(sec_rad)
    text_y = CENTER[1] + dist * math.sin(sec_rad)
    
    # Λεπτός κόκκινος δείκτης
    sec_end = (CENTER[0] + 270 * math.cos(sec_rad), CENTER[1] + 270 * math.sin(sec_rad))
    pygame.draw.line(screen, (200, 0, 0), CENTER, sec_end, 2)
    
    # Εμφάνιση λέξης
    text_rect = rotated_text.get_rect(center=(text_x, text_y))
    screen.blit(rotated_text, text_rect)
    
    # Κεντρική "τάπα" (Το κέντρο του ρολογιού)
    pygame.draw.circle(screen, (20, 20, 20), CENTER, 10)
    pygame.draw.circle(screen, (200, 0, 0), CENTER, 5)

    pygame.display.flip()
    pygame.time.Clock().tick(60)
