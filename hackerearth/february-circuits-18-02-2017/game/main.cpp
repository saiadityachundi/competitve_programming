#include <iostream>
#include <map>
#include <vector>
#include <utility>

using namespace std;

int n;
map<int,map<int,int>> ob;

int mx=1;

void mxx(){
    mx=1;
    int i,j,ln;
    pair<int,int> nd;
    map<pair<int,int>,int> vst;
    vector<pair<int,int>> q;
    q.push_back(make_pair(0,2));
    vst[make_pair(0,2)]=1;
    while(q.size()!=0){
        ln=q.size();
        nd=q[ln-1];
        q.erase(q.back());
        vst[nd]=1;
        i=nd.first;
        j=nd.second;
        if(i>mx)
            mx=i;
        if(i!=n){
            if((ob[i+1].find(j))==ob[i+1].end())
                q.push_back(make_pair(i+1,j));
            if((j!=1)&&(ob[i+1].find(j-1)==ob[i+1].end()))
                q.push_back(make_pair(i+1,j-1));
            if((j!=3)&&(ob[i+1].find(j+1)==ob[i+1].end()))
                q.push_back(make_pair(i+1,j+1));
        }
    }
}

int main(){
    int t,q;
    cin >> t;
    for(int i=0;i<t;i++){
        cin >> n;
        cin >> q;
        int x,y;
        ob.clear();
        for(int i=1;i<=n;i++)
            ob[1]=map<int,int>();
        for(int j=0;j<q;j++){
            cin >> x >> y;
            ob[x][y]=1;
        }
        mxx();
        cout << mx;
    }
    return 0;
}
