#include <iostream>
#include<vector>
#include <map>
#include <climits>

using namespace std;
int g,n,m;
int x;
vector<int> a,b;
map< vector<int>::iterator, map< vector<int>::iterator, int> > dp;

int mxn(vector<int>::iterator at,vector<int>::iterator bt){
    if(dp.find(at)!=dp.end())
        if(dp[at].find(bt)!=dp[at].end())
            return dp[at][bt];
    else
        dp[at]=map<vector<int>::iterator, int>();

    int m1=INT_MIN;
    int m2=INT_MIN;

    int rsm=0;

    vector<int>::iterator it;

    for(it=a.begin();it!=at;it++)
        rsm+=*(it);

    for(it=b.begin();it!=bt;it++)
        rsm+=*(it);

    rsm=x-rsm;

    if(rsm<0){
        dp[at][bt]=0;
        return 0;
    }
    else{
        if(at==a.end() && bt==b.end()){
            dp[at][bt]=0;
            return 0;
        }
        else{
            if(at!=a.end()){
                if(*(at)<=rsm)
                    m1=1+(mxn(at+1, bt));
                else
                    m1=0;
            }
            if(bt!=b.end()){
                if(*(bt)<=rsm)
                    m2=1+(mxn(at, bt+1));
                else
                    m2=0;
            }
            if(m1>m2)
                dp[at][bt]=m1;
            else
                dp[at][bt]=m2;
        }
        return dp[at][bt];
    }
}

int main(){
    int tm,m1,m2;
    cin >> g;
    for(int i=0;i<g;i++){
        cin >> n >> m >> x;
        a.clear();
        b.clear();
        dp.clear();
        for(int j=0;j<n;j++){
            cin >> tm;
            a.push_back(tm);
        }
        for(int j=0;j<m;j++){
            cin >> tm;
            b.push_back(tm);
        }
        if(*(a.begin())<=x)
            m1=1+mxn(a.begin()+1, b.begin());
        else
            m1=0;
        if(*(b.begin())<=x)
            m2=1+mxn(a.begin(), b.begin()+1);
        else
            m2=0;
        if(m1>m2)
            cout << m1 << endl;
        else
            cout << m2 << endl;
    }
    return 0;
}
