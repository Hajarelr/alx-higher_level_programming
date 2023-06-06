#include "lists.h"

/**
 * check_cycle - Function that checks if a singly linked list has a cycle
 * @list: Pointer
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
listint_t *a, *b;
if (list == NULL || list->next == NULL)
return (0);
a = list;
b = a->next;
while (a != NULL && b->next != NULL && b->next->next != NULL)
{
if (a == b)
return (1);
a = a->next;
b = b->next->next;
}
return (0);
}
