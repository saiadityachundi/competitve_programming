#include<iostream>

using namespace std;
typedef long long ll;
typedef long double ld;

int main(){
    ll t;
    cin >> t;

    ld n,b;
    ll n1,m1,n2,m2;

    for(ll i=0;i<t;i++){
        cin >> n >> b;
        n1 = n/(2*b);
        n2 = n1+1;
        m1 = n1*(n-n1*b);
        m2 = n2*(n-n2*b);
        if(m1>m2)
            cout << m1 << endl;
        else
            cout << m2 << endl;
    }

    return 0;
}
