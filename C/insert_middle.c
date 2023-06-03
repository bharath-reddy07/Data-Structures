#include <stdio.h>
#include <stdlib.h>
struct node
{
    int data;
    struct node *address;
};
typedef struct node *NODE;
NODE insert_between(NODE start)
{
    printf("Enter item to be pushed\n");
    int item,n;
    scanf("%d", &item);
    printf("Enter node after which item to be pushed");
    scanf("%d", &n);
    
    NODE temp, current, ptr;
    int check = 0;
    temp = (NODE)malloc(sizeof(struct node));
    temp->data = item;
    temp->address = NULL;
    current = start;
    if (start == NULL)
    {
        start=temp;
    }
    else
    {
        while (current != NULL)
        {
            if (start->address == NULL)
            {
                if (start->data == n)
                {
                    check = 1;
                    printf("only one node..... inserting at end");
                    current->address = temp;
                }
            }
            else if (current->address == NULL)
            {
                if (current->data == n)
                {
                    check = 1;
                    printf("Last node .....inserting at end");
                    current->address = temp;
                }
            }
            else
            {
                if (current->data == n)
                {
                    printf("node inserted\n");
                    check = 1;
                    temp->address = current->address;
                    current->address = temp;
                }
            }
            current = current->address;
        }
        if (check == 0)
            printf("node not found");
        return start;
        }
    
}
void main()
{
    NODE start = NULL;
    start = insert_between(start);
}
