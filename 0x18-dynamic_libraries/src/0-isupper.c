#include "main.h"
/**
 *_isupper - isupper
 *Return: 1 if uppercase else, 0
 *@c: integer within range 0 - 225
 *Description: a function that checks for uppercase character.
 */
int _isupper(int c)
{
	if (c >= 'A' && c <= 'Z')
		return (1);
	else
		return (0);
}
