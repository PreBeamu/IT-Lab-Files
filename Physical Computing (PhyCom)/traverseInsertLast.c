#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// DataNode structure using typedef
typedef struct DataNode {
	char* data;
	struct DataNode* next;
} DataNode;

// SinglyLinkedList structure using typedef
typedef struct SinglyLinkedList {
	unsigned int count;
	DataNode* head;
} SinglyLinkedList;

// Function prototypes
DataNode *createDataNode(char *data);
SinglyLinkedList *createSinglyLinkedList();
void traverse(SinglyLinkedList *list);
void insert_last(SinglyLinkedList *list, char *data);

int main() {
	SinglyLinkedList* mylist = createSinglyLinkedList();
	int n;
	char condition;
	char data[101];
	scanf("%d", &n);

	for (int i = 0; i < n; i++) {
		scanf(" %c: %[^\n]s", &condition, data);

		if (condition == 'F') {
			;
		} else if (condition == 'L') {
			insert_last(mylist, data);
		} else if (condition == 'D') {
			;
		} else {
			printf("Invalid Condition!\n");
		}
	}

	traverse(mylist);

	// Remember to free allocated memory for each node's data
	DataNode *current = mylist->head;
	while (current != NULL) {
		free(current->data);
		DataNode* temp = current;
		current = current->next;
		free(temp);
	}
	free(mylist);
	return 0;
}

DataNode* createDataNode(char* data) {
	DataNode* node = (DataNode*)malloc(sizeof(DataNode));
	node->data = (char*)malloc(strlen(data) + 1);
	strcpy(node->data, data);
	node->next = NULL;

	return node;
}

// Create a new SinglyLinkedList
SinglyLinkedList* createSinglyLinkedList() {
	SinglyLinkedList* list = (SinglyLinkedList*)malloc(sizeof(SinglyLinkedList));
	list->count = 0;
	list->head = NULL;

	return list;
}

// Traverse the list and print data
void traverse(SinglyLinkedList* list) {
	if (list->count == 0) {
		printf("This is an empty list.\n");
		return;
	}
	struct DataNode* pointer = list->head;
	while (pointer->next != NULL) {
		printf("%s -> ", pointer->data);
		pointer = pointer->next;
	}
	printf("%s\n", pointer->data);
}

// Insert a new node at the end of the list
void insert_last(SinglyLinkedList* list, char* data) {
	struct DataNode* pNew = createDataNode(data);
	if (list->count == 0) {
		list->head = pNew;
	} else {
		struct DataNode* pointer = list->head;
		while (pointer->next != NULL) {
			pointer = pointer->next;
		}
		pointer->next = pNew;
	}
	list->count++;
}