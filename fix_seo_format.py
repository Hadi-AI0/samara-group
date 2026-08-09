#!/usr/bin/env python3
import os
import re

pages = ['index.html', 'builmix.html', 'mahara-recruitment.html', 'salmiya-oasis.html', 
         'samara-H-VACR.html', 'samara-parking.html', 'samara-real-estate.html', 'saryryah-healthcare.html']

def get_ar_url(filename):
    if filename == 'index.html':
        return 'https://samara.co.com'
    else:
        name = filename.replace('.html', '').lower()
        return f'https://samara.co.com/{name}'

def get_en_url(filename):
    if filename == 'index.html':
        return 'https://samara.co.com/en/'
    else:
        name = filename.replace('.html', '').lower()
        return f'https://samara.co.com/en/{name}.html'

def fix_page(filepath, is_english=False):
    filename = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix duplicate preconnect issue
    content = re.sub(
        r'<link rel="preconnect" href="https://fonts\.googleapis\.com"><link rel="preconnect" href="https://fonts\.googleapis\.com">',
        r'<link rel="preconnect" href="https://fonts.googleapis.com">',
        content
    )
    
    # Build proper SEO block
    if is_english:
        seo_block = f'''  <!-- Canonical URL -->
  <link rel="canonical" href="{get_en_url(filename)}" />
  
  <!-- Alternate Language Versions -->
  <link rel="alternate" hreflang="ar" href="{get_ar_url(filename)}" />
  <link rel="alternate" hreflang="en" href="{get_en_url(filename)}" />
  <link rel="alternate" hreflang="x-default" href="{get_en_url(filename)}" />'''
    else:
        seo_block = f'''  <!-- Canonical URL -->
  <link rel="canonical" href="{get_ar_url(filename)}" />
  
  <!-- Alternate Language Versions -->
  <link rel="alternate" hreflang="ar" href="{get_ar_url(filename)}" />
  <link rel="alternate" hreflang="en" href="{get_en_url(filename)}" />
  <link rel="alternate" hreflang="x-default" href="{get_ar_url(filename)}" />'''
    
    # Replace existing SEO block
    content = re.sub(
        r'\s*<!-- Canonical URL -->\s*<link rel="canonical"[^>]*>\s*<!-- Alternate Language Versions -->\s*<link rel="alternate"[^>]*>\s*<link rel="alternate"[^>]*>\s*<link rel="alternate"[^>]*>',
        seo_block,
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    lang = "English" if is_english else "Arabic"
    print(f"  Fixed {lang} page: {filename}")

# Fix Arabic pages at root
print("Fixing Arabic pages at root...")
for filename in pages:
    filepath = os.path.join('/workspace', filename)
    if os.path.exists(filepath):
        fix_page(filepath, is_english=False)

# Fix English pages in /en/ folder
print("\nFixing English pages in /en/ folder...")
for filename in pages:
    filepath = os.path.join('/workspace/en', filename)
    if os.path.exists(filepath):
        fix_page(filepath, is_english=True)

print("\nDone!")
