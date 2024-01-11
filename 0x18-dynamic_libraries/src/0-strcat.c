/**
 *size - utility function
 *@str: a parameter of type char *
 *Return: the size of the string
 */
int size(char *str)
{
	int i;

	for (i = 0; *(str + i) != '\0'; i++)
		continue;
	return (i + 1);
}


/**
 *_strcat - string utility function
 *@dest: a parameter of type char *
 *@src: a parameter of type char *
 *Return: pointer to the dest string
 */
char *_strcat(char *dest, char *src)
{
	int i, size_src =  size(src), strlen_dest = size(dest) - 1;

	/**
	 *this makes the assumption that the dest is large enough
	 *to accomodate the source
	 */
	for (i = 0; i < size_src; i++)
		dest[strlen_dest + i] = src[i];
	return (dest);
}

