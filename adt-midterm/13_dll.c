#include <stdio.h>
typedef struct node
{
    int data;
    struct node * prev;
    struct node * next;
} NODE, *NODEPTR;
int main()
{
    NODE * starter = malloc(sizeof(NODE));
    starter->data = 0;
    starter->next = NULL;
    starter->prev = NULL;
    return 0;
}