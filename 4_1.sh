#! /bin/bash

# Пояснения:
# fods (File Or Directory Size)
# fad (File And Directory)
# fod (File Or Directory)

fods() 
{
	local dir="$1"
	local s=$(du -h -s "$dir" 2>/dev/null | cut -f1)
	echo $s
}

fad=$(ls -A)

for fod in $fad
do
	size=$(fods "$fod")
	echo -e "$size\t$fod"
done | sort -hr  -k1,1
