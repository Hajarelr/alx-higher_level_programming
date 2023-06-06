#include "lists.h"
/**
 * insert_node - Function that inserts a number into a sorted sgly lnkd list
 * @head: 1st input
 * @number:2nd input
 * Return: pointer to the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
        listint_t *runner;
        listint_t *new;

        runner = *head;

        new = malloc(sizeof(listint_t));
        if (new == NULL)
                return (NULL);
        new->n = number;

        if (*head == NULL || (*head)->n > number)
        {
                new->next = *head;
                *head = new;
                return (new);
        }

        while (runner->next != NULL)
        {
                if ((runner->next)->n >= number)
                {
                        new->next = runner->next;
                        runner->next = new;
                        return (new);
                }
                runner = runner->next;
        }

        new->next = NULL;
        runner->next = new;
        return (new);
}
