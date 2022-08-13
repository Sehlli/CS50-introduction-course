#include<stdio.h>
#include <ctype.h>
#include<string.h>
#include<stdlib.h>

int test (char ch[])
{	int v;
	for(int i = 0; i< strlen(ch);i++ )
	
	{
		if (!isdigit(ch[i]))
			{	
				printf("enter valid KEY");
				 v =  1;
				return 1;
			}
		else 
			 v=0;
		
	}return v;
}

int main ()
{
	
	// get key
	char ch[20];
	do {
			printf("KEY :");
			scanf("%s",ch);
	}	while(test(ch));
	int k=atoi(ch);
	
		
	// get plein text
	char pleintext[50];
	char ciphertext[50];
	printf("enter text :");
	scanf("%s",pleintext);
	
	// Encipher and print
	
		for(int i =0; i< strlen(pleintext);i++ )
		{
			if (isupper(pleintext[i]))
				ciphertext[i]=( pleintext[i]-65 + k) % 26 + 65;
			else if(islower(pleintext[i])) 
				ciphertext[i]=( pleintext[i]-97 + k) % 26 + 97;
			else
				ciphertext[i]=pleintext[i];
			}
		
	printf("%s",ciphertext);
	
	
return 0;
}
