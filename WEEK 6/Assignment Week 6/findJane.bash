
#!/bin/bash
>oldFiles.txt
files=$(grep " jane " ../data/list.txt | cut -d' ' -f3)
for f in $files; do
    echo ".."$f>>oldFiles.txt
done
