#include "lists.h"

int aux_palindrome(listint_t **head, listint_t *end);
/**
 * is_palindrome -  recursive palindrome or not
 * @head: head list
 * Return: 0 if it is not a palindrome
 * 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (aux_palindrome(head, *head));
}

/**
 * aux_palindrome - funct to know if is palindrome
 * @head: head list
 * @end: end list
 * Return: 1 or 0
 */
int aux_palindrome(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (aux_palind(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}

