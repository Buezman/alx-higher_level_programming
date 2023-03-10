#include "lists.h"
#include <stdlib.h>

/**
 * check_cycle - checks if a linked-list has a cycle
 * @list: linked-list
 * Return: 0 if cycle, else 1
 *
 */

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL || list->next == NULL)
		return (0);

	slow = list->next;
	fast = list->next->next;

	while (slow && fast && fast->next)
	{
		if (slow == fast)
			return (1);

		slow = slow->next;
		fast = fast->next->next;
	}

	return (0);
}
