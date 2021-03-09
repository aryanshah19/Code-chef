#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() 
{
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;i++)
	{
			char input[100000];
			scanf("%s",input); 
			long int groups=0,count=0;
			int flag=0;
			count=strlen(input);
			for(long int i=0;i<count;i++)
			{
				if(input[i]=='1' && flag==0)
				{
					groups++;
					flag=1;
				}
				if(input[i]=='0')
					{
						flag=0;
					}
			}
            printf("%ld\n",groups); 
	}
}