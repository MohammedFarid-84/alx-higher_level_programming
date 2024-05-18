#include "lists.h"

/**
 * check_cycle - check if a linked list has a cycle or not
 * @list: is a single list.
 *
 * Return: 1 if the list has a cycle and 0 if not.
 */
int check_cycle(listint_t *list)
{
	listint_t *d = list, *s = list, *f = list;

	while (d != NULL && s != NULL && f != NULL)
	{
		s = s->next;
		f = f->next->next;

		if (s == f)
			return (1);

		d = d->next;
	}
	return (0);
}
