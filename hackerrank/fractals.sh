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
while [ $lc -le 63 ];do
    lcr=$(expr 64 - $lc)                                            # current line in reverse rank
    eit=$(printf "%.3f" $(echo "-l(1-($lcr/64))/l(2)" | bc -l))     # effective iteration
    eitn=$(printf "%.f" $eit)                                       # greatest integer <= eit
    if [ 1 -eq $(echo "$eitn!=$eit" | bc -l) ]; then
        eit=$(expr $eitn + 1)
    else
        eit=$eitn
    fi
    nlp=$(printf "%.f" `echo "(64)*(1-(1/(2^$eitn)))" | bc -l`)     # number of lines upto current/previous iteration
    lcro=$(expr $lcr - $nlp)                                        # offset of current line from reverse order
    hlci=$(printf "%.f" `echo "16/(2^($eit-1))" | bc -l`)           # number of half lines in current iteration
    hlo=$(expr $lcro - $hlci)                                       # offset beyond half lines of current itrn.
    peit=$(expr $eit - 1)                                           # Previous iteration number
    declare -a fa                                                   # first Array
    declare -a sa                                                   # second Array
    fa=( 50 )
    for(( i=1;i<=$peit;i++ ));do
        sa=()
        for j in "${fa[@]}";do
            sa=( "${sa[@]}" "$(expr $j - $(printf "%.f" $(echo "16/(2^($i-1))" | bc -l)))" "$(expr $j + $(printf "%.f" $(echo "16/(2^($i-1))" | bc -l)))")
        done
        fa=(${sa[@]})
    done
    if [ $hlo -ge 0 ]; then
        sa=()
        for j in "${fa[@]}";do
            sa=( "${sa[@]}" "$(expr $j - $hlo)" "$(expr $j + $hlo)")
        done
        fa=(${sa[@]})
    elif [ $lcro -eq 0 ];then
        sa=()
        for j in "${fa[@]}";do
            sa=( "${sa[@]}" "$(expr $j - $(printf "%.f" $(echo "16/(2^($eit-1))" | bc -l)))" "$(expr $j + $(printf "%.f" $(echo "16/(2^($eit-1))" | bc -l)))")
        done
        fa=(${sa[@]})
    fi
    #echo rws: $rws
    #echo erws: $erws
    #echo lc: $lc
    #echo lcr: $lcr
    #echo eit: $eit
    #echo eitn: $eitn
    #echo nlp: $nlp
    #echo lcro: $lcro
    #echo hlci: $hlci
    #echo hlo: $hlo
    id=0
    for i in {1..100};do
        if [ 1 -eq $(echo "$id <= ${#fa[@]}-1" | bc -l) ];then
            if [ $i -eq ${fa[$id]} ];then
                printf "1"
                ((id++))
            else
                printf "_"
            fi
        else printf "_"
        fi
    done
    printf "\n"
    ((lc++))
done
