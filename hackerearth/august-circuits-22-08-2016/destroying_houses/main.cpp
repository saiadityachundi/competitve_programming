#include<bits/stdc++.h>

using namespace std;

float prob(float R, float D, float x, float y){

    float max, min,a,t;                     // a is alpha, t is theta
    float p = M_PI;

    if(R>=D){
        max = R;
        min = D;
    }
    else{
        max = D;
        min = R;
    }

    float d = sqrt(x*x + y*y);
    float pro;
    if(d<=max-min)
        return (min*min)/(R*R);
    else if(d>=max+min)
        return 0;
    else
        if(d<=sqrt((max*max)-(min*min))){
            a = acos(((max*max)-(min*min)-(d*d))/(2*min*d));
            t = asin((min*sin(a))/R);
            pro = ((max*max*t)-(max*max*cos(t)*sin(t)/2)+(p*min*min)-(min*min*a)+(min*min*cos(a)*sin(a)/2))/(p*R*R);
            return pro;
        }
        else{
            a = acos((-(max*max)+(min*min)+(d*d))/(2*min*d));
            t = asin((min*sin(a))/R);
            pro = ((max*max*t)-(max*max*cos(t)*sin(t)/2)+(min*min*a)-(min*min*cos(a)*sin(a)/2))/(p*R*R);
            return pro;
        }
}

int main(){

    float n,D,R;
    cin >> n >> D >> R;
    float x,y,pr;

    pr = 0;

    for(int i=0;i<n;i++){
        cin >> x >> y;
        pr+=prob(R,D,x,y);
    }
    cout.precision(4);
    cout << fixed; 
    cout << pr;

    return 0;
}
