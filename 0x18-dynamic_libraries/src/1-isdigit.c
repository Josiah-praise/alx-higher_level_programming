/**
 *_isdigit -  a function that checks for a digit (0 through 9).
 *Description:  a function that checks for a digit (0 through 9).
 *Return: 1 if c is a digit elso 0
 *@c: integer ranging from 0-225
 */
int _isdigit(int c)
{
	if (c >= 48 && c <= 57)
		return (1);
	else
		return (0);
}
