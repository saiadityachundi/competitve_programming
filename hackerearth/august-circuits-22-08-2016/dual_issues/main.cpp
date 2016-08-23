#include<bits/stdc++.h>

using namespace std;

bool IsPrime(int n){
    int c=0;
    for(int i=1;i*i<=n;i++){
        if(n%i==0){
            if(i*i==n)
               c++;
            else
               c+=2; 
        } 
    }
    if(c==2)
        return true;
    else
        return false;
}

int maxd(){
    int n;
    cin >> n;
    int a[n];
    for(int i=0;i<n;i++)
        cin >> a[i];
    vector <int> p;
    for(int i=0;i<n;i++){
        if(IsPrime(a[i]))
            p.push_back(a[i]);
    }
    int m;
    if(p.empty())
        cout << -1;
    else{
        m=*max_element(p.begin(),p.end());
        cout << m*m;}
    return 0;
}

int main(){
    /*
    cout << "Prime Numbers below 100: ";
    for(int i=1;i<101;i++){
        if(IsPrime(i))
            cout << " " << i;
    }
    cout << endl;
    */
    int t;
    cin >> t;
    for(int i=0;i<t;i++)
        maxd();
    return 0;
}
