#include<algorithm>
#include<iostream>
#include<climits>
#include<vector>
#include<map>

using namespace std;
typedef long long ll;
typedef long double ld;
//struct line_s{
//    ll m,c;
//    ld xl,xr;
//    inline ll get(ll x){
//        return m*x+c;
//    }
//};
ll N,K;
//deque<ll> lines;

//inline ll msc(ll *mcs,ll i,ll j){
//    return (mcs[j]-mcs[i]-((al[i]-al[0])*(wsm[j]-wsm[i])));
//}

int main(){
    cin >> N >> K;
    ll al[N],wt[N],wsm[N],mcs[N];;
    ll mc[N][2];//ll mc[N][K+1];
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
    
    j = 0;
    i = N-1;
    while(i>-1){
        mc[i][j] = /*msc(mcs,i,N-1);*/(mcs[N-1]-mcs[i]-((al[i]-al[0])*(wsm[N-1]-wsm[i])));
        i--;
    }

    for(ll p=0;p<N;p++)
        mc[p][1]=mc[p][0];

    j = 2;
    while(j<=K){
       i = N-j;
       while(i>=0){
           mc[i][1] = LLONG_MAX;
           k = i+1;
           while(k<=N-j+1){
               ck = mc[k][0]+mcs[k-1]-mcs[i]+(al[i]-al[0])*wsm[i];
               mk = wsm[k-1];
               x = -(al[i]-al[0]);
               mc[i][1] = min(mc[i][1],mk*x+ck);
               k+=1;
           }
           i-=1;
       }
       for(ll p=0;p<N;p++)
           mc[p][0]=mc[p][1];
       j+=1;
    }

    cout << mc[0][1];

    return 0;
}
