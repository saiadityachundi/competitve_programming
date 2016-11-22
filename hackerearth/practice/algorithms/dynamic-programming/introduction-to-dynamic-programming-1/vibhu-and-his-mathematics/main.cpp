#include<iostream>
#include<map>

using namespace std;

long int mod=1000000007;

map<long, long> mp{
    {1,1},{2,2}
};

long int func(long int n){
    if(mp.find(n)!=mp.end())
        return mp[n];
    else{
        mp[n]=(func(n-1)%mod+(((n-1)%mod)*(func(n-2)%mod)))%mod;
        return mp[n];
    }
}

using namespace std;

int main(){

    long int t,n;
    cin >> t;

    for(long int i=0;i<t;i++){
        cin >> n;
        cout << func(n) << endl;
    }
    
    return 0;
}
