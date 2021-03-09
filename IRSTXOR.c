#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() 
{
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;i++)
	{
			long long int n,sum=0,k=1,j,v1,answer;
			scanf("%lld",&n);
		    while(n>=sum)
			{
				sum = pow(2,k);
				k++;
			}
	    j = pow(2,k-2);
		v1=sum-n;
		answer = (j-1)*((j-1)+v1);
		printf("%lld\n",answer);
			
	}
}