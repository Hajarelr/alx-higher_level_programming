#include "lists.h"
/**
 * reverse_listint - Function that reverses a linked list
 * @head: 1st input
 * Return: Void
 */
void reverse_listint(listint_t **head)
{
  listint_t *prev = NULL;
  listint_t *current = *head;
  listint_t *next = NULL;

  while (current)
    {
      next = current->next;
      current->next = prev;
      prev = current;
      current = next;
    }

  *head = prev;
}

/**
 * is_palindrome - Function that checks if a linked list is a palindrome
 * @head: 1st input
 * Return: 1 if it's a palindrome or 0 if not
 */
int is_palindrome(listint_t **head)
{
  listint_t *s = *head, *f = *head, *t = *head, *d = NULL;

  if (*head == NULL || (*head)->next == NULL)
    return (1);

  while (1)
    {
      f = f->next->next;
      if (!f)
	{
	  d = s->next;
	  break;
	}
      if (!f->next)
	{
	  d = s->next->next;
	  break;
	}
      s = s->next;
    }

  reverse_listint(&d);

  while (d && t)
    {
      if (t->n == d->n)
	{
	  d = d->next;
	  t = t->next;
	}
      else
	return (0);
    }

  if (!d)
    return (1);

  return (0);
}
