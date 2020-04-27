#include "lists.h"

/**
 * check_cycle - checks if linked list is a circle
 * @list: imports the linked list
 * Return: Returns 0 | 1
 */

int check_cycle(listint_t *list)
{
	listint_t *head = list; /* Saving a copy of where list begins */

	/* Increment head every single time list doesn't cycle back to head */
	for (; head != NULL; head = head->next)
	{
		for (list = head->next; list != NULL; list = list->next)
		{
			/* If list->next points to the current head */
			/* LOOP DETECTED!!! ABORT */
			if (list == head)
				return(1);
			;
		}
	}
	/* Managed to get to the end of the list */
	/* No Loops reported */
	return (0);
}
