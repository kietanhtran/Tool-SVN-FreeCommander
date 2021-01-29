read -p 'File name: ' file
find . -type f -name $file
read -n 1 -s -r -p "Press any key to continue..."