#include <stdio.h>
#include <stdlib.h>
typedef struct Node{
    char Info;
    struct Node *Left;
    struct Node *Right;
} TYPE_NODE;
typedef TYPE_NODE *TYPE_NODEPTR;

TYPE_NODEPTR NewNode(char Info)
{
    TYPE_NODE *n = (TYPE_NODE *)malloc(sizeof(TYPE_NODE));
    n -> Info = Info;
    n -> Left = NULL;
    n -> Right = NULL;
    return n;
}
void InsertFirst(TYPE_NODEPTR *L, TYPE_NODEPTR N)
{
//Answer start from here
    N -> Left = L;
    N -> Right = (*L) -> Right;
    (*L) -> Right = &N;
//answer end here
}

int main()
{
    TYPE_NODEPTR *root = NewNode('a');
    TYPE_NODEPTR *newnode = NewNode('b');
    InsertFirst(root,*newnode);
    int i=2;
    TYPE_NODEPTR *c = root;
    while(i!=0)
    {
        printf("%c",(*c)->Info);
        i--;
    }
    return 0;
}
