#include <stdio.h>
int main()
{
    char s[10];
    int i;
    for(i=0;i<10;i++)
    {
        s[i] = '-';
    }
    s[5] = '\0';
    printf("%s\n",s);
    return 0;
}
