#include<algorithm>
#include<iostream>
#include<deque>
#include<climits>
#include<cfloat>
#include<vector>
#include<map>

using namespace std;
typedef long long ll;
typedef long double ld;
ll N,K;

struct line{
    ld m,c;
    ld xl = LDBL_MIN;
    ld xr = LDBL_MAX;
};

deque<line> lines;

//inline ll msc(ll *mcs,ll i,ll j){
//    return (mcs[j]-mcs[i]-((al[i]-al[0])*(wsm[j]-wsm[i])));
//}

ld insxn(line l1,line l2){
    return (l1.c - l2.c)/(l2.m - l1.m);
}

void addl(line l){
    line l1;
    ld x;
    if(lines.size()==0)
        lines.push_back(l);
    else if(lines.size()==1){
        l1 = lines.front();
        lines.pop_back();
        x = insxn(l,l1);
        l1.xr = x;
        l.xl = x;
        lines.push_back(l1);
        lines.push_back(l);
    }
    else{
        l1 = lines.back();
        lines.pop_back();
        x = insxn(l,l1);
        if(x<=l1.xl){
            addl(l);
        }
        else{
            l1.xr = x;
            l.xl = x;
            lines.push_back(l1);
            lines.push_back(l);
        }
    }
}

ll hval(ll x,ll st,ll en){
    ll md;
    if(en==st)
        return ((lines[st].m)*x)+(lines[st].c);
    if(en==st+1){
        if(x<=lines[st].xr)
            return ((lines[st].m)*x)+(lines[st].c);
        else
            return ((lines[en].m)*x)+(lines[en].c);
    }
    md = (st+en)/2;
    if(lines[md].xl<=x && x<=lines[md].xr)
        return ((lines[md].m)*x)+(lines[md].c);
    else if(x<lines[md].xl)
        return hval(x,st,md);
    else
        return hval(x,md,en);
}

int main(){
    cin >> N >> K;
    ll al[N],wt[N],wsm[N],mcs[N];;
    ll mc[N][2];
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
        mc[p][1] = mc[p][0];


    j = 2;
    while(j<=K){
       i = N-j;
       lines.clear();
       while(i>=0){
           //mc[i][j] = LLONG_MAX;
           k = i+1;
           //while(k<=N-j+1){
           //ck = mc[k][j-1]+mcs[k-1];
           ck = mc[k][0]+mcs[k-1];
           mk = wsm[k-1];
           x = -(al[i]-al[0]);
           line newl;
           newl.m = mk;
           newl.c = ck;
           newl.xl = LDBL_MIN;
           newl.xr = LDBL_MAX;
           addl(newl);
           ld en = lines.size();
           mc[i][1] = hval(x,0,lines.size()-1);
           //mc[i][j] = min(mc[i][j],mk*x+ck);
           //    k+=1;
           //}
           mc[i][1]+=(al[i]-al[0])*wsm[i]-mcs[i];
           i-=1;
       }
       for(ll p=0;p<N;p++)
           mc[p][0] = mc[p][1];
       j+=1;
    }

    cout << mc[0][0]<< endl;

    return 0;
}
