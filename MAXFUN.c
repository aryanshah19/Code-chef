#include <stdio.h>
#include <stdlib.h>

void bubble_sort(long arr[],int n)
{
	long i,j,temp;
	for(i=0;i<n;i++)
		{
			for(j=i+1;j<n;j++)
				{
					if(arr[i]>arr[j])
						{
							temp=arr[i];
							arr[i]=arr[j];
							arr[j]=temp;
						}
				}
		}
}

int main() 
{
	int t;
	int n;
	scanf("%d",&t);
			for(int i=0;i<t;i++)
				{
					long int max=-1000000000;
					scanf("%d",&n);
                    if(n>=3 && n<=10000)
						{
							long arr[10000]={-1000000000};
							for(int i=0;i<n;i++)
								{
									scanf("%ld",&arr[i]);
								}
							
							bubble_sort(arr,n);
							max=(arr[n-1]-arr[0])*2;
							printf("%ld\n",max);
						}
				}
	return 0;
}