#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

void merge(int list[], int left, int mid, int right, int *sortedList) {
	int current_array_index_val = left;
	int left_index = left;
	int mid_plus = mid + 1;

	while (left_index <= mid && mid_plus <= right) {
		if (list[left_index] <= list[mid_plus]) {
			sortedList[current_array_index_val++] = list[left_index++];
		}
		else {
			sortedList[current_array_index_val++] = list[mid_plus++];
		}
	}

	if (left_index > mid) {
		for (int l = mid_plus; l <= right; l++) {
			sortedList[current_array_index_val++] = list[l];
		}
	}
	else {
		for (int l = left_index; l <= mid; l++) {
			sortedList[current_array_index_val++] = list[l];
		}
	}

	for (int l = left; l <= right; l++) {
		list[l] = sortedList[l];
	}
}

void mergeSort(int list[], int left, int right, int sorted_list[]) {
	int mid;

	if (left < right) {
		mid = (left + right) / 2;
		mergeSort(list, left, mid, sorted_list);
		mergeSort(list, mid + 1, right, sorted_list);
		merge(list, left, mid, right, sorted_list);
	}
}

int solution(int k, int m, int score[], size_t score_len) {
    int answer = 0;
    int* sorted_score = (int*)malloc(sizeof(int) * score_len);
    
	mergeSort(score, 0, score_len - 1, sorted_score);
    int score_index = score_len - m;
    for (int i = 0; i < score_len / m; i++) {
        answer += sorted_score[score_index]*m;
        score_index -= m;
    }
    
    free(sorted_score);
    return answer;
}