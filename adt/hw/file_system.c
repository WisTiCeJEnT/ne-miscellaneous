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

int new_file(char new_file_name[128])
{
    HEADER_LIST *n = (HEADER_LIST *)malloc(sizeof(HEADER_LIST));
    n -> next_file_ptr = NULL; 
    strcpy(n -> file_name, new_file_name);
    n -> content_ptr = NULL;
    if (root == NULL)
    {
        root = n;
    }
    else
    {
        HEADER_LIST *c = root;
        while(c -> next_file_ptr != NULL)
        {
            if(strcmp(c -> file_name, new_file_name) == 0)
                return 1;
            c = c -> next_file_ptr;
        }
        if(strcmp(c -> file_name, new_file_name) == 0)
            return 1;
        c -> next_file_ptr = n;
    }
    return 0;
}

int rename_file(char old_file_name[128], char new_file_name[128])
{
    HEADER_LIST *c = root;
    HEADER_LIST *old_file_ptr = NULL;
    while(c != NULL)
    {
        if(strcmp(c -> file_name, old_file_name) == 0)
            old_file_ptr = c;
        if(strcmp(c -> file_name, new_file_name) == 0)
            return 2; //New file name already exist
        c = c -> next_file_ptr;
    }
    if(old_file_ptr == NULL)
        return 1; //File not found
    strcpy(old_file_ptr -> file_name, new_file_name);
    return 0;
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
    printf("%d\n",new_file("a"));
    printf("%d\n",new_file("a"));
    printf("%d\n",new_file("b"));
    printf("%d\n",new_file("b"));
    printf("%d\n",new_file("c"));
    printf("%d\n",new_file("c"));
    printf("%d\n",new_file("c"));
    printf("%d\n",new_file("d"));
    printf("%d\n", rename_file("a", "e"));
    printf("%d\n", rename_file("b", "c"));
    all_file();
    return 0;
}