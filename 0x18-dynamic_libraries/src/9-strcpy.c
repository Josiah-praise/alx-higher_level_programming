#include "main.h"

/**
 *_strcpy - output function
 *@dest: character pointer parameter
 *@src: character pointer parameter
 *Return: pointer
 */
char *_strcpy(char *dest, char *src)
{
	int len, i;

	len = _strlen(src);

	for (i = 0; i < len; i++)
		*(dest + i) = src[i];
	*(dest + len) = '\0';
	return (dest);
}
