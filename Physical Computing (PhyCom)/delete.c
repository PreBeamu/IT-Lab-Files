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
void insert_front(SinglyLinkedList* list, char* data);
void delete(SinglyLinkedList* list, char* data);

int main() {
    SinglyLinkedList* mylist = createSinglyLinkedList();
    int n;
    char condition;
    char data[100]; // Assuming a maximum string length of 99 characters
    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        scanf(" %c: %[^\n]s", &condition, data); // Read condition and string data

        if (condition == 'F') {
            insert_front(mylist, data);
        } else if (condition == 'L') {
            insert_last(mylist, data);
        } else if (condition == 'D') {
            delete(mylist, data);
        } else {
            printf("Invalid Condition!\n");
        }
    }

    traverse(mylist);
    // Remember to free allocated memory for each node's data
    DataNode* current = mylist->head;
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

void insert_front(SinglyLinkedList* list, char* data) {
    struct DataNode* pNew = createDataNode(data);
	if (list->count == 0) {
		list->head = pNew;
	} else {
		struct DataNode* old_pointer = list->head;
		list->head = pNew;
		pNew->next = old_pointer;
	}
	list->count++;
}

void delete(struct SinglyLinkedList* list, char* data) {
    struct DataNode* current = list->head;
    struct DataNode* previous = NULL;

    if (current == NULL) {
        printf("Cannot delete, %s does not exist.\n", data);
        return;
    }

    while (current != NULL) {
        if (strcmp(current->data, data) == 0) {
            if (previous == NULL) {
                list->head = current->next;
            } else {
                previous->next = current->next;
            }
            
            free(current->data);
            free(current);
            list->count--;
            return;
        }
        previous = current;
		current = current->next;
	}
	printf("Cannot delete, %s does not exist.\n", data);
}