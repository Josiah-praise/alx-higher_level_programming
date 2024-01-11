#include<stdio.h>
/**
 * _strpbrk - n locates the first occurrence in the string s
 * s of any of the bytes in the string accept
 *@s: character array
 *@accept: character array
 *Return:  pointer to the byte in s that matches
 *one of the bytes in accept or NULL if no such byte is found
*/
char *_strpbrk(char *s, char *accept)
{
	int i;

	if (s == NULL || accept == NULL)
	return (NULL);

	while (*s)
	{
		i = 0;
		while (*(accept + i))
		{
			if (*s == *(accept + i))
			{
				return (s);
			}
			i++;
		}
		s++;
	}
	return (NULL);
}
