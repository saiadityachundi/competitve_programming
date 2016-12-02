#include<iostream>
#include<algorithm>

using namespace std;

int n,m,hmx,hmn,*a;
int **op;

int opf(int i,int ms){
    if(op[i][ms]!=-1)
        return op[i][ms];
    else if(i==n-1){
        if(ms>=hmn && ms<=hmx){
            op[i][ms]=1;
            return op[i][ms];
        }
        else{
            op[i][ms]=0;
            return op[i][ms];
        }
    }
    else if(ms<hmn){
        op[i][ms]=0;
        return op[i][ms];
    }
    else if(a[i+1]-a[i]>=hmn && a[i+1]-a[i]<=hmx){
        op[i][ms]=opf(i+1, ms-(a[i+1]-a[i]));
        return op[i][ms];
    }
    else{
        op[i][ms]=0;
        return op[i][ms];
    }
}

int func(int i,int ms){
    if(i==n):
        return a[i-1];
    int z,j;
    if(i==0)
        z=hmx;
    else
        z=min(hmx,a[i]-a[i-1]);
    j=hmn;
    while(j<=z){
        if(opf(i,ms-j))
            return a[i]-j;
        j+=1;
    }
    return func(i+1,ms);
}

int main(){

    cin >> n;

    a=(int *)malloc(n*sizeof(int));

    for(int i=0;i<n;i++)
        cin >> a[i];
    
    cin >> m >> hmn >> hmx;

    op=new int*[n];
    for(int i=0;i<n;i++){
        op[i]=new int[m+1];
        for(int j=0;j<m+1;j++)
            op[i][j]=-1;
    }

    cout << func(0,m);

    return 0;
}
