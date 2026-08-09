#!/usr/bin/env python3
import re

# Read Arabic index.html
with open('/workspace/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Change html tag to English
content = re.sub(r'<html lang="ar" dir="rtl">', '<html lang="en" dir="ltr">', content)

# Update SEO tags for English version
seo_block = '''
  <!-- Canonical URL -->
  <link rel="canonical" href="https://samara.co.com/en/" />
  
  <!-- Alternate Language Versions -->
  <link rel="alternate" hreflang="ar" href="https://samara.co.com" />
  <link rel="alternate" hreflang="en" href="https://samara.co.com/en/" />
  <link rel="alternate" hreflang="x-default" href="https://samara.co.com/en/" />
'''

content = re.sub(
    r'<!-- Canonical URL -->.*?<link rel="preconnect" href="https://fonts\.googleapis\.com">',
    seo_block + r'\n  <link rel="preconnect" href="https://fonts.googleapis.com">',
    content,
    flags=re.DOTALL
)

# Add ltr.css after style-new.css
content = re.sub(
    r'(<link rel="stylesheet" href="style-new\.css">)',
    r'\1\n  <link rel="stylesheet" href="css/ltr.css">',
    content
)

# Update meta description to English
content = re.sub(
    r'<meta name="description" content="[^"]*">',
    '<meta name="description" content="Samara Group - Building Saudi Arabia\'s Future. A diversified family business group with over 40 years of excellence across the GCC.">',
    content
)

# Update title to English
content = re.sub(
    r'<title>[^<]*</title>',
    '<title>Samara Group | Building Saudi Arabia\'s Future</title>',
    content
)

# Write English index.html
with open('/workspace/en/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Created /workspace/en/index.html")
