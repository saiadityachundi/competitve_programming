#include<algorithm>
#include<iostream>
#include<climits>
#include<vector>
#include<map>

using namespace std;
typedef long long ll;
typedef long double ld;
ll N,K;

//inline ll msc(ll *mcs,ll i,ll j){
//    return (mcs[j]-mcs[i]-((al[i]-al[0])*(wsm[j]-wsm[i])));
//}

int main(){
    cin >> N >> K;
    ll al[N],wt[N],wsm[N],mcs[N];;
    ll mc[N][K+1];
    ll i,j,k;
    for(i=0;i<N;i++){
        cin >> al[i] >> wt[i];
    }

    wsm[0] = wt[0];
    i = 0;
    while(i++<N)
        wsm[i] = wsm[i-1]+wt[i];

    mcs[0] = 0;
    i = 0;
    while(i++<N)
        mcs[i] = mcs[i-1] + wt[i]*(al[i]-al[0]);

    ll ck,mk,x;
    
    j = 1;
    i = N-1;
    while(i>-1){
        mc[i][j] = /*msc(mcs,i,N-1);*/(mcs[N-1]-mcs[i]-((al[i]-al[0])*(wsm[N-1]-wsm[i])));
        i--;
    }

    j = 2;
    while(j<=K){
       i = N-j;
       while(i>=0){
           mc[i][j] = LLONG_MAX;
           k = i+1;
           while(k<=N-j+1){
               ck = mc[k][j-1]+mcs[k-1]-mcs[i]+(al[i]-al[0])*wsm[i];
               mk = wsm[k-1];
               x = -(al[i]-al[0]);
               mc[i][j] = min(mc[i][j],mk*x+ck);
               k+=1;
           }
           i-=1;
       }
       j+=1;
    }

    cout << mc[0][K];

    return 0;
}
