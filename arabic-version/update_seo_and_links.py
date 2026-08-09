#!/usr/bin/env python3
import os
import re

# Page mappings
pages = {
    'index.html': {'ar_title': 'مجموعة سمارة | بناء مستقبل المملكة العربية السعودية', 'en_title': 'Samara Group | Building Saudi Arabia\'s Future'},
    'builmix.html': {'ar_title': 'سعودي بيلد ميكس | مجموعة سمارة', 'en_title': 'Saudi Builmix | Samara Group'},
    'mahara-recruitment.html': {'ar_title': 'مهرة للتوظيف | مجموعة سمارة', 'en_title': 'Mahara Recruitment | Samara Group'},
    'salmiya-oasis.html': {'ar_title': 'سلمية واحة | مجموعة سمارة', 'en_title': 'Salmiya Oasis | Samara Group'},
    'samara-H-VACR.html': {'ar_title': 'سمارة للتكييف والتبريد | مجموعة سمارة', 'en_title': 'Samara H-VACR | Samara Group'},
    'samara-parking.html': {'ar_title': 'سمارة لحلول مواقف السيارات | مجموعة سمارة', 'en_title': 'Samara Parking Solutions | Samara Group'},
    'samara-real-estate.html': {'ar_title': 'سمارة للعقارات | مجموعة سمارة', 'en_title': 'Samara Real Estate | Samara Group'},
    'saryryah-healthcare.html': {'ar_title': 'سريرة للرعاية الصحية | مجموعة سمارة', 'en_title': 'Saryryah Healthcare | Samara Group'},
}

def get_canonical_url(filename):
    """Get canonical URL for a page"""
    if filename == 'index.html':
        return 'https://samara.co.com'
    else:
        # Convert filename to lowercase for URL
        name = filename.replace('.html', '').lower()
        return f'https://samara.co.com/{name}'

def get_en_url(filename):
    """Get English version URL for a page"""
    if filename == 'index.html':
        return 'https://samara.co.com/en/'
    else:
        name = filename.replace('.html', '').lower()
        return f'https://samara.co.com/en/{name}.html'

def get_ar_url(filename):
    """Get Arabic version URL for a page"""
    if filename == 'index.html':
        return 'https://samara.co.com'
    else:
        name = filename.replace('.html', '').lower()
        return f'https://samara.co.com/{name}'

def update_arabic_page(filepath, filename):
    """Update Arabic page with proper SEO headers"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Get title info
    title_info = pages.get(filename, pages['index.html'])
    
    # Build SEO header block
    seo_block = f'''  <!-- Canonical URL -->
  <link rel="canonical" href="{get_ar_url(filename)}" />
  
  <!-- Alternate Language Versions -->
  <link rel="alternate" hreflang="ar" href="{get_ar_url(filename)}" />
  <link rel="alternate" hreflang="en" href="{get_en_url(filename)}" />
  <link rel="alternate" hreflang="x-default" href="{get_ar_url(filename)}" />
  
  <link rel="preconnect" href="https://fonts.googleapis.com">'''
    
    # Replace the preconnect line with SEO block + preconnect
    content = re.sub(
        r'\s*<!-- Canonical URL -->.*?<link rel="preconnect" href="https://fonts\.googleapis\.com">',
        seo_block,
        content,
        flags=re.DOTALL
    )
    
    # If no canonical URL exists, add it after the title
    if '<link rel="canonical"' not in content:
        content = re.sub(
            r'(<title>.*?</title>\s*)',
            rf'\1{seo_block}',
            content,
            flags=re.DOTALL
        )
    
    # Update CSS to include style-new.css only (Arabic doesn't need ltr.css)
    # Make sure we're not loading ltr.css
    content = re.sub(r'<link rel="stylesheet" href="css/ltr\.css">\s*', '', content)
    
    # Update navigation links to point to English versions in /en/ folder
    # For company dropdown menu items
    for page_file in pages.keys():
        if page_file == 'index.html':
            continue
        page_name = page_file.replace('.html', '')
        # Update links in navigation to point to ../en/ for English pages when in subfolder context
        # But for root Arabic pages, links stay the same (pointing to other Arabic pages)
        pass
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  Updated Arabic page: {filename}")

def update_english_page(filepath, filename):
    """Update English page with proper SEO headers and LTR CSS"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Get title info
    title_info = pages.get(filename, pages['index.html'])
    
    # Build SEO header block for English
    seo_block = '''  <!-- Canonical URL -->
  <link rel="canonical" href="''' + get_en_url(filename) + '''" />
  
  <!-- Alternate Language Versions -->
  <link rel="alternate" hreflang="ar" href="''' + get_ar_url(filename) + '''" />
  <link rel="alternate" hreflang="en" href="''' + get_en_url(filename) + '''" />
  <link rel="alternate" hreflang="x-default" href="''' + get_en_url(filename) + '''" />
  
  <link rel="preconnect" href="https://fonts.googleapis.com">'''
    
    # Replace or add SEO block
    if '<link rel="canonical"' in content:
        content = re.sub(
            r'\s*<!-- Canonical URL -->.*?<link rel="preconnect" href="https://fonts\.googleapis\.com">',
            seo_block,
            content,
            flags=re.DOTALL
        )
    else:
        content = re.sub(
            r'(<title>.*?</title>\s*)',
            rf'\1{seo_block}',
            content,
            flags=re.DOTALL
        )
    
    # Add ltr.css after style-new.css
    content = re.sub(
        r'(<link rel="stylesheet" href="style-new\.css">)',
        r'\1\n    <link rel="stylesheet" href="css/ltr.css">',
        content
    )
    
    # Update navigation links to use ../ for parent directory references
    # Since English pages are in /en/ folder, they need to reference root for assets
    content = re.sub(r'href="samara-logo-group\.png"', r'href="../samara-logo-group.png"', content)
    content = re.sub(r'href="style-new\.css"', r'href="../style-new.css"', content)
    content = re.sub(r'href="css/ltr\.css"', r'href="../css/ltr.css"', content)
    content = re.sub(r'href="script-new\.js"', r'href="../script-new.js"', content)
    content = re.sub(r'href="webp_images/', r'href="../webp_images/', content)
    
    # Update navigation links to other pages - add ../ prefix
    for page_file in pages.keys():
        if page_file == 'index.html':
            content = re.sub(r'href="index\.html', r'href="../index.html', content)
        else:
            page_name = page_file.replace('.html', '')
            # Don't update links that already have ../ prefix
            content = re.sub(r'href="(?!../)' + page_name + r'\.html', r'href="../' + page_name + '.html', content)
    
    # Update anchor links to index.html sections
    content = re.sub(r'href="index\.html#', r'href="../index.html#', content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  Updated English page: {filename}")

# Process all pages
print("Updating Arabic pages at root...")
for filename in pages.keys():
    filepath = os.path.join('/workspace', filename)
    if os.path.exists(filepath):
        update_arabic_page(filepath, filename)

print("\nUpdating English pages in /en/ folder...")
for filename in pages.keys():
    filepath = os.path.join('/workspace/en', filename)
    if os.path.exists(filepath):
        update_english_page(filepath, filename)

print("\nDone!")
