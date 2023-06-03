#include<stdio.h>
#include<stdlib.h>
#define MAX 100
struct stack
{
    int items[MAX];
    int top;
};
int icp(char symb)
{
    switch(symb)
    {
        case '+':return 1;
        case '-':return 1;
        case '*':return 3;
        case '/':return 3;
        case '^':return 6;
    }
}
int isp(char symb)
{
    switch(symb)
    {
        case '+':return 2;
        case '-':return 2;
        case '*':return 4;
        case '/':return 4;
        case '^':return 5;
        case '(': return 0;
    }
}
void push(char symb,struct stack* s1)
{
    if(s1->top==MAX-1)
    {
        printf("Stack overflow\n");
        exit(0);
    }
    s1->top++;
    s1->items[s1->top]=symb;
}
char pop(struct stack* s1)
{
    char symb;
    if(s1->top==-1)
    {
        printf("Stack Underflow\n");
        exit(0);
    }
    symb=s1->items[s1->top];
    s1->top--;
    return symb;
}
void postfix_conversion(char infix[100],char postfix[100],struct stack* s1)
{
    s1->top=-1;
    int i=0,j=0;
    char symb,topsymb;
    while(infix[i]!='\0')
    {
        symb=infix[i];
        if((symb>='A'&& symb<='Z') || (symb>='a'&& symb<='z'))
        {
            postfix[j]=symb;
            j++;
        }
        else if(symb=='(')
        {
            push(symb,s1);
        }
        else if(symb==')')
        {
            while((s1->items[s1->top]!='(')&& s1->top!=-1)
            {
                topsymb=pop(s1);
                postfix[j]=topsymb;
                j++;
            }
            s1->top--;
        }
        else
        {
            while((isp(s1->items[s1->top])>icp(symb))&& s1->top!=-1)
            {
                topsymb=pop(s1);
                postfix[j]=topsymb;
                j++;
            }
            push(symb,s1);
        }
        i++;
    }
    while(s1->top!=-1)
    {
        topsymb=pop(s1);
        postfix[j]=topsymb;
        j++;
    }
    postfix[j]='\0';
}
void main()
{
    char infix[100],postfix[100];
    struct stack s1;
    printf("Enter the infix expression\n");
    scanf("%s",infix);
    postfix_conversion(infix,postfix,&s1);
    printf("Postfix expression is:%s\n",postfix);
}