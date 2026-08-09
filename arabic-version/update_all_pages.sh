#!/bin/bash

# Update all company pages with Circular Std Book font and proper structure

files=("samara-H-VACR.html" "samara-parking.html" "builmix.html" "mahara-recruitment.html" "salmiya-oasis.html" "samara-real-estate.html" "saryryah-healthcare.html")

for file in "${files[@]}"; do
    if [ -f "$file" ]; then
        # Add Circular Std Book font after existing font links
        sed -i '/<\/head>/i\
    <!-- Circular Std Book Font -->\
    <style>\
        @font-face {\
            font-family: "Circular Std Book";\
            src: url("https://db.onlinewebfonts.com/t/860c3ec7bbc5da3e97233ccecafe512e.eot");\
            src: url("https://db.onlinewebfonts.com/t/860c3ec7bbc5da3e97233ccecafe512e.eot?#iefix") format("embedded-opentype"),\
            url("https://db.onlinewebfonts.com/t/860c3ec7bbc5da3e97233ccecafe512e.woff2") format("woff2"),\
            url("https://db.onlinewebfonts.com/t/860c3ec7bbc5da3e97233ccecafe512e.woff") format("woff"),\
            url("https://db.onlinewebfonts.com/t/860c3ec7bbc5da3e97233ccecafe512e.ttf") format("truetype"),\
            url("https://db.onlinewebfonts.com/t/860c3ec7bbc5da3e97233ccecafe512e.svg#Circular Std Book") format("svg");\
            font-display: swap;\
        }\
        :root {\
            --font-main: "Circular Std Book", "Inter", sans-serif;\
        }\
        body {\
            font-family: var(--font-main);\
        }\
    </style>' "$file"
        echo "Updated $file with Circular Std Book font"
    fi
done

echo "All files updated!"
