#include <stdio.h>

int main() 
{
	int n,max=0;
	scanf("%d",&n);
	if(n<=1000 && n>=2)
		{
			for(int i=1;i<11;i++)
				{
					if(n%i==0 && i>max)
						max=i;
				}
			printf("%d\n",max);
		}
	
}