/**
 *_memset - a function that copies a value
 *to a block of memory
 *Return: pointer destination array
 *@s: source array
 *@b: character to copy
 *@n: unsigned integer---number of bytes to set
 */
char *_memset(char *s, char b, unsigned int n)
{
	int i;

	for (i = 0; i < (int) n; i++)
		*(s + i) = b;

	return (s);
}
