#include<iostream>
#include<string>
#include<sstream>
#include<vector>

using namespace std;
typedef long long ll;
ll md = 1000000007ll;

int main(){
    ll n,x;
    cin >> n; 
    string suf;
    cin >> suf;
    //cin >> x;

    ll a[n+1];

    ll i = n;
    while(i>0){
        a[i] = (suf[i-1]-'0'); 
        i--;
    }

    //for (ll i = 1;i<n+1;i++)
    //    cout << a[i] ;
    
    //ll mp[n+1][8];
    vector<vector<ll>> mp;
    for(ll i=0;i<=n;i++){
        mp.push_back(vector<ll>());
        for(ll j = 0;j<8;j++)
            mp[i].push_back(-1);
    }
    
    i = 0;
    while(i<8){
        if((10*i+a[n])%8==0)
            mp[n][i]=1;
        else
            mp[n][i]=0;
        //cout << n << " " << i << " " << mp[n][i] << endl;
        i++; 
    }

    ll rm,t1,t2,j;

    for(i=n-1;i>0;i--){
        for(j=0;j<8;j++){
            rm = (10*j+a[i])%8;
            if(rm==0){
                t1 = mp[i+1][rm] + 1;
                //t1%=md; 
            }
            //if(rm==0 && mp[i+1][rm]==0)
            //    t1 = 1;
            else
                t1 = mp[i+1][rm];
            t2 = mp[i+1][j];
            //t2%=md;
            mp[i][j] = t1 + t2;
            mp[i][j]%=md;
            //cout << i << " " << j << " " << mp[i][j] << endl;
        }
    }

    cout << mp[1][0];
    return 0;
}
