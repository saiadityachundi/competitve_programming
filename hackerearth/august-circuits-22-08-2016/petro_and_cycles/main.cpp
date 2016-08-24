#include<bits/stdc++.h>

using namespace std;

int main(){
    
    long n,m,x,y;
    cin >> n && cin >> m;

    map<long, vector<long>> ed, nd;                       // ed gives nodes of that edge e, while nd gives all edges containing that node.
    map<long, map<long, long>> epair;
    for(long i=0;i<m;i++){
        cin >> x && cin >> y;
        ed[i+1] = vector<long>();
        
        ed[i+1].push_back(x);
        if(nd.count(x)==0)
           nd[x] = vector<long>();
        nd[x].push_back(i+1);

        ed[i+1].push_back(y);
        if(nd.count(y)==0)
           nd[y] = vector<long>();
        nd[y].push_back(i+1);

       if(epair.count(x)==0)
          epair[x] = map<long, long>();

       epair[x][y] = i+1;

       if(epair.count(y)==0)
          epair[y] = map<long, long>();

       epair[y][x] = i+1;
    }

    map<long, vector<long>> ea;
    for(long i=1;i<=m;i++){
        ea[i] = vector<long>();
        x = ed[i][0];
        y = ed[i][1];
        for(vector<long>::iterator itr = nd[x].begin(); itr!=nd[x].end(); itr++)
            if(*itr != i)
               ea[i].push_back(*itr); 
        for(vector<long>::iterator itr = nd[y].begin(); itr!=nd[y].end(); itr++)
            if(*itr != i)
               ea[i].push_back(*itr); 
 
    }

    map<long, long> elist;
    map<long, long>::iterator iter;
    vector<long>::iterator iter1, iter2, iter3;
    long x1,y1,x2,y2;
    bool isbreak = false;
    bool mark[m+1];
    vector<vector<long>> trip;
    vector<vector<long>>::reverse_iterator vriter;
    long e,e1,e2, max, min, mid;

    for(long i=1;i<m+1;i++)
        mark[i] = false;

    mark[0] = true;                         // Ignore this value

    for(long i=0;i<m;i++)
        elist[i+1] = i+1;

    while(!elist.empty()){
        iter = elist.begin();
        e = iter->first;
        x = ed[e][0];
        y = ed[e][1];
        
        for(iter1 = nd[x].begin(); iter1 != nd[x].end(); iter1++)
            for(iter2 = nd[y].begin(); iter2 != nd[y].end(); iter2++){
                e1 = *iter1;
                e2 = *iter2;
                if((e1 != e) && (e2 != e)){
                    x1 = ed[e1][0];
                    y1 = ed[e1][1];
                    x2 = ed[e2][0];
                    y2 = ed[e2][1];

                    if(e>=e1)
                        if(e>=e2){
                            max = e;
                            if(e1>=e2){
                                mid = e1;
                                min = e2; 
                            }
                            else{
                                mid = e2;
                                min = e1;
                            }
                        }
                        else{
                            max = e2;
                            if(e1>=e){
                                mid = e1;
                                min = e2;
                            }
                            else{
                                mid = e2;
                                min = e1; 
                            }
                        }
                    else
                        if(e1>=e2){
                            max = e1;
                            if(e>=e2){
                                 mid = e;
                                 min = e2;
                            }
                            else{
                                mid = e2;
                                min = e; 
                            }
                        }
                        else{
                            max = e2;
                            if(e1>=e){
                                 mid = e1;
                                 min = e;
                            }
                            else{
                                mid = e;
                                min = e1; 
                            }
                        }

                    if(x1==x && x2==y && y1 == y2 && !mark[e1] && !mark[e2]){
                        trip.push_back(vector<long>());
                        vriter = trip.rbegin();

                        (*vriter).push_back(min);
                        (*vriter).push_back(mid);
                        (*vriter).push_back(max);

                        mark[e] =   true;
                        mark[e1]=   true;
                        mark[e2]=   true;

                        iter = elist.find(e);
                        elist.erase(iter);

                        iter = elist.find(e1);
                        elist.erase(iter);

                        iter = elist.find(e2);
                        elist.erase(iter);
                    }

                    else if(x1==x && y2==y && y1 == x2 && !mark[e1] && !mark[e2]){
                        trip.push_back(vector<long>());
                        vriter = trip.rbegin();
                        (*vriter).push_back(min);
                        (*vriter).push_back(mid);
                        (*vriter).push_back(max);

                        mark[e] =   true;
                        mark[e1]=   true;
                        mark[e2]=   true;

                        iter = elist.find(e);
                        elist.erase(iter);

                        iter = elist.find(e1);
                        elist.erase(iter);

                        iter = elist.find(e2);
                        elist.erase(iter);
                    
                    }

                    else if(y1==x && x2==y && x1 == y2 && !mark[e1] && !mark[e2]){
                        trip.push_back(vector<long>());
                        vriter = trip.rbegin();
                        (*vriter).push_back(min);
                        (*vriter).push_back(mid);
                        (*vriter).push_back(max);

                        mark[e] =   true;
                        mark[e1]=   true;
                        mark[e2]=   true;

                        iter = elist.find(e);
                        elist.erase(iter);

                        iter = elist.find(e1);
                        elist.erase(iter);

                        iter = elist.find(e2);
                        elist.erase(iter);
                     
                    }

                    else if(y1==x && y2==y && x1 == x2 && !mark[e1] && !mark[e2]){
                        trip.push_back(vector<long>());
                        vriter = trip.rbegin();
                        (*vriter).push_back(min);
                        (*vriter).push_back(mid);
                        (*vriter).push_back(max);

                        mark[e] =   true;
                        mark[e1]=   true;
                        mark[e2]=   true;

                        iter = elist.find(e);
                        elist.erase(iter);

                        iter = elist.find(e1);
                        elist.erase(iter);

                        iter = elist.find(e2);
                        elist.erase(iter);
                    
                    }
                }
            }
    }

    cout << trip.size() << endl;

    vector<long>::iterator vit;

    for(long i=0;i<trip.size();i++){
       for(vit = trip[i].begin();vit != trip[i].end(); vit++)
          cout << *vit << " ";
        cout << endl; 
    }

    return 0;
}
