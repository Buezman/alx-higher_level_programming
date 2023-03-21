#include "main.h"

/**
 * _isalpha - checks if a character is an alphabet
 * @c: ascii value of character
 * Return: 1 if true, else 0
 */

int _isalpha(int c)
{
	if ((c >= 65 && c <= 90) || (c >= 97 && c <= 122))
		return (1);
	return (0);
}
