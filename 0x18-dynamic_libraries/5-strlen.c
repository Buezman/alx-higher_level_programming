#include "main.h"

/**
 * _strlen - gets the length of a string
 * @s: pointer to string
 * Return: length of string s
 */

int _strlen(char *s)
{
	int n = 0;

	while (s[n])
		n++;
	return (n);
}
