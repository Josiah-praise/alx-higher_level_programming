/**
  *_strlen - helper function
  *@s: character pointer;
  *Return: lenght of the string
  */
int _strlen(char *s)
{
	int size;

	for (size = 0; s[size] != '\0'; size++)
		continue;
	return (size);
}
