#include<stdio.h>
#include<stdlib.h>
void main()
{
    int count=0;
    for(int i=1;i<=100;i++)
    {
        if(i%5!=0 && i%7!=0)
        {
            count++;
        }
    }
    printf("The count is:%d",count);
}