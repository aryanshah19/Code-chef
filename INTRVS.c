#include <stdio.h>
#include<math.h>
int main() 
{
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;i++)
	{
		int n,k,flag=0;
		scanf("%d%d",&n,&k);
		int arr[n];
		for(int i=0;i<n;i++)
		{
			scanf("%d",&arr[i]);
		}
		double count=0;
		for(int i=0;i<n;i++)
			{
				if(arr[i]!=-1)
				{
					count++;
				}
			}
		int result=ceil((float)n/2);
		if(count<result)
		{
			printf("Rejected\n");
			flag=1;
		}
		else
			{
				for(int i=0;i<n;i++)
					{
						if(arr[i]>k)
							{
								printf("Too Slow\n");
								flag=2;
								break;
							}
					}
			}
		if(flag==0)
		{
			int coun=0;
			for(int i=0;i<n;i++)
				{
					if(arr[i]==1 || arr[i]==0)
						{
							coun++;
						}
				}
			if(coun==n)
				{
					printf("Bot\n");
					flag=3;
						
				}
				
		}
		if(flag==0) 
			{
			printf("Accepted\n");
		}
	}
}