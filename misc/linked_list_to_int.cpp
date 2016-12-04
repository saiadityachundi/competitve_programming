#include<iostream>
#include<cmath>

using namespace std;

struct Node{

    int data;
    struct Node * next;
};

typedef struct Node nd;

int func(nd * head, int *d){

    if(head->next==NULL){
        *d=1;
        return head->data;
    }

    else{
        int y=func(head->next,d);
        y+=((head->data)*pow(10,*d));
        (*d)=(*d)+1;
        return y;
    }
}


int main(){

    nd * head=NULL,*lpt,*pt;
    lpt=head;

    int n;
    cin >> n;

    int x;

    for(int i=0;i<n;i++){
        cin >> x;
        pt=(nd *)malloc(sizeof(nd));
        pt->data=x;
        pt->next=NULL;
        if(lpt!=NULL){
            lpt->next=pt;
            lpt=lpt->next;
        }
        else{
            head=pt;
            lpt=pt;
        }
    }

    pt=head;

    int* d = (int*) malloc(sizeof(int));
    int num=func(head, d);
    cout << num << endl;
    return 0;
}
