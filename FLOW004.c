#include <stdio.h>
int main() 
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
		int sum=0;
		sum=arr[0]+arr[count];
		printf("%d\n",sum);
	}
}