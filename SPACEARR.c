#include <stdio.h>
void quicksort(int number[10000],int first,int last)
{
    int i, j, pivot, temp;
    
    if(first<last){
        pivot=first;
        i=first;
        j=last;
        
        while(i<j){
            while(number[i]<=number[pivot]&&i<last)
                i++;
            while(number[j]>number[pivot])
                j--;
            if(i<j){
                temp=number[i];
                number[i]=number[j];
                number[j]=temp;
            }
        }
        
        temp=number[pivot];
        number[pivot]=number[j];
        number[j]=temp;
        quicksort(number,first,j-1);
        quicksort(number,j+1,last);
        
    }
}int main()
{
    int test;
    scanf("%d",&test);
    while(test--)
    {
        int n;
        scanf("%d",&n);
        int arr[n],counter=0,flag=0,temp=0;
        for(int i=0;i<n;i++)
        {
           scanf("%d",&arr[i]);
        }
        quicksort(arr, 0, n);
        for(int i=0;i<n;i++)
            {
                printf("%d",arr[i]);
            }

        
        for(int i=0;i<n;i++)
        {
            if(arr[i]>i+1)
            {
                printf("Second\n");
                flag=1;
                break;
            }
            else
            {
                counter += i+1-arr[i];
            }
        }
        if(flag==0)
        {
            if(counter&1)
            {
                printf("First\n");
            }
            else
            {
                printf("Second\n");
            }
        }
    }
    return 0;
}