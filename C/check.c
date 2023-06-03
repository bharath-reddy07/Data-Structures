#include<stdio.h>
#include<stdlib.h>
#include<malloc.h>

struct node
{
    int data;
    struct node* leftnode;
    struct node* rightnode;
};
typedef struct node* NODE;

int count=0;

void count_node(NODE root)
{
    if(root==NULL)
        return;
    count_node(root->leftnode);
    count++;
    printf("%d",count);
    count_node(root->rightnode);
}

NODE getnode()
{
    NODE p;
    p=(NODE)malloc(sizeof(struct node));
    if(p==NULL)
    {
        printf("Insufficient Memory\n");
        exit(0);
    }
    p->leftnode=NULL;
    p->rightnode=NULL;
    return p;
}

NODE insert(NODE root,int value)
{
    if(root==NULL)
    {
        root=getnode();
        root->data=value;
        return root;
    }
    else
    {
        if(root->data==value)
        {
            printf("Duplicate Entry\n");
            return root;
        }
        else if(root->data>value)
        {
            root->leftnode=insert(root->leftnode,value);
            return root;
        }
        else
        {
            root->rightnode=insert(root->rightnode,value);
            return root;
        }
    }
}

void search(NODE root,int value)
{
    NODE temp;
    if(root==NULL)
    {
        printf("Binary Tree is empty\n");
    }
    else
    {
        temp=root;
        while(temp!=NULL)
        {
            if(temp->data==value)
            {
                printf("Element Is present\n");
                break;
            }
            else if(temp->data>value)
            {
                temp=temp->leftnode;
            }
            else
            {
                temp=temp->rightnode;
            }
        }
    }
}

NODE inorder_succ(NODE root)
{
    NODE r;
    if(root->leftnode==NULL)
    {
        return root;
    }
    r=inorder_succ(root->leftnode);
    return r;
}

NODE delete(NODE root,int value)
{
    NODE r;
    if(root==NULL)
    {
        printf("Element not present\n");
        return NULL;
    }
    if(root->data==value)
    {
        if(root->leftnode==NULL && root->rightnode==NULL)
        {
            free(root);
            return NULL;
        }
        else if(root->leftnode==NULL)
        {
            r=root->rightnode;
            free(root);
            return r;
        }
        else if(root->rightnode==NULL)
        {
            r=root->leftnode;
            free(root);
            return r;
        }
        else
        {
            r=inorder_succ(root->rightnode);
            root->data=r->data;
            root->rightnode=delete(root->rightnode,r->data);
            return root;
        }
    }
    if(root->data>value)
    {
        root->leftnode=delete(root->leftnode,value);
    }
    else
    {
        root->rightnode=delete(root->rightnode,value);
    }
    return root;
}

void inorder(NODE root)
{
    if(root==NULL)
    {
        return;
    }
    inorder(root->leftnode);
    printf("%d\n",root->data);
    inorder(root->rightnode);
}

void preorder(NODE root)
{
    if(root==NULL)
    {
        return;
    }
    printf("%d\n",root->data);
    preorder(root->leftnode);
    preorder(root->rightnode);
}

void postorder(NODE root)
{
    if(root==NULL)
    {
        return;
    }
    postorder(root->leftnode);
    postorder(root->rightnode);
    printf("%d\n",root->data);
}

void main()
{
    NODE root=NULL;
    int value,ch;
    printf("Binary Search Tree\n");
    for(;;)
    {
        printf("Enter your choice\n1. Insertion\t2. Search\t3. Deletion\t4. Inorder Traversal\t5. Preorder Traversal\t6. Postorder Traversal\t 7. Exit\n");
        scanf("%d",&ch);
        switch(ch)
        {
            case 1:
                printf("Enter the value you want to insert\n");
                scanf("%d",&value);
                root=insert(root,value);
                break;
            case 2:
                printf("Enter the value of the node you want to search\n");
                scanf("%d",&value);
                search(root,value);
                break;
            case 3:
                printf("Enter the value of the node you want to delete\n");
                scanf("%d",&value);
                root=delete(root,value);
                break;
            case 4:
                printf("Inorder traversal is:\n");
                inorder(root);
                break;
            case 5:
                printf("Preorder traversal is:\n");
                preorder(root);
                count_node(root);
                printf("Count is:%d",count);
                break;
            case 6:
                printf("Postorder traversal is:\n");
                postorder(root);
                break;
            case 7:
                exit(0);
        }
    }
}