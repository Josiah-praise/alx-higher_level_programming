#include <stdio.h>
/**
 * len - get string length
 * @str: character pointer
 * Return: integer
 */
int len(char *str)
{
	int i;

	for (i = 0; *str; i++, str++)
		continue;
	return (i);
}



/**
 * _strstr -  finds the first occurrence of the substring needle in the
 *string haystack. The terminating null bytes (\0) are not compared
 *@haystack: character pointer
 *@needle: character pointer
 *Return: pointer to first occurence
 */
char *_strstr(char *haystack, char *needle)
{
	int i, count;

	if (*needle == 0)
		return (haystack);
	while (*haystack)
	{
		if (*haystack == *needle)
		{
			for (i = 0, count = 0; i < len(needle); i++)
			{
				if (*(haystack + i) == needle[i])
					count++;
				else
					break;
			}
			if (count == len(needle))
				return (haystack);
		}
		haystack++;
	}
	return (NULL);
}
