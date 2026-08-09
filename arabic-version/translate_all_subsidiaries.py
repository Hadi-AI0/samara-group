#!/usr/bin/env python3
import re
import os

# Translation mappings for each subsidiary page
translations_map = {
    'samara-H-VACR.html': {
        'title': 'سمارى للتكييف والتهوية والتبريد | مجموعة سمارى',
        'nav': {
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
        },
        'hero': {
            'Samara Group Company': 'شركة من مجموعة سمارى',
            'Advanced HVACR solutions for commercial and industrial applications.': 'حلول تكييف وتهوية وتبريد متقدمة للتطبيقات التجارية والصناعية.',
            'Years Experience': 'سنة خبرة',
            'Projects Completed': 'مشروع مكتمل',
            'Client Satisfaction': 'رضا العملاء',
            'Our Solutions': 'حلولنا',
            'Contact Us': 'اتصل بنا',
        }
    },
    'samara-parking.html': {
        'title': 'سمارى لمواقف السيارات | مجموعة سمارى',
        'nav': {
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
        },
        'hero': {
            'Samara Group Company': 'شركة من مجموعة سمارى',
            'Smart parking solutions for modern urban mobility. Automated systems for efficient space management.': 'حلول مواقف سيارات ذكية للتنقل الحضري الحديث. أنظمة آلية لإدارة المساحات بكفاءة.',
            'Years Experience': 'سنة خبرة',
            'Parking Spaces': 'موقف سيارات',
            'Smart Systems': 'نظام ذكي',
            'Our Systems': 'أنظمتنا',
            'Contact Us': 'اتصل بنا',
        }
    },
    'samara-real-estate.html': {
        'title': 'سمارى للعقارات | مجموعة سمارى',
        'nav': {
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
        },
        'hero': {
            'Samara Group Company': 'شركة من مجموعة سمارى',
            'Premium real estate development and contracting services. Building communities, shaping skylines.': 'خدمات تطوير عقاري ومقاولات متميزة. نبني المجتمعات، نشكل الآفاق.',
            'Years Experience': 'سنة خبرة',
            'Projects Delivered': 'مشروع تم تسليمه',
            'Square Meters Built': 'متر مربع تم بناؤه',
            'Our Projects': 'مشاريعنا',
            'Contact Us': 'اتصل بنا',
        }
    },
    'saryryah-healthcare.html': {
        'title': 'سريرية للرعاية الصحية | مجموعة سمارى',
        'nav': {
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
        },
        'hero': {
            'Samara Group Company': 'شركة من مجموعة سمارى',
            'Comprehensive healthcare services with a commitment to patient care excellence. Medical facilities across the Kingdom.': 'خدمات رعاية صحية شاملة مع الالتزام بالتميز في رعاية المرضى. مرافق طبية في جميع أنحاء المملكة.',
            'Years Experience': 'سنة خبرة',
            'Healthcare Facilities': 'مرفق رعاية صحية',
            'Patients Served Annually': 'مريض يتم خدمتهم سنوياً',
            'Our Services': 'خدماتنا',
            'Contact Us': 'اتصل بنا',
        }
    },
    'mahara-recruitment.html': {
        'title': 'مهارة للتوظيف | مجموعة سمارى',
        'nav': {
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
        },
        'hero': {
            'Samara Group Company': 'شركة من مجموعة سمارى',
            'Professional recruitment and HR solutions. Connecting talent with opportunities across the GCC.': 'حلول توظيف وموارد بشرية احترافية. نربط المواهب بالفرص في جميع أنحاء دول مجلس التعاون الخليجي.',
            'Years Experience': 'سنة خبرة',
            'Successful Placements': 'توظيف ناجح',
            'Corporate Clients': 'عميل من الشركات',
            'Our Services': 'خدماتنا',
            'Contact Us': 'اتصل بنا',
        }
    },
    'salmiya-oasis.html': {
        'title': 'واحة السلمية | مجموعة سمارى',
        'nav': {
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
        },
        'hero': {
            'Samara Group Company': 'شركة من مجموعة سمارى',
            'Hospitality and residential excellence. Creating comfortable living experiences in prime locations.': 'تميز في الضيافة والسكن. نخلق تجارب معيشية مريحة في مواقع متميزة.',
            'Years Experience': 'سنة خبرة',
            'Residential Units': 'وحدة سكنية',
            'Occupancy Rate': 'معدل الإشغال',
            'Explore': 'استكشف',
            'Contact Us': 'اتصل بنا',
        }
    },
}

def translate_file(filepath, translations):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix html tag
    content = content.replace('<html lang="en">', '<html lang="ar" dir="rtl">')
    
    # Fix title
    if 'title' in translations:
        content = re.sub(r'<title>[^<]+</title>', f'<title>{translations["title"]}</title>', content)
    
    # Fix canonical and hreflang
    basename = os.path.basename(filepath).replace('.html', '')
    content = content.replace(f'href="https://samara.co.com/en/{basename}.html" />', f'href="https://samara.co.com/{basename}" />')
    content = content.replace(f'hreflang="ar" href="https://samara.co.com/en/{basename}.html"', f'hreflang="ar" href="https://samara.co.com/{basename}"')
    content = content.replace(f'hreflang="x-default" href="https://samara.co.com/en/{basename}.html"', f'hreflang="x-default" href="https://samara.co.com/{basename}"')
    
    # Remove ltr.css
    content = content.replace('    <link rel="stylesheet" href="../css/ltr.css">\n', '')
    content = content.replace('  <link rel="stylesheet" href="../css/ltr.css">\n', '')
    
    # Apply nav translations
    if 'nav' in translations:
        for en, ar in translations['nav'].items():
            # For link text
            content = re.sub(r'>([^<]*?)' + re.escape(en) + r'([^<]*?)<', r'>\1' + ar + r'\2<', content)
            # For alt attributes  
            content = re.sub(r'alt="' + re.escape(en) + r'"', r'alt="' + ar + '"', content)
    
    # Apply hero translations
    if 'hero' in translations:
        for en, ar in translations['hero'].items():
            content = re.sub(r'>([^<]*?)' + re.escape(en) + r'([^<]*?)<', r'>\1' + ar + r'\2<', content)
            content = re.sub(r'alt="' + re.escape(en) + r'"', r'alt="' + ar + '"', content)
    
    # Fix Samara Group alt
    content = content.replace('alt="Samara Group"', 'alt="مجموعة سمارى"')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Translated {filepath}")

# Translate all subsidiary pages
for filename, translations in translations_map.items():
    filepath = f'/workspace/{filename}'
    if os.path.exists(filepath):
        translate_file(filepath, translations)

print("Done translating all subsidiary pages!")
