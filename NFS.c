#include<stdio.h>
#include <math.h>
int main()
{
    int t;
    scanf("%d",&t);
    for(int i=0;i<t;i++)
    {
        int u,v,a,s;
        scanf("%d%d%d%d",&u,&v,&a,&s);
        if(u<=v)
        {
            printf("Yes\n");
        }
        else 
            {
                if((u*u-v*v)<=(2*a*s))                   
                {
                    printf("Yes\n");
                }
                else
                {
                    printf("No\n");
                }
            }
    }
}
