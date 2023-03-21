#include "main.h"

/**
 * _strcat - concatenate two strings
 * @dest: first string
 * @src: second string
 * Return: concatenation of string2 to string1
 */

char *_strcat(char *dest, char *src)
{
	int n = 0, i = 0;

	while (dest[n])
		n++;
	while (src[i++])
	{
		dest[n + i] = src[i];
	}

	return (dest);
}
