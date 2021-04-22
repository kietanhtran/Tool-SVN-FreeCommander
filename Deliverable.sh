#Choose the date
chooseDate='{2021-03-20}:{2021-04-20}'

#Change your SVN name
yourName="bv_kiettran"

echo "Please wait..."
svn log -v 'http://172.29.143.27/SS2/RCar_Autosar_New' -r $chooseDate | sed -n "/$yourName/,/-----$/ p" | grep "M /\|A /" > temp.txt
sed 's|   M |http://172.29.143.27/SS2/RCar_Autosar_New|g;s|   A |http://172.29.143.27/SS2/RCar_Autosar_New|g' temp.txt > temp1.txt
sort -u temp1.txt > res.txt

echo "Done! Check result in file res.txt"
rm -f temp.txt temp1.txt