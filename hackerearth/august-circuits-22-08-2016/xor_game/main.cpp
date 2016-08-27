#include<bits/stdc++.h>

using namespace std;

void func(map<long, long> m){
    long max = 0;
    long key;
    map<long, long>::iterator iter;
    for(iter = m.begin();iter != m.end(); iter++)
        if(iter->second > max){
            max = iter->second;
            key = iter->first;
        }
    iter = m.find(key);
    m.erase(iter);

    long xor1 = max;
    long varx = max;
    
    max = 0;
    for(iter = m.begin();iter != m.end(); iter++)
        if(iter->second > max){
            max = iter->second;
            key = iter->first;
        }
    iter = m.find(key);
    m.erase(iter);

    long xor2 = max;
    bool one,two;
    long var1, var2, var3;
    one = true;
    two = false;

    max=0;

    while(!m.empty()){
        
        if(one == true){
            for(iter = m.begin();iter != m.end(); iter++){
                var1 = iter->second;
                if(xor1^var1 > max){
                    max = xor1^var1;
                    key = iter->first;
                }
            }
            iter = m.find(key);
            m.erase(iter);
            xor1 = max;
            max = 0;
            one = false;
            two = true;
        }
        
        else if(two == true){
            for(iter = m.begin();iter != m.end(); iter++){
                var1 = iter->second;
                if(xor2^var1 > max){
                    max = xor2^var1;
                    key = iter->first;
                }
            }
            iter = m.find(key);
            m.erase(iter);
            xor2 = max;
            max = 0;
            one = true;
            two = false;
        
        }
    }

    if(xor1 > xor2)
        cout << "Alice" << endl << varx;
    else if(xor1 < xor2)
        cout << "Bob" ;
    else
        cout << "Draw" ;
}

int main(){

    long t,n,x;
    map<long, long> m;

    cin >> t;

    for(int i=0;i<t;i++){
        cin >> n;
        m.clear();
        for(int i=0;i<n;i++){
            cin >> x;
            m[i+1] = x;     
        }
        func(m);
        cout << endl;
    }

    return 0;
}
