from PIL import Image, ImageDraw, ImageFont
import os

def text_wrap(text, font, max_width):
    lines = []
    if font.getlength(text) <= max_width:
        lines.append(text)
    else:
        words = text.split(' ')
        i = 0
        while i < len(words):
            line = ''
            while i < len(words) and font.getlength(line + words[i]) <= max_width:
                line = line + words[i] + ' '
                i += 1
            if not line:
                line = words[i]
                i += 1
            lines.append(line.strip())
    return lines

def generate_image():
    width, height = 1024, 1024
    bg_color = (10, 20, 50)  # Dark navy
    card_bg = (25, 35, 70)
    text_color = (240, 240, 240)
    accent_colors = [(220, 50, 50), (50, 150, 220), (220, 220, 50), (50, 200, 100)]
    
    img = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(img)
    
    font_bold_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    font_reg_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    
    headline_font = ImageFont.truetype(font_bold_path, 80)
    subhead_font = ImageFont.truetype(font_reg_path, 30)
    card_label_font = ImageFont.truetype(font_bold_path, 34)
    card_text_font = ImageFont.truetype(font_reg_path, 26)
    
    # Header
    draw.text((width//2, 100), "20 NOVEMBER 2026", fill=text_color, font=headline_font, anchor="mm")
    draw.text((width//2, 160), "FRIDAY · WORLD NEWS", fill=text_color, font=subhead_font, anchor="mm")
    
    stories = [
        {
            "label": "MISSILES IN POLAND",
            "summary": "Russian missiles and drones landed in Poland during Nato's postwar-planning drills; Tusk calls it deliberate provocation."
        },
        {
            "label": "UK-EU RESET",
            "summary": "Britain and the EU held their first joint summit in years in Brussels, agreeing food, security and youth-mobility deals a decade after Brexit."
        },
        {
            "label": "ITALY GENERAL STRIKE",
            "summary": "Tens of thousands of workers and students rallied across Italy as the CGIL union struck over wages and public services."
        },
        {
            "label": "COP31 ENDGAME",
            "summary": "Climate talks in Antalya hit their final day as a bloc of countries demands stronger fossil-fuel action and more climate finance."
        }
    ]
    
    card_margin = 40
    card_width = (width - 3 * card_margin) // 2
    card_height = 350
    grid_start_y = 250
    
    for i, story in enumerate(stories):
        row = i // 2
        col = i % 2
        
        x1 = card_margin + col * (card_width + card_margin)
        y1 = grid_start_y + row * (card_height + card_margin)
        x2 = x1 + card_width
        y2 = y1 + card_height
        
        # Card background
        draw.rectangle([x1, y1, x2, y2], fill=card_bg)
        # Accent bar
        draw.rectangle([x1, y1, x1 + 10, y2], fill=accent_colors[i])
        
        # Label
        label_y = y1 + 30
        draw.text((x1 + 30, label_y), story['label'], fill=text_color, font=card_label_font)
        
        # Summary
        summary_y = label_y + 60
        max_summary_width = card_width - 60
        wrapped_lines = text_wrap(story['summary'], card_text_font, max_summary_width)
        
        # Draw 2 lines max as requested
        for j, line in enumerate(wrapped_lines[:5]):
            draw.text((x1 + 30, summary_y + j * 38), line, fill=text_color, font=card_text_font)
            
    img.save("entry.png")
    print("entry.png generated successfully.")

if __name__ == "__main__":
    generate_image()
