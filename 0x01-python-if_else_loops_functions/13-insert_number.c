#include "lists.h"

/**
 * insert_node - insert a node into a sorted linked list
 * @head: double pointer to node
 * @number: number to be inserted
 * Return: pointer to new node or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *previous = NULL;
	listint_t *current = *head;
	listint_t *new_node = NULL;

	/*check if list is empty*/
	if (head == NULL )
		return (NULL);

	/*malloc space for new node*/
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;
	if (*head == NULL)
		*head = new_node;
    if (current->n > number)
    {
		new_node->next = current;
		*head = new_node;
		return (*head);
    }
	previous = current;	/*move up one node*/
	current = current->next;
	/*number is neither the smallest nor the largest*/
	while (current)
	{
		if (current->n > number)
		{
			previous->next = new_node;
			new_node->next = current;
			return (new_node);
		}
		previous = current;
		current = current->next;
	}
	/*update last node if number is the largest*/
	previous->next = new_node;
	return (new_node);
}
