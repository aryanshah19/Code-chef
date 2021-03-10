#include <stdio.h>

int main() 
{
	int N,H,x;
	scanf("%d%d%d",&N,&H,&x);
	int time[N];
	for(int i=0;i<N;i++)
	{
		scanf("%d",&time[i]);
	}
	int flag=0,sum;
	for(int i=0;i<N;i++)
		{
			sum=x+time[i];
			if(sum>=H)
			{
				printf("YES\n");
				flag=1;
			}
			if(flag==1)
				break;
		}
	if(flag==0)
		printf("NO\n");
}