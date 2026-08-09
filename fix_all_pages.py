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
    
    # Build proper SEO block with newlines
    if is_english:
        seo_block = '''
  <!-- Canonical URL -->
  <link rel="canonical" href="''' + get_en_url(filename) + '''" />
  
  <!-- Alternate Language Versions -->
  <link rel="alternate" hreflang="ar" href="''' + get_ar_url(filename) + '''" />
  <link rel="alternate" hreflang="en" href="''' + get_en_url(filename) + '''" />
  <link rel="alternate" hreflang="x-default" href="''' + get_en_url(filename) + '''" />
'''
    else:
        seo_block = '''
  <!-- Canonical URL -->
  <link rel="canonical" href="''' + get_ar_url(filename) + '''" />
  
  <!-- Alternate Language Versions -->
  <link rel="alternate" hreflang="ar" href="''' + get_ar_url(filename) + '''" />
  <link rel="alternate" hreflang="en" href="''' + get_en_url(filename) + '''" />
  <link rel="alternate" hreflang="x-default" href="''' + get_ar_url(filename) + '''" />
'''
    
    # Replace title and everything until preconnect with proper structure
    content = re.sub(
        r'(<title>[^<]*</title>).*?(<link rel="preconnect" href="https://fonts\.googleapis\.com">)',
        r'\1' + seo_block + r'\n  \2',
        content,
        flags=re.DOTALL
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    lang = "English" if is_english else "Arabic"
    print(f"  Fixed {lang} page: {filename}")

# Fix all pages
print("Fixing Arabic pages at root...")
for filename in pages:
    filepath = os.path.join('/workspace', filename)
    if os.path.exists(filepath):
        fix_page(filepath, is_english=False)

print("\nFixing English pages in /en/ folder...")
for filename in pages:
    filepath = os.path.join('/workspace/en', filename)
    if os.path.exists(filepath):
        fix_page(filepath, is_english=True)

print("\nDone!")
