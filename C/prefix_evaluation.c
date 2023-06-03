#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#define MAX 100
struct stack
{
    int items[MAX];
    int top;
};
struct stack s1;
int prefix_eval(char prefix[100])
{
    int length,i,opnd1,opnd2,ans;
    s1.top=-1;
    length=strlen(prefix);
    i=length-1;
    while(i>=0)
    {
        if(prefix[i]>='0'&&prefix[i]<='9')
        {
            s1.top++;
            s1.items[s1.top]=prefix[i]-'0';
        }
        else
        {
            opnd1=s1.items[s1.top];
            s1.top--;
            opnd2=s1.items[s1.top];
            switch(prefix[i])
            {
                case '+':
                    ans=opnd1+opnd2;
                    break;
                case '-':
                    ans=opnd1-opnd2;
                    break;
                case '*':
                    ans=opnd1*opnd2;
                    break;
                case '/':
                    ans=opnd1/opnd2;
                    break;
                case '^':
                    ans=pow(opnd1,opnd2);
                    break;
            }
            s1.items[s1.top]=ans;        
        }
        i--;
    }
    return s1.items[s1.top];
    
}
void main()
{
    char prefix[100];
    int ans;
    printf("Enter the prefix expression\n");
    scanf("%s",prefix);
    ans=prefix_eval(prefix);
    printf("Ans is:%d\n",ans);
}