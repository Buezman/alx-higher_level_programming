#include "main.h"

/**
 * _strncat - concatenate n length of a string to another
 * @dest: destination string
 * @src: source string
 * @n: length of soure=ce to be conactenated
 * Return: concatenated string
 */

char *_strncat(char *dest, char *src, int n)
{
	int i;

	for (i = 0; i < n; i++)
		*(dest + i) = *(src + i);
	return (dest);
}
