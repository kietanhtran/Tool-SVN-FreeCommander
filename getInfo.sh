for j in "$@"
do
	svn info $j | grep "^Name:"
	svn info $j | grep "^URL:" >> url.txt
	svn info $j | grep "^Last Changed Rev:" >> rev.txt
	res=$(awk '{print $2}' url.txt)"/?r="$(awk '{print $4}' rev.txt)
	echo -e "$res \n"
	rm -f url.txt rev.txt
done
read -n 1 -s -r -p "Press any key to continue..."
