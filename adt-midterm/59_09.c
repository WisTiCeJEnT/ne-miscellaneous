#include <stdio.h>
char stack[10000];
int stackTop = 0;
void push(char item)
{
    if(stackTop<0)
        printf("overflow\n");
    stack[stackTop] = item;
    stackTop++;
}
void pop(char* item)
{
    if(stackTop<0)
        printf("pop empty stack\n");
    *item = stack[stackTop-1];
    stackTop--;
}
int stringDetect(char * string)
{
    //============= Start here =============
    char checker;
    int i=0;
    int stackCount = 0;
    while(string[i]!='R')
    {
        if(string[i] == 'a' || string[i] == 'b' || string[i] == 'c' || string[i] == 'd')
        {    
            push(string[i]);
            stackCount ++;
        }
        else
            return 1;
        i++;
    }
    i++;
    while(string[i]!='L')
    {
        if (stackCount==0)
            return 5;
        pop(&checker);
        if(string[i] != checker)
            return 2;
        stackCount --;
        i++;
    }
    if (stackCount!=0)
        return 5;
    i++;
    while(string[i]!='M')
    {
        if(string[i] == 'a' || string[i] == 'b' || string[i] == 'c' || string[i] == 'd')
        {    
            push(string[i]);
            stackCount ++;
        }
        else
            return 1;
        i++;
    }
    i++;
    while(string[i]!='\0')
    {
        if (stackCount==0)
            return 5;
        pop(&checker);
        if(string[i] != checker)
            return 2;
        stackCount --;
        i++;
    }
    return 0;
    //============= End here =============
}
int main()
{
    char s[1000];
    scanf("%s",s);
    printf("%d\n",stringDetect(s));
    return 0;
}