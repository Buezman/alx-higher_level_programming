#include "main.h"

/**
 * _strncpy - copies the content of length of one string to another
 * @dest: destination string
 * @src: source string
 * @n: length of source to be copied
 * Return: copied string
 */

char *_strncpy(char *dest, char *src, int n)
{
	int i = 0;

	while ((i < n) && (*(src + i) != '\0'))
	{
		dest[i] = src[i];
		i++;
	}
	while (i < n)
	{
		dest[i] = '\0';
		i++;
	}

	return (dest);
}
