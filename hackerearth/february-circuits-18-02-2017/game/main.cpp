#include <iostream>
#include <map>
#include <vector>
#include <utility>

using namespace std;

int n;
map<int,map<int,int>> ob;

int mx=1;

//void mxx(){
//    mx=1;
//    int i,j,ln;
//    pair<int,int> nd;
//    map<pair<int,int>,int> vst;
//    vector<pair<int,int>> q;
//    q.push_back(make_pair(0,2));
//    vst[make_pair(0,2)]=1;
//    while(q.size()!=0){
//        ln=q.size();
//        nd=q[ln-1];
//        q.erase(q.back());
//        vst[nd]=1;
//        i=nd.first;
//        j=nd.second;
//        if(i>mx)
//            mx=i;
//        if(i!=n){
//            if((ob[i+1].find(j))==ob[i+1].end())
//                q.push_back(make_pair(i+1,j));
//            if((j!=1)&&(ob[i+1].find(j-1)==ob[i+1].end()))
//                q.push_back(make_pair(i+1,j-1));
//            if((j!=3)&&(ob[i+1].find(j+1)==ob[i+1].end()))
//                q.push_back(make_pair(i+1,j+1));
//        }
//    }
//}

int main(){
    int t,n,o,x,y,mx;
    map<int, map<int,int>> ob;
    map<int, int> nob;
    cin >> t;
    for(int i=0;i<t;i++){
        cin >> n >> o;
        ob.clear();
        nob.clear();
        for(int j=1;j<=n;j++)
            nob[j]=0;
        for(int j=1;j<=o;j++)
            ob[j]=map<int, int>();
        mx=n;
        for(int j=0;j<o;j++){
            cin >> x >> y;
            if(ob[x].find(y)==ob[x].end()){
                ob[x][y]=1;
                nob[x]+=1;
            }
            if(nob[x]==3){
                if(x-1<mx)
                    mx=x-1;
            }
            else if(nob[x]==2){
                if(x!=n){
                    if(ob[x].find(1)!=ob[x].end() && ob[x].find(2)!=ob[x].end()){
                        if(ob[x+1].find(1)==ob[x+1].end()){
                            ob[x+1][1]=1;
                            nob[x+1]+=1;
                        }
                    }
                    if(ob[x].find(2)!=ob[x].end() && ob[x].find(3)!=ob[x].end()){
                        if(ob[x+1].find(3)==ob[x+1].end()){
                            ob[x+1][3]=1;
                            nob[x+1]+=1;
                        }
                    }
                }
            }
        }
        cout << mx << endl;
    }
    return 0;
}
