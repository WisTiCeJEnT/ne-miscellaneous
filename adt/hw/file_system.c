#include <stdlib.h>
#include <stdio.h>
#include <string.h>

typedef struct Content_Node { 
    struct Content_Node* next_content_ptr;
    char line_content[128];
} CONTENT_LIST;
typedef struct Header_Node { 
    struct Header_Node* next_file_ptr;
    char file_name[128];
    struct Content_Node* content_ptr;
} HEADER_LIST;

HEADER_LIST* root = NULL;

void new_file(char new_file_name[128])
{
    HEADER_LIST *n = (HEADER_LIST *)malloc(sizeof(HEADER_LIST));
    n -> next_file_ptr = NULL; 
    strcpy(n -> file_name, new_file_name);
    n -> content_ptr = NULL;
    if (root == NULL)
        root = n;
    else
    {
        HEADER_LIST *c = root;
        while(c -> next_file_ptr != NULL)
            c = c -> next_file_ptr;
        c -> next_file_ptr = n;
    }
}

void all_file()
{
    HEADER_LIST *c = root;
    while (c != NULL)
    {
        printf("%s\n",c -> file_name);
        c = c -> next_file_ptr;
    }
}

int main()
{
    //(HEADER_LIST *)malloc(sizeof(HEADER_LIST));
    new_file("a");
    new_file("b");
    new_file("a1");
    new_file("b2");
    all_file();
    return 0;
}