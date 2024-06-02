#include "main.h"

/**
 *_strncpy - string utility function
 *@dest: a parameter of type char *
 *@src: a parameter of type char *
 *@n: integer parameter
 *Return: pointer to the dest string
 */
char *_strncpy(char *dest, char *src, int n)
{
	int i;

	for (i = 0; (i < n) && (src[i] != '\0'); i++)
	{
		dest[i] = src[i];
	}
	while (i < n)
	{
		dest[i] = '\0';
		i++;
	}
	return (dest);
}

