#include<stdio.h>
#include<stdlib.h>
#define MAX 100
struct stack
{
    int items[MAX];
    int top;
};
int ISP(char symb)
{
    switch (symb)
    {
    case '+':
        return 12;
    case '-':
        return 12;
    case '*':
        return 13;
    case '/':
        return 13;
    case '^':
        return 14;
    case '(':
        return 0;
    }
}
int ICP(char symb)
{
    switch (symb)
    {
    case '+':
        return 12;
    case '-':
        return 12;
    case '*':
        return 13;
    case '/':
        return 13;
    case '^':
        return 14;
    }
}
void infix_postfix(char infix[100],char postfix[100],struct stack *s1)
{
    int i=0,j=0;
    s1->top=-1;
    while(infix[i]!='\0')
    {
        if(infix[i]>='A'&&infix[i]<='Z'|| infix[i]>='a'&& infix[i]<='z')
        {
            postfix[j]=infix[i];
            j++;
        }
        else
        {
            if(infix[i]=='('|| infix[i]=='^')
            {
                s1->top++;
                s1->items[s1->top]=infix[i];
            }
            else if(infix[i]==')')
            {
                while(s1->items[s1->top]!='(')
                {
                    postfix[j]=s1->items[s1->top];
                    s1->top--;
                    j++;
                }
                if(s1->top!=-1)
                {
                    s1->top--;
                }
            }
            else
            {
                int isp,icp;
                isp=ISP(s1->items[s1->top]);
                icp=ICP(infix[i]);
                if(icp>isp)
                {
                    s1->top++;
                    s1->items[s1->top]=infix[i];
                }
                else
                {
                    while()
                }
            }
        }
    }
}
void main()
{
    char infix[100],postfix[100];
    struct stack s1;
    printf("Enter the infix expression\n");
    scanf("%s",infix);
    infix_postfix(infix,postfix,&s1);
    printf("The final postfix expression is:%s",postfix);
}