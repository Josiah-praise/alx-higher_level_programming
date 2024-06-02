#include <stdio.h>
int is_present(char *, char);
/**
 * _strspn - Returns the number of bytes in the initial
 * segment of s which consist only of bytes
 * @s: pointer to array
 * @accept: pointer to array
 * Return: unsigned integer
*/
unsigned int _strspn(char *s, char *accept)
{
	size_t count = 0, con;
	int i;

	while (*s) /*traverse s*/
	{
		for (i = 0, con = 0; *(accept + i);  i++)
		{
			if (*s == *(accept + i))
			{
				count++;
				con = 1;
				break;
			}
		}
		if (!con)
			return (count);
		s++;
	}
	return (count);
}

/**
 * is_present - checks if that character is in the buffer
 * @buffer: pointer to buffer
 * @c: charater
 * Return: 1 (present) /0 (not present)
*/
int is_present(char *buffer, char c)
{
	while (*buffer)
	{
		if ((*buffer) == c)
			return (1);
		buffer++;
	}
	return (0);
}
