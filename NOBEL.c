#include <stdio.h>
#include <stdlib.h>
#include <string.h>
void quicksort(int arr[],int first,int last)
{
	int i, j, pivot, temp;
	
	if(first<last){
		pivot=first;
		i=first;
		j=last;
		
		while(i<j)
			{
			while(arr[i]<=arr[pivot]&&i<last)
				i++;
			while(arr[j]>arr[pivot])
				j--;
			if(i<j){
				temp=arr[i];
				arr[i]=arr[j];
				arr[j]=temp;
			}
		}
		temp=arr[pivot];
		arr[pivot]=arr[j];
		arr[j]=temp;
		quicksort(arr,first,j-1);
		quicksort(arr,j+1,last);
	}
}
int main() 
{
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;i++)
	{
		int N,M;
		scanf("%d%d",&N,&M);
		int arr[N];
		for(int i=0;i<N;i++)
			{
				scanf("%d",&arr[i]);
			}
		quicksort(arr, 0, N-1);
		int flag=arr[0],ans=0,count=1;
		for(int i=1;i<N;i++)
			{
				if(count!=M)
					{
						if(arr[i]!=flag)
							{
								flag=arr[i];
								count++;
							}
					}
				else 
					{
					break;
					}
			}
		if(count<M)
			printf("Yes\n");
		else
			printf("No\n");

	}
}