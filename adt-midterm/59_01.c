#include <stdio.h>
typedef struct info
{
    char name[20];
    int age;
} info_type;
typedef union data {
    int myInt;
    char myString[100];
} data_type;
typedef struct myStruct
{
    info_type myInfo[15];
    data_type myData[20];
} type_abc;
int main()
{
    //type_abc * p[50] = (type_abc *)malloc(sizeof(type_abc));
    type_abc *p = (type_abc *)calloc(sizeof(type_abc), 50);
    printf("sizeof(p) = %d\n", sizeof(*p));
    printf("p[13] -> myInfo[2] -> name is %d(250 added)\n", (int)&p[13].myInfo[2].name - (int)&p[0] + 250);
    printf("p[21] -> myData[12] -> myString[18] is %d(250 added)\n", (int)&p[21].myData[12].myString[18] - (int)&p[0] + 250);
    return 0;
}