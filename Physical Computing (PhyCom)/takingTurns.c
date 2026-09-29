#include <stdio.h>
#include <stdlib.h>

typedef struct DataNode {
    int data;
    struct DataNode* next;
} DataNode;

typedef struct SinglyLinkedList {
    unsigned int count;
    DataNode* head;
} SinglyLinkedList;

DataNode* createDataNode(int data) {
    DataNode* node = (DataNode*)malloc(sizeof(DataNode));
    node->data = data;
    node->next = NULL;
    return node;
}

SinglyLinkedList* createSinglyLinkedList() {
    SinglyLinkedList* list = (SinglyLinkedList*)malloc(sizeof(SinglyLinkedList));
    list->count = 0;
    list->head = NULL;
    return list;
}

void traverse(SinglyLinkedList* list) {
    if (list->count == 0) {
        printf("This is an empty list.\n");
        return;
    }
    DataNode* pointer = list->head;
    while (pointer->next != NULL) {
        printf("%d -> ", pointer->data);
        pointer = pointer->next;
    }
    printf("%d\n", pointer->data);
}

void insert_last(SinglyLinkedList* list, int data) {
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

DataNode* get_node_at(SinglyLinkedList* list, int index) {
    DataNode* curr = list->head;
    while (index > 0 && curr != NULL) {
        curr = curr->next;
        index--;
    }
    return curr;
}

SinglyLinkedList* rearrange_list(SinglyLinkedList* original) {
    SinglyLinkedList* new_list = createSinglyLinkedList();
    int n = original->count;
    if (n == 0) return new_list;

    int left = 0;
    int right = n - 1;
    int is_first = 1;
    int turn = 0;

    while (left <= right) {
        int take_count = is_first ? 1 : 2;
        is_first = 0;

        if (turn == 0) {
            int taken = 0;
            while (right >= left && taken < take_count) {
                DataNode* target = get_node_at(original, right);
                insert_last(new_list, target->data);
                right--;
                taken++;
            }
            turn = 1;
        } else {
            int taken = 0;
            while (left <= right && taken < take_count) {
                DataNode* target = get_node_at(original, left);
                insert_last(new_list, target->data);
                left++;
                taken++;
            }
            turn = 0;
        }
    }

    return new_list;
}

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;

    SinglyLinkedList* original_list = createSinglyLinkedList();
    int val;
    for (int i = 0; i < n; i++) {
        scanf("%d", &val);
        insert_last(original_list, val);
    }

    SinglyLinkedList* result_list = rearrange_list(original_list);

    traverse(result_list);

    DataNode* current = original_list->head;
    while (current != NULL) {
        DataNode* temp = current;
        current = current->next;
        free(temp);
    }
    free(original_list);

    current = result_list->head;
    while (current != NULL) {
        DataNode* temp = current;
        current = current->next;
        free(temp);
    }
    free(result_list);

    return 0;
}