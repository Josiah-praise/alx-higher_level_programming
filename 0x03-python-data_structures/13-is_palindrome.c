#include "lists.h"
/**
 * reverse - reverses a linked list
 * @head: pointer to head
 * Return: pointer to head
 */
listint_t *reverse(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (NULL);

	listint_t *current, *previous, *next;

	current = *head;
	previous = NULL;

	while (current)
	{
		next = current->next;
		current->next = previous;
		previous = current;
		current = next;
	}
	*head = previous;
	return (*head);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head
 * Return: 1 if it's a palindrome and 0 if it isn't
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (0);

	listint_t *fast, *slow;

	slow = *head;
	fast = *head;
	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	if (fast)
		slow = slow->next;

	slow = reverse(&slow);

	fast = *head;
	while (slow)
	{
		if (slow->n != fast->n)
			return (0);
		slow = slow->next;
		fast = fast->next;
	}
	return (1);
}
