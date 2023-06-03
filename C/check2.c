#include<stdio.h>
#include<stdlib.h>
#include<malloc.h>
struct node
{
    int data;
    struct node* next;
};
typedef struct node* NODE;

NODE last=NULL;

NODE getnode()
{
    NODE p=(NODE)malloc(sizeof(struct node));
    p->next=NULL;
    return p;
}

void insert()
{
    NODE p;
    int value;
    printf("Enter the value\n");
    scanf("%d",&value);
    if(last==NULL)
    {
        p=getnode();
        p->data=value;
        last=p;
        last->next=last;
    }
    else
    {
        p=getnode();
        p->data=value;
        p->next=last->next;
        last->next=p;
        last=p;
    }
}

NODE elect(int N,int K,int j,NODE start)
{
    NODE temp=start;
    NODE prev=NULL;
    NODE leader;
    if(N==1)
    {
        printf("%d",last->data);
        return last;
    }
    for(int i=j;i<j+K-1;i++)
    {
        prev=temp;
        temp=temp->next;
    }
    prev->next=temp->next;
    printf("Temp data %d\n",temp->data);
    if(temp==last)
    {
        last=prev;
    }
    free(temp);
    start=prev->next;
    j=j+K-1;
    N--;
    leader=elect(N,K,j,start);
    return leader;
}

NODE elect2(int N,int K,int j,NODE start)

void main()
{
    NODE leader;
    NODE start;
    int N,K,j=1;
    printf("Enter the total number of participants\n");
    scanf("%d",&N);
    printf("Enter K\n");
    scanf("%d",&K);
    for(int i=0;i<5;i++)
    {
        insert();
    }
    start=last->next;
    leader=elect(N,K,j,start);
    printf("The leader is %d:",leader->data);
}