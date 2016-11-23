#include<iostream>
//#include<iomanip>
#include<algorithm>
#include<map>

using namespace std;

float maxm(float a, float b, float c, float d){
    return max(max(a,b), max(c,d));
}

map<float, map<float, float>> mp;
    
float t,x,y,n,w,p1,p2,mx,mn;
float sc,p, pm;

float pmax(float s, float i){
    if(mp.find(s)!=mp.end()){
        if(mp[s].find(i)!=mp[s].end())
            return mp[s][i];
    }
    else
        mp[s]=map<float, float>();

    if(s==0){
        mp[s][i]=1;
        return mp[s][i];
    }

    if(i==n)
        mp[s][i]=0;
    else
        mp[s][i]=maxm(p1*pmax(s-x, i+1), p2*pmax(s-y, i+1), (1-p1)*pmax(s, i+1), (1-p2)*pmax(s, i+1));
    return mp[s][i];
}

int main(){

    cin >> t;

    for(float i=0;i<t;i++){
        cin >> x >> y >> n >> w >> p1 >> p2;
        p1=p1/100;
        p2=p2/100;
        mx=max(x,y);
        mn=min(x,y);
        pm=max(p1, p2);
        mp.clear();
        mp[0]=map<float, float>();
        mp[0][n]=1;
        for(sc=1;sc<=mn;sc++){
            mp[sc]=map<float, float>();
            mp[sc][n]=pm;
        }
        if(x==mx)
            p=p1;
        else
            p=p2;
        for(;sc<=mx;sc++){
            mp[sc]=map<float,float>();
            mp[sc][n]=p;
        }
        cout.precision(6);
       cout << fixed << pmax(w,1)*100 << endl;

       //cout << x;
       //cout << y << n <<  w << p1 << p2;
    }

    return 0;
}
