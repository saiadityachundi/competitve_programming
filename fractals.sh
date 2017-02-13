#!/usr/bin/bash
read n                                                          # n denotes iteration number
rws=$(printf "%.f" `echo "(64)*(1-(1/(2^$n)))" | bc -l`)        # rws is the number of non-empty rows
erws=$(printf "%.f" `expr 63 - $rws`)                           # erws is the number of empty rows

for((i=1; i<=$erws; i++)); do
    for j in {1..100};do
        printf "_"
    done
    printf "\n"
done
lc=$(expr $erws + 1)                                            # current line
lcr=$(expr 64 - $lc)                                            # current line in reverse rank
eit=$(printf "%.3f" $(echo "-l(1-($lcr/64))/l(2)" | bc -l))     # effective iteration
eitn=$(printf "%.f" $eit)                                       # greatest integer <= eit
if [ 1 -eq $(echo "$eitn!=$eit" | bc -l) ]; then
    eit=$(expr $eitn + 1)
else
    eit=$eitn
fi
nlp=$(printf "%.f" `echo "(64)*(1-(1/(2^$eitn)))" | bc -l`)      # number of lines upto current/previous iteration
lcro=$(expr $lcr - $nlp)                                        # offset of current line from reverse order
hlci=$(printf "%.f" `echo "16/(2^($eit-1))" | bc -l`)           # number of half lines in current iteration
hlo=$(expr $lcro - $hlci)                                       # offset beyond half lines of current itrn.
echo rws: $rws
echo erws: $erws
echo lc: $lc
echo lcr: $lcr
echo eit: $eit
echo eitn: $eitn
echo nlp: $nlp
echo lcro: $lcro
echo hlci: $hlci
echo hlo: $hlo
