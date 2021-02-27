#include <stdio.h>
int main()
{
int n;
scanf("%d",&n);
for(int i=0;i<n;i++)    
   {
            long int n, string=0, rem;
            scanf("%ld", &n);
            while(n!=0)
                  {
                     rem=n%10;
                     string=string*10+rem;
                     n=n/10;
                  }
            printf("%ld\n",string);
    }
return 0;
}