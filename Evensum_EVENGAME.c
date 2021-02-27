#include<stdio.h>
int main()
{
    int n;
    scanf("%d",&n);
    for(int i=0;i<n;i++)
    {
        int length;
        scanf("%d",&length);
        int arr[length];
        int sum=0;
        for(int i=0;i<length;i++)
            scanf("%d",&arr[i]);
        for(int i=0;i<length;i++)
            sum=sum+arr[i];
        if(sum%2==0)
            printf("1\n");
        else
            printf("2\n");
    }
}
