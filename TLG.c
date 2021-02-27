#include <stdio.h>
#include<stdlib.h>

int main() 
{
	int n,p1win=0,p2win=0,p1=0,p2=0,diff=0;
	scanf("%d",&n);
	for(int i=0;i<n;i++)
		{
			int temp1,temp2;
			scanf("%d%d",&temp1,&temp2);
			p1=p1+temp1;
			p2=p2+temp2;
			diff=p1-p2;
			if(p1>p2)
			{
				diff=p1-p2;
				if(p1win<diff)
					{
						p1win=diff;
					}
				
			}
			else if(p1<p2)
				{
					    diff=p2-p1;
						if(p2win<diff)
						{
							p2win=diff;
						}
				}
	}
	if(p1win>p2win)
	{
		printf("1 %d",p1win);
	}
	else		
		{
		printf("2 %d",p2win);
	}
}