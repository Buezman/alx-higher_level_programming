#include "main.h"

/**
 * _islower - checks if a character is lowercase
 * @c: ascii value of character
 * Return: 1 if true, else 0
 */

int _islower(int c)
{
	if (c >= 97 && c <= 122)
		return (1);
	return (0);
}
