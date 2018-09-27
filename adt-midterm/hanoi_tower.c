#include<stdio.h>

void hanoi(int n, char f, char a, char t){
	if(n>0){
		hanoi(n-1, f, t, a);
		printf("Moving %d from %c to %c\n",n,f,t);
		hanoi(n-1, a, f, t);
	}
}

int main(){
	int n;
	char f='A', a='B', t='C';
	printf("n: ");
	scanf("%d",&n);
	hanoi(n,f,a,t);
	return 0;
}
