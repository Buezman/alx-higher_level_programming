#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly-linked-list
 * @head: pointer to the head of singly linked list
 * @number: number to insert
 * Return: new linked list with inserted number
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr = *head, *node;

	node = malloc(sizeof(listint_t));

	if (node == NULL)
		return (NULL);

	node->n = number;

	if (curr == NULL || curr->n >= number)
	{
		node->next = curr;
		*head = node;
		return (*head);
	}

	while (curr && curr->next && curr->next->n < number)
		curr = curr->next;

	node->next = curr->next;
	curr->next = node;

	return (node);
}
