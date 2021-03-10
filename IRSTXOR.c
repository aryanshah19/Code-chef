#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() 
{
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;i++)
	{
			long long int n,sum=0,d=1,j,v1,answer;
			scanf("%lld",&n);//6
		    while(n>=sum)
			{
				sum = pow(2,d);//8
				d++;//4
			}
	    j = pow(2,d-2);//4
		v1=sum-n;
		answer = (j-1)*((j-1)+v1);
		printf("%lld\n",answer);
			
	}
}