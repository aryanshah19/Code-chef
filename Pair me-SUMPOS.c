#include <stdio.h>

int main() 
{
	int n,x,y,z;
	scanf("%d",&n);
	for(int i=0;i<n;i++)
	{
		scanf("%d%d%d",&x,&y,&z);
		if(x>=1 && y>=1 && z>=1 && x<=1000 && y<=1000 && z<=1000)
			{
				if((x==(y+z)) || (y==(x+z)) || (z==(y+x)))
					{
						printf("YES\n");
					}
				else 
					{
						printf("NO\n");
					}
			}
	}
	return 0;
}