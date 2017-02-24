#include<iostream>
#include<cmath>
#include<map>

using namespace std;

map<long long, bool> chck;

bool chkp(long long l){
    long long i=2;
    while(i*i<=l){
        if(l%i==0)
            return false;
        i+=1;
    }
    return true;
}

bool chk(long long l){
    if(l==0)
        return true;
    long long r;
    if(chck.find(l)!=chck.end())
        return chck[l];
    if(l<10){
        if(l==2 || l==3 || l==5 || l==7){
            chck[l]=true;
            return true;
        }
        else{
            chck[l]=false;
            return false;
        }
    }
    else{
        r=l%10;
        if(r==2 || r==3 || r==5 || r==7){
            chck[l]=chk(l/10);
            return chck[l];
        }
        else{
            chck[l]=false;
            return false;//chck[l];
        }
    } 
}

long long nxt(long long n){
    if(n==0)
        return 2;
    long long l=n%10;
    if(l==2){
        l=3;
        n/=10;
        n=n*10+l;
        return n;
    }
    else if(l==3){
        l=5;
        n/=10;
        n=n*10+l;
        return n;
    }
    else if(l==5){
        l=7;
        n/=10;
        n=n*10+l;
        return n;

    }
    else if(l==7){
        l=2;
        n/=10;
        n=nxt(n);
        n=n*10+l;
        return n;
    }
}

long long nxtd(long long n){
    long long r=n%10;
    long long l=n/10;
    if(chk(l)){
        if(r<2){
            r=2;
            l=l*10+r;
            return l;
        }
        else if(r<3){
            r=3;
            l=l*10+r;
            return l;
        }
        else if(r<5){
            r=5;
            l=l*10+r;
            return l;
        }
        else if(r<7){
            r=7;
            l=l*10+r;
            return l;
        }
        else{
            r=2;
            l=nxt(l);
            l=l*10+r;
            return l;
        }
    }
    else{
        l=nxtd(l);
        l=l*10+2;
        return l;
    }
}

int main(){
    long long f,l,cnt;
    cnt=0;
    cin >> f >> l;
//    cin >> c;
//    if(chkp(c))
//        cout << "Yes";
//    else
//        cout << "No";

    long long i;
    if(chk(f))
        i=f;
    else
        i=nxtd(f);
    while(i<=l){
        if(chkp(i)){
//            cout << i << endl;
            cnt+=1;
        }
        i=nxt(i);
    }
    cout << cnt;

//    cout << chk(f) << " " << chk(l) << endl; 
    return 0;
}
