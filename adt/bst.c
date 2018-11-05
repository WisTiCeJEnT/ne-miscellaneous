#include <stdio.h>
#include <stdlib.h>
typedef struct Tree_node{
    struct Tree_node* l;
    struct Tree_node* r;
    struct Tree_node* p;
    int hight;
    int data;
}TREE_NODE;

TREE_NODE * root = NULL;

void print_tree(TREE_NODE* c)
{
    if(c != NULL)
    {
        print_tree(c -> l);
        printf("%d %d\n",c -> data, c -> hight);
        print_tree(c -> r);
    }
}

int insert_tree(int n)
{
    TREE_NODE* new_node = (TREE_NODE *)malloc(sizeof(TREE_NODE));
    new_node -> data = n;
    new_node -> hight = 0;
    new_node -> l = NULL;
    new_node -> r = NULL;
    TREE_NODE*c = root;
    if(root == NULL)
    {
        new_node -> p = NULL;
        root = new_node;
        return 0;
    }
    while(1)
    {
        if(c -> data < n)
        {
            if(c -> r == NULL)
            {
                new_node -> p = c;
                c -> r = new_node;
                if(c -> l == NULL)
                {
                    while(c != NULL)
                    {
                        c -> hight += 1;
                        c = c -> p;
                    }
                }
                return 0;
            }
            else
            {
                c = c -> r;
            }
        }
        else
        {
            if(c -> l == NULL)
            {
                new_node -> p = c;
                c -> l = new_node;
                if(c -> r == NULL)
                {
                    while(c != NULL)
                    {
                        c -> hight += 1;
                        c = c -> p;
                    }
                }
                return 0;
            }
            else
            {
                c = c -> l;
            }
        }
    }
}
int main()
{
    int inp;
    scanf("%d",&inp);
    while(inp > -1)
    {
        insert_tree(inp);
        scanf("%d",&inp);
    }
    print_tree(root);
    return 0;
}
