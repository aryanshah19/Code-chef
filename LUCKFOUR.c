#include <stdio.h>

int main(int argc, char *argv[]) 
{
			int n;
		scanf("%d",&n);
		for(int i=0;i<n;i++)
			{
				int arr[50],j=0,count=0,number;
				scanf("%d",&number);
				while(number>=10)
					{
						arr[j]=number%10;
						number=number/10;
						count++;
						j++;
					}
				arr[count]=number;
			    int n4=0;
				for(int i=0;i<=count;i++)
				{
					if(arr[i]==4)
					{
						n4++;
					}
				}
				printf("%d\n",n4);


			}
	
}