#define mod 10000009

#include <map>
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int next(map<long, vector<long> > & newmap, map<long, vector<long>::iterator > & mit, long kind, long ar[]){

    map<long, vector <long>>::reverse_iterator riter(newmap.find(kind));
    /*
    map<long, vector <long>>::reverse_iterator riter(newmap.find(kind));
    map<long, vector <long>>::iterator it1;
    long ind = riter->first;
    mit[ind]++;

    while(mit[ind]==newmap[ind].end() && riter!=newmap.rend()){
        ind=riter->first;
        mit[ind]=newmap[ind].begin();
        riter++;
        ind=riter->first;
        mit[ind]++;
    }

    if(riter==newmap.rend())
        return -1;

    map<long, vector<long>>::iterator iter=newmap.find(riter->first);
    map<long, vector<long>>::iterator iter0=newmap.begin();
    long i;
    long r;
    long j,jr;
    vector <long>::iterator it2;

    for(iter0 = newmap.begin();iter0!=newmap.end();iter0++){
        i = iter0->first;
        r = *mit[i];
        it1=iter;
        for(it1=it1;it1!=newmap.end();it1++){
            j=it1->first;
            if(j%i==0){
                it2 = newmap[j].begin();
                while(*it2%i != r && it2 != newmap[j].end())
                    it2++;
                if(it2==newmap[j].end()){
                    return next(newmap, mit, i);
                }
            }
        }
    }

    //======================================================
    for(iter=iter;iter!=newmap.end();iter++){
        i = iter->first;
        r = *mit[i];
        it1=iter;
        it1++;
        for(it1=it1;it1!=newmap.end();it1++){
            j=it1->first;
            if(j%i==0){
                it2 = newmap[j].begin();
                while(*it2%i != r && it2 != newmap[j].end())
                    it2++;
                if(it2==newmap[j].end()){
                    return next(newmap, mit, i);
                }
            }
        }
    }
    //=====================================================
    */
    return 0;
}

int main() {
    map <long, vector <long>> m;
    long n;
    cin >> n;
    long a[n];
    for(long i=0;i<n;i++){
        cin >> a[i];
        if(a[i]==-1){
            m[i+1]=vector<long>();
        }
    }

    vector<long>::iterator it;
    long z;
    bool made_empty[m.size()];

    long j,p;

    for(long i=1;i<=n;i++){
        if(a[i-1]!=-1){
            j=1;
            p=i*j;
            while(p<=n){
                if(m.count(p)>0){       // Assuming all other positions except the ones with -1 form nice sequence(s)
                    if(m[p].empty()){
                        z=a[i-1];
                        while(z<p){     // Make '<' '<='
                            m[p].push_back(z);
                            z+=i;
                        }
                    }
                    else{
                        it = m[p].begin();
                        while(it != m[p].end()){
                            long x = *it;
                            if(x%i == a[i-1])
                                it++;
                            else
                                m[p].erase(it);
                        }
                        if(m[p].empty()){
                            cout << 0;
                            return 0;
                        }
                    }
                }
                j+=1;
                p=i*j;
            }
        }
    }

    for(map<long, vector <long> >::iterator iter=m.begin();iter!=m.end();iter++){
        long n = iter->first;
        if(m[n].empty()){
            for(long i = 0;i<n;i++){
                m[n].push_back(i);
            }
        }
    }

    long c=0;
    p=1;

    map<long, vector <long>>::iterator itr;
    for(itr=m.begin();itr!=m.end();itr++){
        long f=itr->first;
        c=0;
        for(it=m[f].begin();it!=m[f].end();it++){
        c++;
        c%=mod;
        }
        p*=c;
        p%=mod;
    }
    cout << p;

    /*map<long, vector <long>> newmap;
    for(map<long, vector<long> >::iterator it=m.begin();it!=m.end();it++){
        long in = it->first;
        newmap[in]=m[in];
    }

    long sz = m.size();
    vector <long>::iterator at[sz+1];*/
}
