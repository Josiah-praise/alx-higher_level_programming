#include "main.h"
/**
  *_puts - output function
  *@str: character pointer
  *Return: no return value
  */
void _puts(char *str)
{
	int i;

	for (i = 0; str[i] != '\0'; i++)
	{
		_putchar(str[i]);
	}
	_putchar('\n');
}
