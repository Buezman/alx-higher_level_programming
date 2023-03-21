#include "main.h"

/**
 * _atoi - converts a string to an integer
 * @s: pointer to string
 * Return: integer equivalent of string
 */

int _atoi(char *s)
{
	int n = 0, i = 0;

	while (s[i++])
	{
		n += (s[i] + '0');
	}

	return (n);
}
