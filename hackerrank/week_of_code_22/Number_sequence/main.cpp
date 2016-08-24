#define mod 10000009

#include <map>
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int next(map<long, vector<long> > & newmap, map<long, vector<long>::iterator > & mit, long kind){

    if(newmap.count(kind)==0)
        return 0;
    map<long, vector <long>>::reverse_iterator riter(++newmap.find(kind));
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
        return 0;

    map<long, vector<long>>::iterator iter=newmap.find(riter->first);
    map<long, vector<long>>::iterator iter0=newmap.begin();
    long i;
    long r;
    long j,jr;
    vector <long>::iterator it2;
    
    for(iter0 = iter;iter0!=newmap.end();iter0++){
        for(it1=newmap.begin();it1!=iter0;it1++){
            i = it1->first;
            r = *mit[i];
            j=iter0->first;
            if(j%i==0){
                it2 = mit[j];
                while(*it2%i != r && it2 != newmap[j].end())
                    it2++;
                if(it2==newmap[j].end()){
                    mit[j]=newmap[j].begin();
                    return next(newmap, mit, j-1);
                }
                mit[j]=it2;
            }
        }
    }
    return kind;
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
                            cout << 0 ;
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

    map<long, vector<long>> newmap=m;
    map<long, vector<long>::iterator> mit;
    
    for(map<long, vector <long>>::iterator iter=newmap.begin();iter != newmap.end();iter++){
        mit[iter->first]=newmap[iter->first].begin();
    }
    
    long i,r;

    long c=0;
    bool isBreak=false;
    for(map<long, vector<long>>::iterator iter=newmap.begin();iter!=newmap.end();iter++){
        for(map<long, vector<long>>::iterator iter1=newmap.begin();iter1!=iter;iter1++){
            j=iter->first;
            i=iter1->first;
            r=*mit[i];
            if(j%i==0 && *mit[j]%i!=r){
                isBreak = true;
                break;
            }
        }
        if(isBreak)
            break;
    }
    if(!isBreak)
        c=1;
    
    long index;
    map<long, vector<long>>::reverse_iterator riter = newmap.rbegin();
    if(riter!=newmap.rend())
        index = riter->first;
    
    if(!newmap.empty())
        while(index=next(newmap, mit, index)){
            c++;
            c%=mod;
        }
    
    cout << c;
    
}
