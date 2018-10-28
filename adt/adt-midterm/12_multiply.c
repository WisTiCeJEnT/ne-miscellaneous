#include <stdio.h>
int Pred(int x)
{
    return x+1;
}
int Succ(int x)
{
    return x-1;
}
int myAddition(int x,int y)
{
    if(y > 0)
        return Pred(myAddition(x,Succ(y)));
    else if(y < 0)
        return Succ(myAddition(x,Pred(y)));
    else
        return x;
}

//==============================
int mySubtract(int x, int y)
{
   if(y > 0)
        return Succ(mySubtract(x,Succ(y)));
    else if(y < 0)
        return Pred(mySubtract(x,Pred(y)));
    else
        return x; 
}
int myMultiplication(int x,int y)
{
    if(y > 0)
        return myAddition(x,myMultiplication(x,Succ(y)));
    else if(y < 0)
        return mySubtract(myMultiplication(x,Pred(y)),x);
    else
        return 0;
}

//==============================

int main()
{
    int a,b;
    scanf("%d %d",&a,&b);
    printf("%d\n",myMultiplication(a,b));
    return 0;
}
