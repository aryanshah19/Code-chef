#include<stdio.h>
#include<stdlib.h>

int main()
{
	long long t;
	scanf("%lld",&t);
	while(t--)
	{
		long long r,c,x;
		scanf("%lld%lld%lld",&r,&c,&x);
		long long a[r][c], b[r][c];
		long long suma=0,sumb=0;
		for(long long i=0;i<r;i++)
		{
			for(long long j=0;j<c;j++)
			{
				scanf("%lld",&a[i][j]);
				suma+=a[i][j];
			}
		}
		for(long long i=0;i<r;i++)
		{
			for(long long j=0;j<c;j++)
			{
				scanf("%lld",&b[i][j]);
				sumb+=b[i][j];
			}
		}

		if(x==2 && 0)
		{
			long long pathsum=0;
			for(long long i=0;i<r;i++)
			{
				for(long long j=0;j<c;j++)
				{
					long long mul;
					if((r-i+c-j)%2==0)
						mul=-1;
					else 
						mul=1;
					if(!(i==r-1 && j==c-1)) 
						pathsum+=mul*(a[i][j]-b[i][j]);
				}
			}

			if(a[r-1][c-1]-pathsum==b[r-1][c-1])  
				printf("Yes\n");
			else 
				printf("No\n");
		}
		else
		{
			long long diffarr[r][c];
			for(long long i=0;i<r;i++)
			{
				for(long long j=0;j<c;j++)
				{
					diffarr[i][j]=b[i][j]-a[i][j];
				}
			}
			for(long long j=0;j<c;j++)
			{
				long long toadd=0;
				long long tempaddidx=r-x;
				while(tempaddidx>=0)
				{
					toadd += diffarr[tempaddidx][j];
					tempaddidx -= x;
				}
				for(long long i=r-1;i>r-x;i--)
				{
					long long temp=i-x;
					while(temp>=0)
					{
						diffarr[i][j] += diffarr[temp][j];
						temp=temp-x;
					}
					diffarr[i][j] -= toadd;
				}
			}
			for(long long i=r-1;i>r-x;i--)
			{
				long long toadd=0; //diff has to be added
				long long tempaddidx=c-x;
				while(tempaddidx>=0)
				{
					toadd += diffarr[i][tempaddidx];
					tempaddidx -= x;
				}
				for(long long j=c-1;j>c-x;j--)
				{
					long long temp=j-x;
					while(temp>=0)
					{
						diffarr[i][j] += diffarr[i][temp];
						temp=temp-x;
					}
					diffarr[i][j] -= toadd;
				}
			}
			int valid=1;
			for(long long i=r-1;i>r-x;i--)
			{
				for(long long j=c-1;j>c-x;j--)
				{
					if(diffarr[i][j]!=0) 
						valid=0;
				}
			}
			if(!valid)
				printf("No\n");
			else
				printf("Yes\n");
		}
	}
	return 0;
}
