#include "main.h"

/**
 * _abs - return the absolute value of an integer
 * @n: integer
 * Return: absolute  value of n
 */
int _abs(int n)
{
	if (n < 0)
		n *= -1;
	return (n);
}
