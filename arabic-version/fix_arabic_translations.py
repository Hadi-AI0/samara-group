#!/usr/bin/env python3
"""
Fix Arabic pages - translate remaining English content and fix misspellings
"""

import os
import re

# Misspelling fixes
SPELLING_FIXES = {
    'salmiya': 'سالمية',
    'samara': 'سمارى',
    'H-VACR': 'تبريد و تكييف',
    'builmix': 'بيلميكس',
}

# Translation mappings for common phrases
TRANSLATIONS = {
    # Builmix translations
    'بيلميكس السعودية is a premier provider of construction chemicals and advanced building solutions.': 
        'بيلميكس السعودية هي شركة رائدة في مجال الكيماويات الإنشائية وحلول البناء المتقدمة.',
    'We are dedicated to enhancing the quality, durability, and sustainability of construction projects across the Kingdom.':
        'نحن ملتزمون بتحسين الجودة والمتانة والاستدامة لمشاريع البناء في جميع أنحاء المملكة.',
    'Our range of products, including Microsilica, Fly Ash, and GGBFS, meets the highest international standards.':
        'مجموعة منتجاتنا، بما في ذلك ميكروسيليكا والرماد المتطاير و GGBFS، تلبي أعلى المعايير الدولية.',
    'We deliver high-performance, cost-effective cement replacement materials for durable concrete.':
        'نقدم مواد بديلة للأسمنت عالية الأداء وفعالة من حيث التكلفة لخرسانة متينة.',
    'Count on us for expert technical support on mix designs and reliable supply throughout Saudi Arabia.':
        'اعتمد علينا للحصول على دعم فني خبير حول تصميمات الخلطات وإمدادات موثوقة في جميع أنحاء المملكة العربية السعودية.',
    'Our materials are trusted by professionals who demand consistency, performance, and reliability.':
        'موادنا موثوقة من قبل المهنيين الذين يطالبون بالاتساق والأداء والموثوقية.',
    'بيلميكس Microsilica is a high-pozzolanic activity densified microsilica for concrete and mortar, providing exceptional strength and durability.':
        'بيلميكس ميكروسيليكا هو ميكروسيليكا مكثف عالي النشاط البوزولاني للخرسانة والملاط، يوفر قوة ومتانة استثنائية.',
    'بيلميكس Fly Ash is a residue of coal combustion that occurs at power generation plants, used as a supplementary cementitious material.':
        'بيلميكس للرماد المتطاير هو بقايا احتراق الفحم الذي يحدث في محطات توليد الطاقة، ويستخدم كمادة اسمنتية تكميلية.',
    'بيلميكس GGBFS is a powder Ground Granulated Blast Furnace Slag that is used in concrete to enhance strength and reduce environmental impact.':
        'بيلميكس GGBFS هو مسحوق خبث الفرن العالي المحبب الأرضي الذي يستخدم في الخرسانة لتعزيز القوة وتقليل التأثير البيئي.',
    'Our materials are trusted by professionals who demand consistency, performance, and reliability in every project.':
        'موادنا موثوقة من قبل المهنيين الذين يطالبون بالاتساق والأداء والموثوقية في كل مشروع.',
    'At بيلميكس, quality control is a core principle. تخضع موادنا لاختبارات صارمة لتلبية المعايير ذات الصلة مع المساهمة في تقليل استخدام الأسمنت وخفض انبعاثات ثاني أكسيد الكربون.':
        'في بيلميكس، مراقبة الجودة هي مبدأ أساسي. تخضع موادنا لاختبارات صارمة لتلبية المعايير ذات الصلة مع المساهمة في تقليل استخدام الأسمنت وخفض انبعاثات ثاني أكسيد الكربون.',
    
    # Salmiya Oasis translations
    'واحة سالمية is Al-Khobar\'s premier event destination, offering an expansive 10,000 square meters of versatile space designed for corporate events, conferences, exhibitions, and large-scale gatherings.':
        'واحة سالمية هي وجهة الفعاليات الرائدة في الخبر، وتوفر مساحة متنوعة تبلغ 10,000 متر مربع مصممة للفعاليات الشركات والمؤتمرات والمعارض والتجمعات الكبيرة.',
    'Located in the heart of Al-Khobar, our state-of-the-art facility combines elegant design with modern amenities to create unforgettable experiences.':
        'تقع في قلب الخبر، وتجمع منشأتنا الحديثة بين التصميم الأنيق وسائل الراحة العصرية لخلق تجارب لا تُنسى.',
    'Our venue features multiple configurable halls equipped with advanced audiovisual systems, professional lighting, and high-speed connectivity.':
        'يتميز مكاننا بقاعات متعددة قابلة للتكوين مجهزة بأنظمة سمعية وبصرية متقدمة وإضاءة احترافية واتصال عالي السرعة.',
    'Whether hosting a product launch, annual conference, trade exhibition, or corporate celebration, our experienced events team provides comprehensive support from planning to execution, ensuring every detail exceeds expectations.':
        'سواء كنت تستضيف إطلاق منتج أو مؤتمرًا سنويًا أو معرضًا تجاريًا أو احتفالًا للشركات، فإن فريق الفعاليات ذو الخبرة لدينا يقدم دعمًا شاملاً من التخطيط إلى التنفيذ، مما يضمن تجاوز كل التفاصيل للتوقعات.',
    'Square Meters':
        'متر مربع',
    'Regional Healthcare Expo':
        'معرض الرعاية الصحية الإقليمي',
    'Three-day medical exhibition showcasing latest healthcare innovations with 50+ exhibitors and 1000+ visitor attendees.':
        'معرض طبي لمدة ثلاثة أيام يعرض أحدث ابتكارات الرعاية الصحية مع أكثر من 50 عارضًا وأكثر من 1000 زائر.',
    
    # Samara Parking translations
    'Our R&D systems are administered by experienced and scientifically-competent engineers in the automatic parking engineering field.':
        'يتم إدارة أنظمة البحث والتطوير الخاصة بنا من قبل مهندسين ذوي خبرة وكفاءة علمية في مجال هندسة مواقف السيارات الأوتوماتيكية.',
    'We continuously innovate to provide advanced and suitable solutions for the various needs of developing communities.':
        'نحن نبتكر باستمرار لتقديم حلول متقدمة ومناسبة للاحتياجات المختلفة للمجتمعات النامية.',
    
    # Samara Real Estate translations
    'Samara العقارات & Contracting is a premier developer and contractor within the Samara Group, specializing in residential, commercial, and mixed-use projects across the Kingdom of Saudi Arabia.':
        'سمارى للعقارات والمقاولات هي مطور ومقاول رائد ضمن مجموعة سمارى، متخصص في المشاريع السكنية والتجارية والاستخدامات المختلطة في جميع أنحاء المملكة العربية السعودية.',
    'With over 25 years of industry expertise, we deliver exceptional spaces that enhance communities and provide lasting value to investors and occupants alike.':
        'مع أكثر من 25 عامًا من الخبرة الصناعية، نقدم مساحات استثنائية تعزز المجتمعات وتوفر قيمة دائمة للمستثمرين والمقيمين على حد سواء.',
    
    # Saryryah Healthcare translations
    'سريرية للرعاية الصحية is a leading healthcare provider within the Samara Group, dedicated to delivering comprehensive medical services that improve community health and well-being across Saudi Arabia.':
        'سريرية للرعاية الصحية هي مقدم رعاية صحية رائد ضمن مجموعة سمارى، مكرس لتقديم خدمات طبية شاملة تحسن صحة المجتمع ورفاهيته في جميع أنحاء المملكة العربية السعودية.',
    'Our network of clinics and specialized centers offers accessible, patient-centered care with a focus on quality outcomes.':
        'شبكتنا من العيادات والمراكز المتخصصة تقدم رعاية سهلة الوصول تركز على المريض مع التركيز على نتائج الجودة.',
    'We bring together experienced physicians, nurses, and healthcare professionals who are committed to excellence in diagnosis, treatment, and preventive care.':
        'نجمع أطباء وممرضين ومحترفين في الرعاية الصحية ذوي خبرة ملتزمون بالتميز في التشخيص والعلاج والرعاية الوقائية.',
    'Our facilities are equipped with modern medical technology to ensure accurate diagnostics and effective treatments for diverse health conditions.':
        'مرافقنا مجهزة بتكنولوجيا طبية حديثة لضمان تشخيص دقيق وعلاجات فعالة لمختلف الحالات الصحية.',
    'Comprehensive healthcare solutions':
        'حلول رعاية صحية شاملة',
    'Expert care in cardiology, orthopedics, pediatrics, gynecology, dermatology, and other medical specialties.':
        'رعاية خبيرة في أمراض القلب وجراحة العظام وطب الأطفال وأمراض النساء والجلدية وغيرها من التخصصات الطبية.',
    'Healthcare delivery by the numbers':
        'تقديم الرعاية الصحية بالأرقام',
    
    # Mahara Recruitment translations
    'مهارة للتوظيف is a leading human resources solutions provider within the Samara Group, specializing in connecting exceptional talent with top-tier organizations across Saudi Arabia and Egypt.':
        'مهارة للتوظيف هي مقدم رائد لحلول الموارد البشرية ضمن مجموعة سمارى، متخصصة في ربط المواهب الاستثنائية مع المنظمات الرائدة في جميع أنحاء المملكة العربية السعودية ومصر.',
    'With over 15 years of industry expertise, we serve as a strategic bridge for businesses seeking skilled professionals in medical, engineering, technology, finance, and sales sectors.':
        'مع أكثر من 15 عامًا من الخبرة الصناعية، نعمل كجسر استراتيجي للشركات التي تبحث عن محترفين مهرة في القطاعات الطبية والهندسية والتكنولوجية والمالية والمبيعات.',
    'Specialized recruitment of doctors, nurses, technicians, and healthcare administrators for hospitals and clinics.':
        'توظيف متخصص للأطباء والممرضين والفنيين ومديري الرعاية الصحية للمستشفيات والعيادات.',
    'Healthcare Excellence':
        'التميز في الرعاية الصحية',
    
    # Index page translations
    'Comprehensive healthcare facilities with modern medical technology.':
        'مرافق رعاية صحية شاملة مع تكنولوجيا طبية حديثة.',
    'Samara التبريد provides industrial-grade cold rooms, freezers, refrigeration projects, maintenance services, and a full-service refrigeration workshop.':
        'سمارى للتبريد توفر غرف تبريد صناعية ومجمدات ومشاريع تبريد وخدمات صيانة وورشة تبريد كاملة الخدمات.',
    'Supporting food security across the Eastern Province since 1992.':
        'ندعم الأمن الغذائي في المنطقة الشرقية منذ عام 1992.',
}

def fix_spellings(content):
    """Fix misspellings in content"""
    for wrong, correct in SPELLING_FIXES.items():
        # Case insensitive replacement for URLs and filenames
        content = re.sub(re.escape(wrong), correct, content, flags=re.IGNORECASE)
    return content

def translate_content(content):
    """Translate English phrases to Arabic"""
    for english, arabic in TRANSLATIONS.items():
        content = content.replace(english, arabic)
    return content

def process_file(filepath):
    """Process a single HTML file"""
    print(f"Processing: {filepath}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Fix spellings
    content = fix_spellings(content)
    
    # Translate content
    content = translate_content(content)
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✓ Updated {filepath}")
    else:
        print(f"  - No changes needed")

def main():
    # Process Arabic pages (root level)
    arabic_pages = [
        '/workspace/builmix.html',
        '/workspace/salmiya-oasis.html',
        '/workspace/samara-parking.html',
        '/workspace/samara-real-estate.html',
        '/workspace/saryryah-healthcare.html',
        '/workspace/mahara-recruitment.html',
        '/workspace/index.html',
    ]
    
    print("Fixing Arabic pages...\n")
    for page in arabic_pages:
        if os.path.exists(page):
            process_file(page)
    
    print("\nDone!")

if __name__ == '__main__':
    main()
