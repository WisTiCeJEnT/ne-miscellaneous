#include<iostream>
using namespace std;
void fx(int* x)
{
    *x += 1;
    cout << "X = " << x << " ";
    cout << "&X = " << &x << endl;
}
void fy(int*& y)
{
    *y += 1;
    cout << "Y = " << y << " ";
    cout << "&Y = " << &y << endl;
}
int main()
{
    int a=0;
    int* aptr = &a;
    cout << "aptr = " << aptr << " ";
    cout << "&aptr = " << &aptr << endl;
    fx(aptr);
    cout << a << endl;
    fy(aptr);
    cout << a << endl;
    return 0;
}
