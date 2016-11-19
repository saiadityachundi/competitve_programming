#include<iostream>
#include<map>
#include<algorithm>

using namespace std;

long t,n;
map<long, map<long, long>> memd, mp;

long minm(long a, long b, long c){
    return min(min(a,b),c);
}

long mins(long id, long be){

    if(memd.find(be)!=memd.end()){
        if(memd[be].find(id)!=memd[be].end())
            return memd[be][id];
    }
    else{
        memd[be]=map<long, long>();
    }
    
    switch(id){
        case 1:
            if(be==n)
                memd[be][id]=min(mp[be][2], mp[be][3]);
            else
                memd[be][id]=min(mp[be][2]+mins(2, be+1), mp[be][3]+mins(3, be+1));
            break;

        case 2:
            if(be==n)
                memd[be][id]=min(mp[be][1], mp[be][3]);
            else
                memd[be][id]=min(mp[be][1]+mins(1, be+1), mp[be][3]+mins(3, be+1));
            break;

        case 3:
            if(be==n)
                memd[be][id]=min(mp[be][1], mp[be][2]);
            else
                memd[be][id]=min(mp[be][1]+mins(1, be+1), mp[be][2]+mins(2, be+1));
            break;

        return memd[be][id];

    }
}

long func(){
    if(n==1)
        return minm(mp[1][1], mp[1][2], mp[1][3]);
    return minm(mp[1][1]+mins(1, 2), mp[1][2]+mins(2, 2), mp[1][3]+mins(3, 2));
}

int main(){

    cin>>t;
    for(long i=0;i<t;i++){
        memd.clear();
        mp.clear();
        cin>>n;
        for(long j=0;j<n;j++){
            mp[j+1]=map<long, long>();
            for(long k=0;k<3;k++){
                mp[j+1][k+1]=0;
                cin>>mp[j+1][k+1];
            }
        }
        cout << func() << endl;
    }

    return 0;
}
