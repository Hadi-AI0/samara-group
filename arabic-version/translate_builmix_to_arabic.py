#!/usr/bin/env python3
import re

# Read the English version
with open('/workspace/en/builmix.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Arabic translations dictionary
translations = {
    # Navigation
    'About': 'من نحن',
    'Companies': 'الشركات',
    'Contact': 'اتصل بنا',
    'Samara H-VACR': 'سمارى للتكييف والتهوية والتبريد',
    'Samara Parking': 'سمارى لمواقف السيارات',
    'Saudi Builmix': 'بيلد ميكس السعودية',
    'Samara Real Estate': 'سمارى للعقارات',
    'Saryryah Healthcare': 'سريرية للرعاية الصحية',
    'Mahara Recruitment': 'مهارة للتوظيف',
    'Salmiya Oasis': 'واحة السلمية',
    
    # Hero section
    'Samara Group Company': 'شركة من مجموعة سمارى',
    'Innovative materials for stronger structures. Smart solutions for modern construction with advanced cement replacement materials.': 'مواد مبتكرة لهياكل أقوى. حلول ذكية للبناء الحديث مع مواد متقدمة بديلة للإسمنت.',
    'Years Experience': 'سنة خبرة',
    'Projects Supplied': 'مشروع تم توريدها',
    'Quality Assurance': 'ضمان الجودة',
    'Our Products': 'منتجاتنا',
    'Contact Us': 'اتصل بنا',
    
    # Common
    'Builmix Construction Materials': 'مواد البناء والتشييد بيلد ميكس',
}

# Apply translations
for en, ar in translations.items():
    # For text content between tags
    content = re.sub(r'>([^<]*?)' + re.escape(en) + r'([^<]*?)<', r'>\1' + ar + r'\2<', content)
    # For alt attributes
    content = re.sub(r'alt="' + re.escape(en) + r'"', r'alt="' + ar + '"', content)
    # For placeholder attributes
    content = re.sub(r'placeholder="' + re.escape(en) + r'"', r'placeholder="' + ar + '"', content)

# Fix html tag
content = content.replace('<html lang="en">', '<html lang="ar" dir="rtl">')

# Fix canonical and hreflang
content = content.replace('href="https://samara.co.com/en/builmix.html" />', 'href="https://samara.co.com/builmix" />')
content = content.replace('hreflang="ar" href="https://samara.co.com/builmix"', 'hreflang="ar" href="https://samara.co.com/builmix"')
content = content.replace('hreflang="en" href="https://samara.co.com/en/builmix.html"', 'hreflang="en" href="https://samara.co.com/en/builmix.html"')
content = content.replace('hreflang="x-default" href="https://samara.co.com/en/builmix.html"', 'hreflang="x-default" href="https://samara.co.com/builmix"')

# Remove ltr.css
content = content.replace('    <link rel="stylesheet" href="../css/ltr.css">\n', '')

# Fix title
content = content.replace('<title>Saudi Builmix | Samara Group</title>', '<title>بيلد ميكس السعودية | مجموعة سمارى</title>')

# Fix Samara Group alt
content = content.replace('alt="Samara Group"', 'alt="مجموعة سمارى"')

# Write the Arabic version
with open('/workspace/builmix.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Translated builmix.html to Arabic")
