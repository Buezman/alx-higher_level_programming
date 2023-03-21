#include "main.h"

/**
 * _strcmp - compares two strings
 * @s1: string1
 * @s2: string2
 * Return: 0 if equal, else another number
 *
 */

int _strcmp(char *s1, char *s2)
{
	int i = 0, d = 0;

	while ((s1[i] != '\0') && (s2[i] != '\0'))
	{
		d = s1[i] - s2[i];
		if (d != 0)
			return (d);
		i++;
	}

	return (d);
}
