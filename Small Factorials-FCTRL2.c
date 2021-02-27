#include<stdio.h>

int main()
{
    int t,n,a[200],k,l,m;
    scanf("%d",&t);
    while(t--)
    {
	    scanf("%d",&n);
        m=1;
        a[0]=1;
        for(int j=2;j<=n;j++)
        {
            l=0;
            for(k=0;k<m;k++)
            {
                a[k]=a[k]*j+l;//a[0]=2, a[0]=6, a[0]=24 , a[0]=20   ,a[1]=12        
                l=a[k]/10;//l=0,//l=2,//l=2,//l=1
                a[k]=a[k]%10;//a[0]=6;//a[0]=4,k=1,//a[0]=0//a[1]=2,k=2
            }
            while(l)
            {
	            a[k]=l%10;//a[1]=1
                k++;//k=2;
                m++;//m=2
                l=l/10;//l=0
            }
        }
        for(int i=m-1;i>=0;i--)
            printf("%d",a[i]);

        printf("\n");
    }
    return 0;
}