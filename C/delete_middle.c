#include <stdio.h>
#include <stdlib.h>
struct node
{
    int data;
    struct node *address;
};
typedef struct node *NODE;
NODE delete_between(NODE start)
{
    int n;
    scanf("%d", &n);
    NODE temp, current, prev = NULL;
    int flag = 0;
    current = start;
    if (start == NULL)
    {
        printf("No Nodes present in linked list\n");
        return NULL;
    }
    while (current != NULL)
    {
        prev = current;
        temp = current;
        if (start->address == NULL)
        {
            if (start->data == n)
            {
                flag = 1;
                printf("only one node..... deleting\n");
                printf("Node deleted is %d\n", start->data);
                free(start);
                return NULL;
            }
        }
        else if (temp->address == NULL)
        {
            if (temp->data == n)
            {
                flag = 1;
                printf("Last node .....deleting at end\n");
                prev->address = NULL;
                printf("Node deleted is %d\n", temp->data);
                free(temp);
            }
        }
        else
        {
            if (temp->data == n)
            {
                printf("node deleted is %d\n", temp->data);
                flag = 1;
                prev->address = temp->address;
                free(temp);
            }
        }
        current = current->address;
    }
    if (flag == 0)
        printf("node not found");
    return start;
}
void display(NODE start)
{
    NODE temp;
    if (start == NULL)
    {
        printf("STACK EMPTY");
    }
    else
    {
        printf("Stack contents are \n");
        temp = start;
        while (temp != NULL)
        {
            printf("%d\t", temp->data);
            temp = temp->address;
        }
    }
}
void main()
{
    NODE start = NULL;
    start = delete_between(start);
}
