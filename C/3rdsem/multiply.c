#include<stdio.h>
#include<stdlib.h>
#include<malloc.h>
struct node
{
    int coff;
    int exp;
    struct node* next;
};
typedef struct node* NODE;
NODE getnode();
NODE readpoly(NODE poly1);
NODE insert_last(NODE poly1,int coeff,int exp);
NODE mul(NODE poly1,NODE poly2);
NODE insert_update(NODE result,int coeff,int exp);
void display(NODE poly3);
void main()
{
    NODE poly1=NULL,poly2=NULL,poly3;
    printf("Enter the values of the first polynomial\n");
    poly1=readpoly(poly1);
    printf("Enter the values of the second polynomial\n");
    poly2=readpoly(poly2);
    printf("The result of multiplication of two polynomials is:\n");
    poly3=mul(poly1,poly2);
    display(poly3);
}
NODE getnode()
{
    NODE temp=(NODE)malloc(sizeof(struct node*));
    if(temp==NULL)
    {
        printf("Insufficient Memory\n");
        exit(0);
    }
    temp->next=NULL;
    return temp;
}
NODE readpoly(NODE poly1)
{
    int n,i;
    int coeff,exp;
    printf("Enter the number of values in the polynomial\n");
    scanf("%d",&n);
    for(i=1;i<=n;i++)
    {
        printf("Enter the coefficient\n");
        scanf("%d",&coeff);
        printf("Enter the exponent\n");
        scanf("%d",&exp);
        poly1=insert_last(poly1,coeff,exp);
        display(poly1);
    }
    return poly1;
}
NODE insert_last(NODE poly1,int coeff,int exp)
{
    NODE temp=getnode();
    NODE cur;
    temp->coff=coeff;
    temp->exp=exp;
    if(poly1==NULL)
    {
        return temp;   
    }
    cur=poly1;
    while(cur->next!=NULL)
    {
        cur=cur->next;
    }
    cur->next=temp;
    return poly1;
}
NODE mul(NODE poly1,NODE poly2)
{
    NODE result=NULL;
    NODE p,q;
    int coeff,exp;
    if(poly1==NULL || poly2==NULL)
    {
        printf("The Resultant polynomial is of order 0\n");
        exit(0);
    }
    p=poly1;
    while(p!=NULL)
    {
        q=poly2;
        while(q!=NULL)
        {
            coeff=p->coff*q->coff;
            exp=p->exp+q->exp;
            result=insert_update(result,coeff,exp);
            q=q->next;
        }
        p=p->next;
    }
    return result;
}
NODE insert_update(NODE result,int coeff,int exp)
{
    NODE temp=getnode();
    NODE cur,prev=NULL;
    int linked=0;
    temp->coff=coeff;
    temp->exp=exp;
    if(result==NULL)
    {
        return temp;
    }
    cur=result;
    while(cur!=NULL)
    {
        if(cur->exp==exp)
        {
            cur->coff+=coeff;
            linked=1;
            free(temp);
            break;
        }
        if(cur->exp>exp)
        {
            break;
        }
        prev=cur;
        cur=cur->next;
    }
    if(!linked)
    {
        if(prev==NULL)
        {
            temp->next=result;
            result=temp;
        }
        else
        {
            temp->next=prev->next;
            prev->next=temp;
        }
    }
    return result;
}
void display(NODE poly3)
{
    NODE cur;
    if(poly3==NULL)
    {
        printf("Empty polynomial\n");
        exit(0);
    }
    cur=poly3;
    while(cur!=NULL)
    {
        if(cur->coff>0)
        {
            printf("+");
        }
        printf("%d x^%d",cur->coff,cur->exp);
        cur=cur->next;
    }
    printf("\n");
}