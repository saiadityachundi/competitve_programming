#include<bits/stdc++.h>

/*
 * P(A/B)=P(B/A)*P(A)/P(B)
 * A -- asst was unbiased
 * B -- 1st kill missed and second kill strikes
 * n -- Total number of assts
 * m -- Fair(unbiased) assts
 * = (m/n)*(1/4)/((m/n)*(1/4)+(-m+n/n)*(2/9))
 * = (m/4n)/(9m/36n + -8m+8n/36n)
 * = (m/4n)/(m+8n / 36n)
 * = (9mn)/(m+8n)
 */

using namespace std;

int gcd(int a,int b){
    if(a==0)
        return b;
    else if(b==0)
        return a;
    if(a>b)
        return gcd(a%b,b);
    else if(b>a)
        return gcd(b%a,a);
    else if(a==b)
        return a;
}

void reduce(int a,int b){
    int g = gcd(a,b);
    cout << a/g << "/" << b/g << endl;
}

void prob(int m, int n){
    reduce((9*m),(m+8*n));
}

int main(){
    int t,m,n;
    cin >> t;
    for(int i=0;i<t;i++){
        cin >> n;
        cin >> m;
        reduce((9*m),(m+8*n));
    }
    return 0;
}
