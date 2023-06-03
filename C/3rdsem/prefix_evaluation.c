#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#define MAX 100
struct stack
{
    float items[MAX];
    int top;
};
void push(struct stack* s1,float symb)
{
    if(s1->top==MAX-1)
    {
        printf("Stack Overflow\n");
        exit(0);
    }
    s1->top++;
    s1->items[s1->top]=symb;
    printf("Pushed:%f\n",s1->items[s1->top]);
}
float pop(struct stack* s1)
{
    float x;
    if(s1->top==-1)
    {
        printf("Stack underflow\n");
        exit(0);
    }
    x=s1->items[s1->top];
    s1->top--;
    printf("popped symbol:%f\n",x);
    return x;
}
float calculate(int oprnd1,int oprnd2,char operator)
{
    switch(operator)
    {
        case '+':return(oprnd1+oprnd2);
        case '-':return(oprnd1-oprnd2);
        case '*':return(oprnd1*oprnd2);
        case '/':
            if(oprnd2==0)
            {
                printf("Divide by zero error\n");
                exit(0);
            }
            return(oprnd1/oprnd2);
        case '^':return(pow(oprnd1,oprnd2));
    }
}
float prefix_eval(struct stack* s1,char prefix[100])
{
    s1->top=-1;
    float oprnd1,oprnd2,result;
    int i;
    char symb;
    i=strlen(prefix)-1;
    while(i>=0)
    {
        symb=prefix[i];
        if(symb>='0'&& symb<='9')
        {
            symb=(float)symb -48;
            push(s1,symb);
        }
        else
        {
            oprnd1=pop(s1);
            oprnd2=pop(s1);
            result=calculate(oprnd1,oprnd2,symb);
            push(s1,result);
        }
        i--;
    }
    result=pop(s1);
    return result;
}
void main()
{
    char prefix[100];
    float result;
    struct stack s1;
    printf("Enter the prefix expression\n");
    scanf("%s",prefix);
    result=prefix_eval(&s1,prefix);
    printf("The result of evaluation of the prefix expression is:%f\n",result);
}