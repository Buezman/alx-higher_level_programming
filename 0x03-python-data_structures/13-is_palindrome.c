#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: A pointer to the head of the linked list
 * Return: 1 if is_palindrome, else 0
 *
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *prev = NULL, *tmp;

	while (fast && fast->next)
	{
		fast = fast->next->next;
		tmp = slow->next;
		slow->next = prev;
		prev = slow;
		slow = tmp;
	}
	if (fast)
		slow = slow->next;

	while (slow)
	{
		if (slow->n != prev->n)
			return (0);
		slow = slow->next;
		prev = prev->next;
	}
	return (1);
}
