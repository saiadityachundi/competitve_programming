#!/usr/bin/bash

declare -a fa           # constant for an iteration
declare -a sa           # current array variable
declare -a ma

read N
rws=$(printf "%.f" $(echo "(64)*(1-(1/(2^$N)))" | bc -l))
erws=$(expr 63 - $rws)

for((il=0;il<$erws;il++));do
    for jl in {1..100};do
        printf "_"
    done
    printf "\n"
done

lcr=$rws


lid=1
fa=( 50 )

while [ $lid -le $lcr ];do
    
    eit=$(printf "%.3f" $(echo "-l(1-($lid/64))/l(2)" | bc -l))     # effective iteration
    eitn=${eit%.*}
    if [ 1 -eq $(echo "$eitn!=$eit" | bc -l) ]; then
        eit=$(expr $eitn + 1)
    else
        eit=$eitn
    fi
    nlp=$(printf "%.f" `echo "(64)*(1-(1/(2^$eitn)))" | bc -l`)     # number of lines upto current/previous iteration
    lcro=$(expr $lid - $nlp)                                        # offset of current line from reverse order
    hlci=$(printf "%.f" `echo "16/(2^($eit-1))" | bc -l`)           # number of half lines in current iteration
    hlo=$(expr $lcro - $hlci)                                       # offset beyond half lines of current itrn.
    peit=$(expr $eit - 1)                                           # Previous iteration number
    
    #echo rws: $rws
    #echo erws: $erws
    #echo lc: $lc
    #echo lcr: $lcr
    #echo lid: $lid
    #echo eit: $eit
    #echo eitn: $eitn
    #echo nlp: $nlp
    #echo lcro: $lcro
    #echo hlci: $hlci
    #echo hlo: $hlo
    #echo fa: ${fa[@]}
    #echo sa: ${sa[@]}
    #echo st: $st

    if [ $lid -eq 1 ];then
        st=
        for i in {1..100};do
            if [ $i -eq 50 ];then
                st=$st"1"
            else
                st=$st"_"
            fi
        done
        ma[$lid]=$st
        (( lid++ ))
    else
        if [ $hlo -le 0 ];then
            if [ $lcro -ne 0 ];then
                ma[$lid]=$st
                (( lid++ ))
            else
                sa=()
                for(( k=0;k<${#fa[@]};k++ ));do
                    sa=("${sa[@]}" "$(expr ${fa[$k]} - $hlci)" "$(expr ${fa[$k]} + $hlci)")
                done
                id=0
                st=
                for j in {1..100};do
                    if [ $id -lt ${#sa[@]} ];then
                        if [ $j -eq ${sa[$id]} ];then
                            st=$st"1"
                            (( id++ ))
                        else
                            st=$st"_"
                        fi
                    else
                        st=$st"_"
                    fi
                done
                ma[$lid]=$st
                (( lid++ ))
                fa=("${sa[@]}")
            fi
        else
            sa=()
            #echo going into the for loop
            for((kr=0;kr<${#fa[@]};kr++));do
                sa=( "${sa[@]}" "$(expr ${fa[$kr]} - $hlo)" "$(expr ${fa[$kr]} + $hlo)")
            done
            #echo came from the for loop
            id=0
            st=
            for j in {1..100};do
                if [ $id -lt ${#sa[@]} ];then
                    if [ $j -eq ${sa[$id]} ];then
                        st=$st"1"
                        (( id++ ))
                    else
                        st=$st"_"
                    fi
                else
                    st=$st"_"
                fi
            done
            ma[$lid]=$st
            (( lid++ ))
        fi
    fi

    #echo
    #echo fa: ${fa[@]}
    #echo sa: ${sa[@]}
    #echo st: $st
    #echo 
done

for(( i=$lcr; i>=1; i-- ));do
    echo ${ma[$i]}
done
