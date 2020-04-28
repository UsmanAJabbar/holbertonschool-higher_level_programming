#include "lists.h"
/*
 * insert_node - inserts a new node sorted by
 * numeric weight
 * @head: address of head
 * @number: data to add to the new node
 * Return: NULL | newnode
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head; /* Keep a copy of where the list starts at */
	listint_t *new = malloc(sizeof(listint_t));
	listint_t *secondhalf; /* Keeps a copy of where the list was broken */

	if (*head == NULL || head == NULL)
		return (NULL);

	if (new == NULL)
	{
		free(new);
		return (NULL);
	}

	/* Go through the linked list up until the list has < number */
	for (; temp->next->n <= number; temp = temp->next)
	{
		;
	}
	secondhalf = temp->next; /* Keep a copy of the next list */

	/* Connect current temp->next to the new node */
	temp->next = new;

	/* Add data to the new node */
	new->n = number;
	new->next = secondhalf;

	return(new);
}
