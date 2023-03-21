#include "main.h"

/**
 * _strcpy - copies a string into another
 * @dest: pointer to destination for string copy
 * @src: pointer to string to be copied
 * Return: copied string
 *
 */

char *_strcpy(char *dest, char *src)
{
	int n = 0;

	while (src[n])
	{
		dest[n] = src[n];
		n++;
	}

	return (dest);
}
