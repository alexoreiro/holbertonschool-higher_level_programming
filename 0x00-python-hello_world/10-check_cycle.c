#include "lists.h"

/**
 * check_cycle - check if there is a a cycle in a singly linked list
 * @list - linked list
 * Return: 0 if there is no cycle; 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
listint_t *fast, *slow;

fast = slow = list;
while (fast != NULL && fast->next != NULL)
{
slow = slow->next;
fast = fast->next->next;
if (slow == fast)
return (1);
}
return (0);
}
