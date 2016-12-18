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
 
int ind(int *a, int st, int ed, int sr){
    if(st==ed)
        if(a[st]==sr)
            return st+1;
        else if(a[st]>sr)
            return st+2;
        else if(a[st]<sr)
            return st+1;
    if(ed==st+1)
        if(sr>a[st])
            return st+1;
        else if(sr<a[ed])
            return ed+2;
    int md=(st+ed)/2;
    if(a[md]==-1)
        return ind(a, st, md-1, sr);
    else if(a[md]==sr)
        return md+1;
    else if(a[md]>sr)
        return ind(a, md+1, ed, sr);
    else if(a[md]<sr)
        return ind(a, st, md-1, sr);
}

int main(){
    int n;
    cin >> n;
    vector<int> scores(n);
    for(int scores_i = 0;scores_i < n;scores_i++){
       cin >> scores[scores_i];
    }
    
    int m;
    cin >> m;
    
    int ar[n];
    
    for(int i=0;i<n;i++)
        ar[i]=-1;
    
    int l=scores.size();
    
    ar[0]=scores[0];
    
    int j=1;
    
    for(int i=1;i<l;i++){
        if(scores[i]!=scores[i-1]){
            ar[j]=scores[i];
            j++;
        }
    }

    vector<int> alice(m);
    for(int alice_i = 0;alice_i < m;alice_i++){
       cin >> alice[alice_i];
       cout << ind(ar, 0, n-1, alice[alice_i]) << endl;
    }
    
    return 0;
}

