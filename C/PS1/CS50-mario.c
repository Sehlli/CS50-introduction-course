#include<stdio.h>
#include<String.h>
int verif(int n)
{
	char y;
	y='n';
	if (isdigit(y))
		{
				printf("yes\n");
			return(1);
		
		}
}
int main (void)
{
	int n,i,j,k;
		do 
		{	
			printf("hight : ");
			scanf("%d",&n);
		} while (n<=0 || n>8  );
		
		for ( i=0; i<=n ; ++i)
		{
			for ( j=0; j<i ; ++j)
				{
					printf("#");
				}
			printf("\n");
			for ( k=0; k<n-i ; ++k)
			 			printf(" ");	
		}


}
