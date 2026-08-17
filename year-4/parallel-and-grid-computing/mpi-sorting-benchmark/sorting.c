/**
 * MPI Program that performs simple sorting
 */
 
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "mpi.h"
 
 
 // 2 word report
 // will real life comm time be visible in real execution
double * merge_array(int n, double * a, int m, double * b);
void     merge_sort(int n, double * a);
void     swap (double * a, double * b);
void     bubble_sort(int n, double * a);

// MPI sort methods
int MPI_Sort_direct(int n, double * a, int root, MPI_Comm comm);
int MPI_Sort_bucket(int n, double * a, double m, int root, MPI_Comm comm);
int MPI_Sort_oddeven(int n, double * a, int root, MPI_Comm comm);
int MPI_Sort_shell(int n, double * a, int root, MPI_Comm comm);

int MPI_Exchange(int rank1, int rank2, int n, double * a,  MPI_Comm comm);
int MPI_Is_sorted(int n, double * a, int * ans, int root, MPI_Comm comm); 
 
 
int main (int argc, char *argv[])
{
	int rank, size;
 
	int n = 10000000, i, j, k, x, q, l, shell, pair, *nr;
	double m = 10.0;
	double * scattered_array, * array;
 
	// Init + rank + size
	MPI_Init(&argc, &argv);
   	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
   	MPI_Comm_size(MPI_COMM_WORLD, &size);
    array = (double *) calloc( n, sizeof(double) );
 
	if( rank == 0 )
	{
	   //initialise the array with random values, then scatter to all processors
	   srand( ((unsigned)time(NULL)+rank) );
	   for( i = 0; i < n; i++ )
	   {
	      array[i]=((double)rand()/RAND_MAX)*m;
	   }
	}


    // call and time evaluate MPI sorting algos
    double time = MPI_Wtime();

    //MPI_Sort_direct(n, array, 0, MPI_COMM_WORLD);
    //MPI_Sort_bucket(n, array, m, 0, MPI_COMM_WORLD);
    //MPI_Sort_oddeven(n, array, 0, MPI_COMM_WORLD);
    MPI_Sort_shell(n, array, 0, MPI_COMM_WORLD);
    time = MPI_Wtime() - time; // get time
    printf("%d -> %lf\n", rank, time); // print time
 
	MPI_Finalize();
}
 


// MPI_Sort Functions
// shell
int MPI_Sort_shell(int n, double * a, int root, MPI_Comm comm){
     // get rank size of comm
    int rank, size, ans;
    MPI_Comm_rank(comm, &rank);
    MPI_Comm_size(comm, &size);
 
    // init comm time vars
    double comm_time, comm_time_start = 0.0;

    comm_time_start = MPI_Wtime();
    // scatter a to localArray
    double * localArray = (double *) calloc(n/size, sizeof(double));
    MPI_Scatter(a, n/size, MPI_DOUBLE, localArray, n/size, MPI_DOUBLE, root, comm);
    comm_time += MPI_Wtime() - comm_time_start;
    
    // init proc time variables
    double proc_time = MPI_Wtime();
    // sort localArray
    merge_sort(n/size, localArray);
    proc_time = MPI_Wtime() - proc_time;
    printf("Rank %d proc time: %lf\n", rank, proc_time); // print proc time
    
    // repeat the shell preprocess
    int left=0, right=size-1;
    
    while (left<right) {
        // calculate pair for the current process
        int pair = left + right - rank;
        
        comm_time_start = MPI_Wtime();
        // if pair is less than rank, exchange data from pair to rank, else exchange from rank to pair
        if (pair<rank) {
            MPI_Exchange(pair, rank, n/size, localArray, comm);
        } else {
            MPI_Exchange(rank, pair, n/size, localArray, comm);
        }
        comm_time += MPI_Wtime() - comm_time_start; // add to comm time
        MPI_Barrier(comm);

        int mid = (left+right)/2;
        if (rank<=mid) {
            right=mid;
        } else {
            left=mid+1;
        }
    }
 
    // repeat odd-even until sorted
    for(int step = 0; step<size; step++){
        comm_time_start = MPI_Wtime();
        if((step+rank)%2 == 0){
            if(rank<size-1)MPI_Exchange(rank, rank+1, n/size, localArray, comm);
        } else{
            if(rank>0)MPI_Exchange(rank-1, rank, n/size, localArray, comm);
        }
        comm_time += MPI_Wtime() - comm_time_start;
        MPI_Barrier(comm);
        // check localArray isSorted
        MPI_Is_sorted(n/size, localArray, &ans, root, comm);
        if(ans == 1){
        	printf("break after %d steps of %d\n", step, size);
        	break;
        }
    }
 
    comm_time_start = MPI_Wtime();
    // gather
    MPI_Gather(localArray, n/size, MPI_DOUBLE, a, n/size, MPI_DOUBLE, root, comm);
    comm_time += MPI_Wtime() - comm_time_start;

    printf("Rank %d total comm time: %lf\n", rank, comm_time); // print comm time
 
    return MPI_SUCCESS;
}

// odd-even
int MPI_Sort_oddeven(int n, double * a, int root, MPI_Comm comm){
     // get rank size of comm
    int rank, size, ans;
    MPI_Comm_rank(comm, &rank);
    MPI_Comm_size(comm, &size);

    // init comm time vars
    double comm_time, comm_time_start = 0.0;
 
    comm_time_start = MPI_Wtime();
    // scatter a to localArray
    double * localArray = (double *) calloc(n/size, sizeof(double));
    MPI_Scatter(a, n/size, MPI_DOUBLE, localArray, n/size, MPI_DOUBLE, root, comm);
    comm_time += MPI_Wtime() - comm_time_start;
 
    // init variables to measure processing time
    double proc_time = MPI_Wtime();
    // sort localArray
    merge_sort(n/size, localArray);
    proc_time = MPI_Wtime() - proc_time;
    printf("Rank %d proc time: %lf\n", rank, proc_time); // print proc time
 
    // repeat odd-even until sorted
    for(int step = 0; step<size; step++){
        comm_time_start = MPI_Wtime();
        if((step+rank)%2 == 0){
            if(rank<size-1)MPI_Exchange(rank, rank+1, n/size, localArray, comm);
        } else{
            if(rank>0)MPI_Exchange(rank-1, rank, n/size, localArray, comm);
        }
        comm_time += MPI_Wtime() - comm_time_start;
        MPI_Barrier(comm);
        // check localArray isSorted
        MPI_Is_sorted(n/size, localArray, &ans, root, comm);
        if(ans == 1){
        	printf("break after %d steps of %d\n", step, size);
        	break;
        }
    }
    
    comm_time_start = MPI_Wtime();
    // gather
    MPI_Gather(localArray, n/size, MPI_DOUBLE, a, n/size, MPI_DOUBLE, root, comm);
    comm_time += MPI_Wtime() - comm_time_start;

    printf("Rank %d total comm time: %lf\n", rank, comm_time); // print comm time
 
    return MPI_SUCCESS;
 
}

// bucket
int MPI_Sort_bucket(int n, double * a, double m, int root, MPI_Comm comm){
    // get rank size of comm
    int rank, size;
    MPI_Comm_rank(comm, &rank);
    MPI_Comm_size(comm, &size);

    // init comm time vars
    double comm_time_start, comm_time = 0.0;
 
    // allocate space for the bucket
    double *bucket = (double *)calloc(n, sizeof(double));
    
    comm_time_start = MPI_Wtime();
    // bcast a
    MPI_Bcast(a, n, MPI_DOUBLE, root, comm);
    comm_time += MPI_Wtime() - comm_time_start;
 
    // filter a into the buckets
    int count = 0;
    for(int i=0;i<n;i++){
        if(a[i] >= rank*m/size && a[i]<(rank+1)*m/size){
            bucket[count++] = a[i];
        }
    }
 
    // init variables to measure processing time
    double proc_time = MPI_Wtime();
    // sort localArray
    merge_sort(count, bucket);
    proc_time = MPI_Wtime() - proc_time;
    printf("Rank %d proc time: %lf\n", rank, proc_time);
 
    // gather-v
    int *counts = (int *)calloc(size, sizeof(int));
    int *displs = (int *)calloc(size, sizeof(int));
 
    comm_time_start = MPI_Wtime();
    MPI_Gather(&count, 1, MPI_INT, counts, 1, MPI_INT, root, comm);
    comm_time += MPI_Wtime() - comm_time_start;
 
    if(rank == root){
        displs[0] = 0;
        for(int i=1;i<size;i++){
            displs[i] = displs[i-1] + counts[i-1];
        }
    }
 
    comm_time_start = MPI_Wtime();
    MPI_Gatherv(bucket, count, MPI_DOUBLE, a, counts, displs, MPI_DOUBLE, root, comm);
    comm_time += MPI_Wtime() - comm_time_start;

    printf("Rank %d total comm time: %lf\n", rank, comm_time); // print comm time
 
    return MPI_SUCCESS;
}

// direct 
int MPI_Sort_direct(int n, double * array, int root, MPI_Comm comm){
 
    int rank, size;
    MPI_Comm_rank(comm, &rank);
    MPI_Comm_size(comm, &size);

    // init comm time vars
    double comm_time_start, comm_time = 0.0;
 
    double * localArray = (double *)calloc(n/size, sizeof(double));
 
    // scatter array to localArray with double elements
    comm_time_start = MPI_Wtime();
    int rc = MPI_Scatter(array, n/size, MPI_DOUBLE, localArray, n/size, MPI_DOUBLE, root, comm);
    if(rc != MPI_SUCCESS)return rc;
    comm_time += MPI_Wtime() - comm_time_start;
 
    // init variables to measure processing time
    double proc_time = MPI_Wtime();

    // sort localArray
    merge_sort(n/size, localArray);
    proc_time = MPI_Wtime() - proc_time;
    printf("Rank %d proc time: %lf\n", rank, proc_time);
 
    comm_time_start = MPI_Wtime();
    // gather localArray to array with double elements
    rc = MPI_Gather(localArray, n/size, MPI_DOUBLE, array, n/size, MPI_DOUBLE, root, comm);
    if(rc != MPI_SUCCESS)return rc;
    comm_time += MPI_Wtime() - comm_time_start;
 
    if( rank == 0 )
    {
        // merge the size chunks of array
        for(int i=1;i<size;i++)
        {
            double * tmpArray = merge_array(n/size*i, array, n/size, array+n/size*i);
            for(int j=0;j<(i+1)*n/size;j++)array[j] = tmpArray[j];
        }
    }

    printf("Rank %d total comm time: %lf\n", rank, comm_time); // print comm time
    return MPI_SUCCESS;
}


// other MPI functions
int MPI_Is_sorted(int n, double * a, int * ans, int root, MPI_Comm comm){
    // get rank size of comm
    int rank, size, answer;
    MPI_Comm_rank(comm, &rank);
    MPI_Comm_size(comm, &size);
    
    // gather the a[0] and a[n-1] to root
    double * first = (double *)calloc(size, sizeof(double));
    double * last = (double *)calloc(size, sizeof(double));
    MPI_Gather(&a[0], 1, MPI_DOUBLE, first, 1, MPI_DOUBLE, root, comm);
    MPI_Gather(&a[n-1], 1, MPI_DOUBLE, last, 1, MPI_DOUBLE, root, comm);
 
    // if root check MPI_Is_sorted
   if(rank == root){
   	answer=1;
   	for(int i=0;i<size-1;i++){
   		if(last[i]>first[i+1]){
   			answer=0; break;
   		}	
   	}
   }
    // bcast ans
    MPI_Bcast(&answer, 1, MPI_INT, root, comm);
    *ans = answer;
    
    return MPI_SUCCESS;
}
 
// exchange
int MPI_Exchange(int rank1, int rank2, int n, double * a,  MPI_Comm comm){
    // get rank size of comm
    int rank, size;
    MPI_Comm_rank(comm, &rank);
    MPI_Comm_size(comm, &size);
 
    // ping-pong a
    int tag1=1, tag2=2;
    double * b = (double *)calloc(n, sizeof(double));
    MPI_Status status;
    if(rank == rank1){
        MPI_Send(a, n, MPI_DOUBLE, rank2, tag1, comm);
        MPI_Recv(b, n, MPI_DOUBLE, rank2, tag2, comm, &status);
        double * tempA = merge_array(n,a,n,b);
        // rank1 retains the first half
        for(int i=0;i<n;i++)a[i] = tempA[i];
    }else if(rank == rank2){
        MPI_Recv(b, n, MPI_DOUBLE, rank1, tag1, comm, &status);
        MPI_Send(a, n, MPI_DOUBLE, rank1, tag2, comm);
        double * tempA = merge_array(n,a,n,b);
        // rank2 retains the second half
        for(int i=0;i<n;i++)a[i] = tempA[i+n];
    }
 
    return MPI_SUCCESS;
 
}
 

 
// function to merge the array a with n elements with the array b with m elements
// function returns the merged array
double * merge_array(int n, double * a, int m, double * b){
 
   int i,j,k;
   double * c = (double *) calloc(n+m, sizeof(double));
 
   for(i=j=k=0;(i<n)&&(j<m);)
 
      if(a[i]<=b[j])c[k++]=a[i++];
      else c[k++]=b[j++];
 
   if(i==n)for(;j<m;)c[k++]=b[j++];
   else for(;i<n;)c[k++]=a[i++];
 
return c;
}
 
// function to merge sort the array a with n elements
void merge_sort(int n, double * a){
 
   double * c;
   int i;
 
   if (n<=1) return;
 
   if(n==2) {
 
      if(a[0]>a[1])swap(&a[0],&a[1]);
      return;
   }
 
 
 
   merge_sort(n/2,a);merge_sort(n-n/2,a+n/2);
 
   c=merge_array(n/2,a,n-n/2,a+n/2);
 
   for(i=0;i<n;i++)a[i]=c[i];
 
return;
}
 
void     bubble_sort(int n, double * a){
    for(int i=0;i<n-1;i++)
        for(int j=0;j<n-1;j++){
            if(a[j]>a[j+1])swap(a+j, a+j+1);
        }
}
 
// swap two doubles
void swap (double * a, double * b){
 
   double temp;
 
   temp=*a;*a=*b;*b=temp;
 
}
