for datafile in *.txt
do
    echo >> output.txt
     bash goostats $datafile | head -1 >> output.txt
done

