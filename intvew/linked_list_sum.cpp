#include<bits/stdc++.h>

using namespace std;

struct node{
    node * next;
    int data;
};

node * reverse(node * head);
node * sum(node * h1, node * h2);

int main(){

    node *h1, *h2,  *ptr;

    int n, m;

    cin >> n >> m;
    h1 = new node;
    h2 = new node;
    
    ptr = h1;
    for(int i=0;i<n-1;i++){
        cin >> ptr->data;
        ptr->next = new node;
        ptr=ptr->next;
    }
    cin >> ptr->data;
    ptr->next = NULL;

    ptr = h2;
    for(int i=0;i<m-1;i++){
        cin >> ptr->data;
        ptr->next = new node;
        ptr=ptr->next;
    }
    cin >> ptr->data;
    ptr->next = NULL;


    ptr = sum(h1, h2);
    cout << "The sum";
    while(ptr!=NULL){
        cout << " " << ptr->data;
        ptr=ptr->next;
    }
    cout << endl;
 
    /*
    ptr = h1;
    cout << "The list:";
    while(ptr!=NULL){
        cout << " " << ptr->data;
        ptr=ptr->next;
    }

    head = reverse(head);
    ptr = head;
    cout << "The list in reverse order:";
    while(ptr!=NULL){
        cout << " " << ptr->data;
        ptr=ptr->next;
    }
    */
 
    return 0;
}

node * reverse(node * head){
    node * temp;
    if(head==NULL || head ->next == NULL)
        return head;
    else{
    temp = reverse(head->next);
    head->next->next = head;
    head->next = NULL;
    return temp;
    }
}

node * sum(node * h1, node * h2){
    h1 = reverse(h1);
    h2 = reverse(h2);
    node *s, *h;
    s = new node;
    h = s;
    node * ptr1, * ptr2;
    int cr = 0;
    int su;
    ptr1 = h1;
    ptr2 = h2;
    while(ptr1->next!=NULL && ptr2->next!=NULL){
        su = cr+((ptr1->data) +  (ptr2->data));
        s->data = su%10;
        cr = su/10;
        ptr1=ptr1->next;
        ptr2=ptr2->next;
        s->next = new node;
        s=s->next;
    }
    su = cr+((ptr1->data) +  (ptr2->data));
    s->data = su%10;
    cr = su/10;
    if(ptr1->next == NULL && ptr2->next != NULL){
        s->next = new node;
        s=s->next;
        ptr2 = ptr2->next;
        while(ptr2->next!=NULL){
            su = cr + (ptr2->data);
            s->data = su%10;
            cr = su/10;
            ptr2=ptr2->next;
            s->next = new node;
            s=s->next;
        }
        su = cr+ptr2->data;
        s->data = su%10;
        cr = su/10;
        if(cr){
            s->next = new node;
            s=s->next;
            s->data = cr;
            s->next = NULL;
        }
    }
    else if(ptr1->next != NULL && ptr2->next == NULL){
        s->next = new node;
        s=s->next;
        ptr1 = ptr1->next;
        while(ptr1->next!=NULL){
            su = cr + (ptr1->data);
            s->data = su%10;
            cr = su/10;
            ptr1=ptr1->next;
            s->next = new node;
            s=s->next;
        }
        su = cr+ptr1->data;
        s->data = su%10;
        cr = su/10;
        if(cr){
            s->next = new node;
            s=s->next;
            s->data = cr;
            s->next = NULL;
        }
    }
    else{
        if(cr){
                s->next = new node;
                s=s->next;
                s->data = cr;
                s->next = NULL;
        }
    }
    h1 = reverse(h1);
    h2 = reverse(h2);
    h = reverse(h);
    return h;
}
