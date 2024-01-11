/**
 *_strcmp - utility function
 *@s1: character pointer
 *@s2: character pointer
 *Return: integer
 */
int _strcmp(char *s1, char *s2)
{
	int i;

	i = 0;

	while (s1[i] != '\0' && s2[i] != '\0')
	{
		if (s1[i] == s2[i])
		{
			i++;
			continue;
		}
		else
		{
			return (s1[i] - s2[i]);
		}
		i++;
	}
	return (0);
}
