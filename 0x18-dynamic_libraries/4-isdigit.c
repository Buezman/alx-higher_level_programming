#include "main.h"

/**
 * _isdigit - checks if a character is digit
 * @c: ascii value of character
 * Return: 1 if true, else 0
 */

int _isdigit(int c)
{
	if (c >= 0 && c <= 9)
		return (1);
	return (0);
}
