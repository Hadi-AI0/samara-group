#!/bin/bash

# Fix builmix.html - Root should be Arabic
sed -i 's/<html lang="en">/<html lang="ar" dir="rtl">/' /workspace/builmix.html
sed -i 's|href="https://samara.co.com/en/builmix.html"|href="https://samara.co.com/builmix"|g' /workspace/builmix.html
sed -i 's|<link rel="stylesheet" href="../css/ltr.css">||' /workspace/builmix.html
sed -i 's/Saudi Builmix | Samara Group/بيلد ميكس السعودية | مجموعة سمارى/' /workspace/builmix.html
sed -i 's/alt="Samara Group"/alt="مجموعة سمارى"/' /workspace/builmix.html

echo "Fixed builmix.html header"
