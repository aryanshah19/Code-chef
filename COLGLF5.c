#include<stdio.h>
void quicksort(long int arr[],int first,int last)
{
	long int i, j, pivot, temp;

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
    while(t--)
    {
        int N,M,f=0,c=0,channel=0;
        scanf("%d%d",&N,&M);
        long int F[N],C[M],s=0;
        long int mix[N+M],start=0;
        for(int i=0;i<N;i++)
        {
            scanf("%ld",&F[i]);
            mix[i]=F[i];
        }
        for(int i=0;i<M;i++)
        {
            scanf("%ld",&C[i]);
        }
        for(int i=N;i<N+M;i++)
            {
                mix[i]=C[start++];
            }
        quicksort(mix,0,M+N-1);
        for(int i=0;i<M+N;i++)
        {
            //for football
            if(mix[i]==F[0])
            {
                f++;
            }
            else if(mix[i]==F[f] && channel==1)
            {
                channel=0;
                f++;
                s++;
            }
            //for cricket
            if(mix[i]==C[c] && channel==0)
            {
                channel=1;
                c++;
                s++;
            }
        }
        printf("%ld\n",s);
    }
}