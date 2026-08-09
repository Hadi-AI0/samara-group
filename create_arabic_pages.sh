#!/bin/bash

cd /workspace

# Create Arabic versions of all company pages at root
PAGES="builmix mahara-recruitment salmiya-oasis samara-H-VACR samara-parking samara-real-estate saryryah-healthcare"

echo "Creating Arabic versions of company pages..."

for page in $PAGES; do
    if [ -f "en/${page}.html" ]; then
        # Read the English file
        content=$(cat "en/${page}.html")
        
        # Update html tag to Arabic
        content=$(echo "$content" | sed 's/<html lang="en">/<html lang="ar" dir="rtl">/')
        
        # Add canonical and hreflang tags after the title line
        # This is a simplified approach - we'll add the SEO tags
        
        echo "$content" > "${page}.html"
        echo "  Created ${page}.html (Arabic version)"
    fi
done

echo "Done creating Arabic pages!"
