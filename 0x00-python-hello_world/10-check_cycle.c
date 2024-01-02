#include "lists.h"

/**
 * check_cycle - checks for a loop in a linked list
 * @list: head of the linked list
 * Return: 0(no cycle) or 1(cycle)
 */
int check_cycle(listint_t *list)
{
	listint_t *slow;
	listint_t *fast;

	/*check for NULL pointers*/
	if (list == NULL)
		return (0);

	slow = list;
	fast = list;

	/*let fast move 2 nodes faster than slow*/
	/*using floyd's cycle detection algorithm*/
	while (fast->next != NULL && fast->next->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}
	return (0);
}
