#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define MAX 100
struct stack
{
    int items[MAX];
    int top;
};
struct stack s1;
void infix_reverse(char infix[100],char reverse_infix[100])
{
    int i=0,length,j;
    length=strlen(infix);
    j=length-1;
    while(j>=0)
    {
        if(infix[j]=='(')
        {
            reverse_infix[i]=')';
        }
        else if(infix[j]==')')
        {
            reverse_infix[i]='(';
        }
        else
        {
            reverse_infix[i]=infix[j];
        }
        i++;
        j--;
    }
    reverse_infix[i]='\0';
}
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
void infix_postfix(char infix[100],char postfix[100])
{
    int i=0,j=0,isp,icp;
    s1.top=-1;
    while(infix[i]!='\0')
    {
        if((infix[i])>='A' && infix[i]<='Z' || infix[i]>='a'&&infix[i]<='z')
        {
            postfix[j]=infix[i];
            j++;
        }
        else
        {
            if(infix[i]=='('|| infix[i]=='^')
            {
                s1.top+=1;
                s1.items[s1.top]=infix[i];
            }
            else if(infix[i]==')')
            {
                while(s1.items[s1.top]!='(')
                {
                    postfix[j]=s1.items[s1.top];
                    s1.top--;
                    j++;
                }
                if(s1.top!=-1)
                {
                    s1.top--;
                }
                
            }
            else
            {
                if(s1.top==-1)
                {
                    s1.top++;
                    s1.items[s1.top]=infix[i];
                }
                else
                {
                    icp=ICP(infix[i]);
                    isp=ISP(s1.items[s1.top]);
                    if(icp>isp)
                    {
                        s1.top++;
                        s1.items[s1.top]=infix[i];
                    }
                    else
                    {
                        while(isp>=icp && s1.top>=0)
                        {
                            postfix[j]=s1.items[s1.top];
                            s1.top-=1;
                            isp=ISP(s1.items[s1.top]);
                            j++;
                        }
                        s1.top++;
                        s1.items[s1.top]=infix[i];
                    }
                }
            }
        }
        i++;
    }
    while(s1.top!=-1)
    {
        postfix[j]=s1.items[s1.top];
        j++;
        s1.top--;
    }
    postfix[j]='\0';
}
void main()
{
    char infix[100],postfix[100],reverse_infix[100],prefix[100];
    printf("Enter the infix expression\n");
    scanf("%s",infix);
    infix_reverse(infix,reverse_infix);
    //printf("%s\n",reverse_infix);
    infix_postfix(reverse_infix,postfix);
    //printf("%s",postfix);
    infix_reverse(postfix,prefix);
    printf("%s",prefix);
}