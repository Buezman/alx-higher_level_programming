#include "main.h"
/**
 * *_strbrk - searches for first common character in two strings
 * @s: string 1
 * @accept: string 2
 * Return: first char common in s and accept
 */
char *_strpbrk(char *s, char *accept)
{
	unsigned int i, j;

	for (i = 0; *(s + i) != '\0'; i++)
	{
		for (j = 0; *(accept + j) != '\0'; j++)
		{
			if (s[i] == accept[j])
				return (s + i);
		}
	}
	return ('\0');
}
