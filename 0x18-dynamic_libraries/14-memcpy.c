#include "main.h"
/**
 * *_memcpy - copy memory area
 * @src: source memory area
 * @dest: destination memory area
 * Return: copied memory area
 */
char *_memcpy(char *dest, char *src, unsigned int n)
{
	unsigned int i;

	for (i = 0; i < n; i++)
		*(dest + 1) = *(src + 1);

	return (dest);
}
