#include <stdio.h>
#include <stdlib.h>
typedef struct node{
    int data;
    struct node * next;
}NODE;

NODE* root = NULL;

void printList()
{
    NODE* c = root;
    while(c != NULL)
    {
        printf("%d ",c -> data);
        c = c -> next;
    }
}

int appendList(int newData)
{
    NODE* c = root;
    NODE* newNode = (NODE*)malloc(sizeof(NODE));
    newNode -> data = newData;
    newNode -> next = NULL;
    if(c == NULL)
    {
        root = newNode;
        return 0;
    }
    while(c -> next != NULL)
    {
        c = c -> next;
    }
    c -> next = newNode;
    return 0;
}

int main()
{
    int inp;
    scanf("%d",&)
    appendList(1);
    appendList(2);
    appendList(4);
    printList();
    return 0;
}