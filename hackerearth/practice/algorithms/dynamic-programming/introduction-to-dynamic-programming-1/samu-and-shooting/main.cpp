#include<iostream>
//#include<iomanip>
#include<algorithm>
#include<map>

using namespace std;

double maxm(double a, double b, double c, double d){
    return max(max(a,b), max(c,d));
}

map<double, map<double, double>> mp;
    
double t,x,y,n,w,p1,p2,mx,mn,pmx,pmn;
double sc,p, pm;

double pmax(double s, double i){
    if(mp.find(s)!=mp.end()){
        if(mp[s].find(i)!=mp[s].end())
            return mp[s][i];
    }
    else
        mp[s]=map<double, double>();

    if(s<=0){
        mp[s][i]=1;
        return mp[s][i];
    }

    else if(i>n){
        mp[s][i]=0;
        return mp[s][i];
    }

    else if(i==n){
        if(s<=mn)
            return max(p1, p2);
        else if(s<=mx)
            return p;
        else
            return 0;
    }

    mp[s][i]=(p1*pmax(s-x, i+1)+(1-p1)*pmax(s, i+1), p2*pmax(s-y, i+1)+(1-p2)*pmax(s, i+1));
    return mp[s][i];
}

int main(){

    cin >> t;

    for(double i=0;i<t;i++){
        cin >> x >> y >> n >> w >> p1 >> p2;
        p1=p1/100;
        p2=p2/100;
        mp.clear();
        mx=max(x,y);
        mn=min(x,y);
        if(x==mx)
            p=p1;
        else
            p=p2;

        cout.precision(6);
        cout << fixed << pmax(w,1)*100 << endl;

       //cout << x;
       //cout << y << n <<  w << p1 << p2;
    }

    return 0;
}
