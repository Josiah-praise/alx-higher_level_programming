/**
 * _memcpy - copy a block of memory to another block
 * @dest: destination array
 * @src: source array
 * @n: unsigned int
 * Return: pointer to destination array
*/
char *_memcpy(char *dest, char *src, unsigned int n)
{
	for (; n; n--)
	{
		dest[n - 1] = src[n - 1];
	}
	return (dest);
}
