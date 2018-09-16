#include <stdio.h>
typedef struct info { char name[20]; int age;
} info_type;
typedef union data { int myInt;
char myString[100]; } data_type;
typedef struct myStruct { info_type myInfo[15]; data_type myData[20];
} type_abc;
int main()
{
    //type_abc * p[50] = (type_abc *)malloc(sizeof(type_abc));
    printf("%ul",sizeof(type_abc));
    return 0;
}