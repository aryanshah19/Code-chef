#include<stdio.h>
int main()
{
    int t;
    scanf("%d",&t);
    while(t--)
    {
        long int n,x;
        long long int max=0;
        scanf("%ld %ld",&n,&x);
        while(n--)
        {
            long long int s,r;
            scanf("%lld %lld",&s,&r);
            if(s<=x)
            {
                if(max<r)
                {
                    max=r;
                }
            }
        }
        printf("%lld\n",max);
    }
}