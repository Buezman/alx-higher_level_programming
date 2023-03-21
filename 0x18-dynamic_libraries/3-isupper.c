#include "main.h"

/**
 * _isupper - checks if a character is in uppercase
 * @c: ascii value of character
 * Return: 1 if true, else 0
 */

int _isupper(int c)
{
	if (c >= 65 && c <= 90)
		return (1);
	return (0);
}
