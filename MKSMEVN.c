#include<stdio.h>
#include <math.h>
int main()
{
    int t;
    scanf("%d",&t);
    for(int i=0;i<t;i++)
    {
        int n;
        scanf("%d",&n);
        int arr[n];
        int sum=0;
        for(int i=0;i<n;i++)
        {
            scanf("%d",&arr[i]);
            sum=sum+arr[i];
        }
        if(sum%2==0)
        {
            printf("0\n");
        }
        else 
            {
                int ans=0;
                for(int i=0;i<n;i++)
                {
                    if(arr[i]%2==0 && ((arr[i]+1)/2-1<=0))
                    {
                        ans=1;
                        break;
                    }
                }
                if(ans==0)
                    {
                        printf("-1\n");
                    }
                else
                    {
                        printf("1\n");
                    }
                
            }
        
    }
}
    