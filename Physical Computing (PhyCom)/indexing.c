#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct DataNode {
    char* data;
    struct DataNode* next;
} DataNode;

typedef struct SinglyLinkedList {
    unsigned int count;
    DataNode* head;
} SinglyLinkedList;

DataNode* createDataNode(char* data) {
    DataNode* node = (DataNode*)malloc(sizeof(DataNode));
    node->data = (char*)malloc(strlen(data) + 1);
    strcpy(node->data, data);
    node->next = NULL;
    return node;
}

SinglyLinkedList* createSinglyLinkedList() {
    SinglyLinkedList* list = (SinglyLinkedList*)malloc(sizeof(SinglyLinkedList));
    list->count = 0;
    list->head = NULL;
    return list;
}

void insert_last(SinglyLinkedList* list, char* data) {
    DataNode* pNew = createDataNode(data);
    if (list->count == 0) {
        list->head = pNew;
    } else {
        DataNode* pointer = list->head;
        while (pointer->next != NULL) {
            pointer = pointer->next;
        }
        pointer->next = pNew;
    }
    list->count++;
}

void get_at_index(SinglyLinkedList* list, int index) {
    int target_index;

    if (index < 0) {
        target_index = (int)list->count + index;
    } else {
        target_index = index;
    }

    if (target_index < 0 || target_index >= (int)list->count) {
        printf("Error\n");
        return;
    }

    DataNode* current = list->head;
    for (int i = 0; i < target_index; i++) {
        current = current->next;
    }

    printf("%s\n", current->data);
}

int main() {
    SinglyLinkedList* mylist = createSinglyLinkedList();
    char* menu = (char*)malloc(sizeof(char) * 25);

    while (scanf("%s", menu) == 1) {
        if (strcmp(menu, "Last") == 0) {
            break;
        }
        insert_last(mylist, menu);
    }

    int target_idx;
    if (scanf("%d", &target_idx) == 1) {
        get_at_index(mylist, target_idx);
    }
    
    free(menu);

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