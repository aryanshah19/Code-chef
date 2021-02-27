#include <stdio.h>

int main(void) 
{
    int t;
    scanf("%d",&t);
    for(int i=0;i<t;i++)
        {
                int n,k;
                scanf("%d %d",&n,&k);
                long int array[k],i=0;
                for(i=0;i<k;++i)
                {
                scanf("%ld",&array[i]);
                 }
            char string1[n+1][k+1];
            i=0;
                for(i=0;i<n;++i)
                    {
            scanf("%s",string1[i]);
                }
            long long int marks[n];
            for(int j=0;j<n;++j)
                {
                        marks[j]=0;
                    for(int i=0;i<k;++i)
                        {
                        if(string1[j][i]=='0')
                        marks[j]+=0*array[i];
                        else
                        marks[j]+=1*array[i];
                    }
            }
            for(int i=0;i<n;++i)
                {
                printf("%lli\n",marks[i]);
            }
    }
return 0;
}

