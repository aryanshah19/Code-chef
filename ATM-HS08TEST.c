#include<stdio.h>
#include<math.h>
int main()
{
int debit;
float balance;
scanf("%d%f",&debit,&balance);
		
			if(debit+0.5>balance)
			{
				printf("%0.2f",balance);
			}
			else
				{
					if(debit%5!=0)
						{
							printf("%0.2f",balance);
						}
					else
					{
						printf("%0.2f",balance-debit-0.5);
					}
				}
}