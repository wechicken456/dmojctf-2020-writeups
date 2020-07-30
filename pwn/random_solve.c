#include <time.h>
#include <stdlib.h>
#include <stdio.h>

int main(){
	srand(time(NULL));
	for (int i = 0; i < 5; i++){
		 rand();
	}
	printf("1\n5\n2\n%d", rand());
	return 0;

}
