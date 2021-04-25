#include<stdio.h>
void reverseArray(int arr[], int start, int end)
{
    int temp;
    while (start < end)
        {
            temp = arr[start];  
            arr[start] = arr[end];
            arr[end] = temp;
            start++;
            end--;
        }  
}    
int main()
{
    int t,n;
    scanf("%d",&t);
    for(int i=0;i<t;i++)
    {
        scanf("%d",&n);
        int arr[n],result=0;
        for(int i=0;i<n;i++)
        {
            scanf("%d",&arr[i]);
        }
        for(int j=0;j<n-1;j++)
            {
                int min=128,index=-1;
                for(int k=j;k<n;k++)
                {
                    if(arr[k]<min)
                    {
                        min=arr[k];
                        index=k;
                    }
                }
                int first=*arr+j;
                int last=*arr+index+1;
                reverseArray(arr, first, last);
                result=result+(index-j)+1;
            }
        printf("Case #%d: %d\n",i+1,result);
    }
}