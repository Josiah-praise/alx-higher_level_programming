#include <stdio.h>
/**
 *_strchr - a function that locates a character
 *in a string
 *@s: pointer to array
 *@c: character to be located
 *Return: pointer to the character
*/
char *_strchr(char *s, char c)
{
	while (*s >= 0)
	{
		if (*s == c)
			return (s);
		s++;
	}

	return (NULL);
}
