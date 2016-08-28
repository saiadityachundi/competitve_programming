#include<bits/stdc++.h>

using namespace std;

long steps(long a, long b){                 // a is the number which needs to be made equal to b
    long c=0;
    if(b>=a)
        return b-a;
        
    while(a>b){
        a/=2;
        c++;       
    }
    c+=b-a;

    return c;
}

long mtime(vector<long> a){
    long mx = 0;
    long c = 0;
    long mi = -1;
    vector<long>::iterator iter1, iter2, iter3;

    for(iter1 = a.begin();iter1!=a.end();iter1++)
        if(*iter1>mx)
            mx = *iter1;

    for(long i=0;i<=mx;i++){
        c = 0;
        for(iter2 = a.begin();iter2!=a.end();iter2++){
            c+=steps(*iter2, i);
        }
        if(mi==-1 || c < mi)
            mi = c;
    }

    return mi;
}

int main(){

    long t,n,x;
    vector<long> a;

    cin >> t;

    for(long i=0;i<t;i++){
        cin >> n;
        for(long j=0;j<n;j++){
            cin >> x;    
            a.push_back(x);
        }
    }

    cout << mtime(a) << endl;

    return 0;
}
