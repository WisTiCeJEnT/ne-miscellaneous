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

int main()
{
    int a,b;
    scanf("%d %d",&a,&b);
    printf("%d\n",myAddition(a,b));
    return 0;
}