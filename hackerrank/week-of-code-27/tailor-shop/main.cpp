#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;


int main(){
    int n;
    int p;
    cin >> n >> p;
    vector<int> a(n);
    for(int a_i = 0;a_i < n;a_i++){
       cin >> a[a_i];
       a[a_i]=ceil((float)a[a_i]/p);
    }
    
    map<int, int> cnt;
    vector<int> b;
    
    for(int i=0;i<n;i++){
        if(cnt.find(a[i])!=cnt.end()){
            cnt[a[i]]+=1;
        }
        else{
            cnt[a[i]]=1;
            b.push_back(a[i]);
        }
    }
    
    sort(b.begin(),b.end());
    vector<int>::iterator it;
    
    int lt=0,mbs=0;
    int x;
    
    for(it=b.begin();it!=b.end();it++){
        if(*it>lt){
            mbs+=((((cnt[*it])*(2*(*it)+(cnt[*it]-1)))/2));
            lt=(*it)+(cnt[*it]-1);
        }
        else{
            x=lt+1;
            mbs+=((((cnt[*it])*(2*(x)+(cnt[*it]-1)))/2));
            lt=x+(cnt[*it]-1);
        }
    }
    
    cout << mbs;

    return 0;
}
