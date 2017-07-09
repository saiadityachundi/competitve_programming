#include<iostream>

using namespace std;

typedef long long ll;

int main(){
    ll t;
    cin >> t;
    string s;
    ll mx,mn,cu,ln;

    for(ll i=0;i<t;i++){
        cin >> s;
        ln = s.length();
        mx = mn = cu = ln+1;
        for(ll j=0;j<ln;j++){
            if(s[j]=='<')
                cu++;
            if(s[j]=='>')
                cu--;
            if(cu>mx)
                mx = cu;
            if(cu<mn)
                mn = cu;
        }
        cout << mx-mn+1 << endl;
    }

    return 0;
}
