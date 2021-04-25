#include <stdio.h>

int main() 
{
	int r,o,c;
	scanf("%d%d%d",&r,&o,&c);
	int rem=20-o;
	int runs=rem*36;
	if(runs+c>r)
		printf("Yes\n");
	else
		printf("No\n");
}