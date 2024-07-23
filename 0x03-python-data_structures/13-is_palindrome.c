#include "lists.h"

/**
 * is_palindrome - test if the duobly linked list
 * is a palindrome or not.
 * @head: a duobly linked list.
 * Return: 1 if has a palindrome and 0 if not.
 */
int is_palindrome(listint_t **head)
{
	listint_t *h = *head;
	int *my_arry;
	int s = 0, i = 0;

	/* count nodes in the list */
	while (h != NULL)
	{
		s++;
		h = h->next;
	}
	h = *head;

	/* intilize the array */
	my_arry = malloc(s * sizeof(int));

	/* save the list in the array */
	while (h != NULL)
	{
		my_arry[i] = h->n;
		h = h->next;
		i++;
	}
	h = *head;
	i = 0;
	/* commpare values in the array and free array */
	while (i < s / 2)
	{
		if (my_arry[i] != my_arry[s - 1 - i])
		{
			free(my_arry);
			return (0);
		}
		h = h->next;
		i++;
	}
	free(my_arry);
	return (1);
}
