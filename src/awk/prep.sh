Tmp=/tmp/$USER/$$
Doc=./doc
mkdir -p $Tmp
sed 's?^#?//?' $1.awk > $Tmp/$1.c 
pycco -d $Doc $Tmp/$1.c
open $Doc/$1.html
