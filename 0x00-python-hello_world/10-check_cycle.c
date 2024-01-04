#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
  * check_cycle - checks for a cycle in a linked list
  *
  * @head: the first node in the list
  * Return: 0 if no cycle, 1 if cycle found
  */
int check_cycle(listint_t *head)
{
	listint_t *s, f*;
	int flag = 0;

	if (head == NULL)
		return (0);

	s = f = head;

	while (f)
	{
		flag++;
		f = f->next;
		if (flag % 2 == 0)
			s = s->next;
		if (f == s)
			return (1);
	}

	return (0);
}
