#include<stdio.h>
#define MAX 100
int main()
{
    int t;
    scanf("%d",&t);
    while(t!=0)
    {
        int n,x,i=0,arr[MAX],flag=0;
        scanf("%d",&n);
        while(n%10==0)
            {
                n=n/10;
            } 
        while(n!=0)
        {
            x=n%10;
            n=n/10;
            arr[i]=x;
            i++;
        }
        for(int j=0;j<i;j++)
        {
             printf("%d",arr[j]);
        }
        printf("\n");
        t--;
    }
}