#include<stdio.h>
#include<stdlib.h>
struct node
{
    int data;
    struct node *address;
};
typedef struct node *NODE;
NODE start=NULL;
NODE createnode(int data)
{
    NODE ptr;
    ptr=(NODE)malloc(sizeof(struct node));
    if(ptr==NULL)
    {
        printf("Insufficient memory\n");
        exit(0);
    }
    ptr->data=data;
    ptr->address=NULL;
    return ptr;
}
NODE insertLast(int data)
{
    NODE ptr=createnode(data);
    if(start==NULL)
    {
        start=ptr;
    }
    else
    {
        NODE temp=start;
        while (temp->address!=NULL)
        {
            temp=temp->address;
        }
        temp->address=ptr;
    }
}
NODE deleteBegin()
{
    NODE temp;
    if(start==NULL)
    {
        printf("List is Empty\n");
    }
    else
    {
        temp=start;
        start=start->address;
        printf("The Node deleted is:%d\n",temp->data);
        free(temp);
    }
}
NODE traverse()
{
    NODE temp;
    temp=start;
    while(temp!=NULL)
    {
        printf("%d\n",temp->data);
        temp=temp->address;
    }
}
void main()
{
    insertLast(25);
    insertLast(20);
    insertLast(23);
    insertLast(22);
    deleteBegin();
    traverse();
}