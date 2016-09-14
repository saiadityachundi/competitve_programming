#include<bits/stdc++.h>

using namespace std;

bool ck(int **li, int p, int q, int r, int n){

    int i,j,d,e;

    if(p-r<1 || p+r>n || q-r<1 || q+r>n)
        return false;

    else if(li[p][q+r]==1 || li[p][q-r]==1 || li[p+r][q]==1 || li[p-r][q]==1)
        return false;
    else{
        i = p-r+1;
        while(i!=p){
            d = int(floor(sqrt(pow(r,2)-pow(i-p,2))));
            j = q+d;
            if(li[i][j]==1)
                return false;
            j=q-d;
            if(li[i][j]==1)
                return false;
            if(li[2*p-i][j]==1)
                return false;
            j=q+d;
            if(li[2*p-i][j]==1)
                return false;
            i++;
        }
    }
    return true;
}

int main(){

    int **a;
    int n;
    string s;
    vector<pair<int,int>> li;
    
    cin >> n;
    a=new int*[n+1];
    for(int i=0;i<n;i++){
        a[i+1]=new int[n+1];
        cin >> s;
        for(int j=0;j<n;j++){
            if(s[j]=='*')
                a[i+1][j+1]=1;
            else{
                a[i+1][j+1]=0;
                li.push_back(*(new pair<int,int>(i+1,j+1)));
            }
        }
    }

    vector<pair<int, int >>::iterator iter;

    int m=0;
    int x,y,r;

    for(iter=li.begin();iter!=li.end();iter++){
        x=iter->first;
        y=iter->second;

        r=1;
        while(ck(a,x,y,r,n))
            r++;

        r--;
        if(r>m)
            m=r;
    }

    cout << m;
    return 0;
}
