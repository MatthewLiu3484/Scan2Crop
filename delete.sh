cd crop/static/crop/images/
for file in $(ls | grep -E 'ROI|photos')
do
	sincemodification=$(($(date +%s) - $(date +%s -r $file)))
	if [ $sincemodification -gt 86400 ]
	then
		rm $file
	fi
done
