#include "lists.h"

/**
 * insert_node - insert a new node in a list, after sorted elements.
 * @head: a list to insert into.
 * @number: a value of a new node.
 *
 * Return: the address of new node or null.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *d = *head, *new_nod = malloc(sizeof(listint_t)), *old_nod = NULL;

	if (d == NULL || new_nod == NULL)
		return (NULL);

	while (d && d->next)
	{
		if (d->next->n - d->n != 1)
		{
			old_nod = d->next;
			new_nod->n = number;
			new_nod->next = old_nod;
			d->next = new_nod;
			return (new_nod);
		}
		else
		{
			d = d->next;
		}
	}
	return (new_nod);
}
