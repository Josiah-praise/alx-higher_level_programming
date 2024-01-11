#include "main.h"

/**
 *_isalpha - alphabet checker
 *@c: integer
 *Description: Checks for alphabetic character
 *Return: 1 if alphabet else false
 */
int _isalpha(int c)
{
	if ((c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z'))
		return (1);
	return (0);
}
