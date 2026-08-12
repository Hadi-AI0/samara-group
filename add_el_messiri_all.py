#!/usr/bin/env python3
import re
import os

def add_el_messiri_font(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Find the Manrope font link and add El Messiri after it
    old_text = '<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">'
    new_text = '''<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css2?family=El+Messiri:wght@400;500;600;700&display=swap" rel="stylesheet">'''
    
    content = content.replace(old_text, new_text)
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added El Messiri font: {filepath}")
        return True
    return False

# Fix all Arabic HTML files (root level)
arabic_files = [
    '/workspace/index.html',
    '/workspace/builmix.html',
    '/workspace/mahara-recruitment.html',
    '/workspace/salmiya-oasis.html',
    '/workspace/samara-H-VACR.html',
    '/workspace/samara-parking.html',
    '/workspace/samara-real-estate.html',
    '/workspace/saryryah-healthcare.html',
]

for filepath in arabic_files:
    if os.path.exists(filepath):
        add_el_messiri_font(filepath)

print("Done adding El Messiri font!")
