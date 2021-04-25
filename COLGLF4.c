#include <stdio.h>

int main() 
{
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;i++)
	{
		long N,E,H,A,B,C;
		scanf("%ld%ld%ld%ld%ld%ld",&N,&E,&H,&A,&B,&C);
		//Maximum number of items that can be made
		long omm=0,milksh=0,cake=0;
		long items=0;
		int n=1;
		long int omm1=0,milksh1=0,cake1=0;
		long int omm2=0,milksh2=0,cake2=0;
		long int omm3=0,milksh3=0,cake3=0;
		long int items1=0,items2=0,items3=0;

		//order ommlette,milkshake,cake
		if(n==1)
		{
			long items1=0;
			if(E%2==0)
			{
				items1=E/2;
				omm1=items1;
			}
			else 
			{
				items1=E/2;
				omm1=items1;
				if(H>=1)
				{
					items1++;
					cake1++;
				}
			}
			if(items1>items)
				{
					items=items1;
				}
			n=2;
		}
		
		//order milkshake,ommlette,cake
		if(n==2)
		{
			long items2=0;
			if(H%3==0)
				{
					items2=H/3;
					milksh2=items2;
				}
			else 
				{
					items2=H/3;
					milksh2=items2;
					int choc_left=H%3;
					int eggs=E;
					if(choc_left==2 && eggs>=2)
					{
						items2=items2+2;
						cake2++;
						cake2++;
					}
					if(choc_left==2 && eggs==1)
					{
							items2=items2+1;
							cake2++;
					}
					if(choc_left==1 && eggs>=1)
					{
						items2=items2+1;
						cake2++;
					}
				}
			if(items2>items)
				{
					items=items2;
				}
			n=3;
		}
		
		if(n==3)
			{
				int eggs_left=E,milksh_left=H;
				if(eggs_left==milksh_left)
				{
					items3=eggs_left;
					cake3=items3;
				}
				else if(eggs_left>milksh_left)
				{
					items3=milksh_left;
					cake3=items3;
					eggs_left=eggs_left-milksh_left;
					omm3=eggs_left/2;
					items3=items3+omm3;
				}
				else if(eggs_left<milksh_left)
					{
						items3=eggs_left;
						cake3=items3;
						milksh_left=milksh_left-eggs_left;
						milksh3=milksh_left/3;
						items3=items3+milksh3;
					}
				if(items3>items)
					{
						items=items3;
					}
			}
		
		printf("%ld\n",items);
		/*printf("%ld\n",omm1);
		printf("%ld\n",milksh1);
		printf("%ld\n",cake1);
		printf("%ld\n",omm2);
		printf("%ld\n",milksh2);
		printf("%ld\n",cake2);
		printf("%ld\n",omm3);
		printf("%ld\n",milksh3);
		printf("%ld\n",cake3);*/
		/*if(items1>=items2 && items1>=items3)
		{
			omm=omm1;
			milksh=milksh1;
			cake=cake1;
		}
		if(items2>=items1 && items2>=items3)
			{
				omm=omm2;
				milksh=milksh2;
				cake=cake2;
			}
		if(items3>=items2 && items3>=items1)
			{
				omm=omm3;
				milksh=milksh3;
				cake=cake3;
			}*/
		if(items<N)
		{
			printf("-1\n");
		}
		else 
		{
				long cost;
				if(A<B && A<C)
				{
					int count=N;
					omm=omm1;
					milksh=milksh1;
					cake=cake1;
					if(count>omm)
						{
							cost=A*omm;
							count=count-omm1;
							if(B<C && count!=0)
								{
									if(count>milksh)
										{
											cost=cost+(B*milksh);
											N=N-milksh1;
										}
									else 
									{
										cost=B*count;
									}
								}
						}
					else 
						{
						cost=A*count;
					}
							
					
				}
			
		
		}
		
		
	}
}