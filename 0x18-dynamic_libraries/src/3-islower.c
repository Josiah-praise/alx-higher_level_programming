#include "main.h"
/**
 *_islower - check for lower characters
 *Description: return 1 for lowercase and 0 for uppercase
 *Return: 1 if lowercase else 0
 *@c: an integer
 */
int _islower(int c)
{
	if (c >= 'a' && c <= 'z')
	{
		return (1);
	}
	return (0);
}
