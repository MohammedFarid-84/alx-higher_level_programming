#include "lists.h"

/**
 * revers_list - revers singl list.
 * @head: a linked list.
 * Return: a revers linked list.
 */
listint_t *revers_list(listint_t *head)
{
	listint_t *current = head;
	listint_t *next = NULL;
	listint_t *prev = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return (prev);
}


/**
 * is_palindrome - test if the duobly linked list
 * is a palindrome or not.
 * @head: a duobly linked list.
 * Return: 1 if has a palindrome and 0 if not.
 */
int is_palindrome(listint_t **head)
{
	listint_t *h = *head;
	listint_t *front = NULL;
	listint_t *rev_list = NULL;

	/* save old list in new list */
	while (h != NULL)
	{
		add_nodeint_end(&front, h->n);
		h = h->next;
	}
	h = *head;

	/* reverse the old list */
	rev_list = revers_list(h);

	/* commpare the list from to sides */
	while (front != NULL && rev_list != NULL)
	{
		if (front->n != rev_list->n)
		{
			return (0);
		}
		front = front->next;
		rev_list = rev_list->next;
	}
	return (1);
}
