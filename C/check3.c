#include<stdio.h>
#include<stdlib.h>
#include<malloc.h>
void main()
{
    int n,*x;
    printf("Enter the no of elements\n");
    scanf("%d",&n);
    *x=(int *)malloc(n*sizeof(int));
    for(int i=0;i<n;i++)
    {
        scanf("%d",&x[i]);
    }
    for(int i=0;i<n;i++)
    {
        printf("%d",x[i]);
    }
}