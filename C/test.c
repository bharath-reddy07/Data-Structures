#include<stdio.h>
#include<stdlib.h>
#include<sys/types.h>
#include<string.h>
#include<wait.h>
#include<unistd.h>
int main(int argc,char* argv[])
{
    printf("Main function\n");
    int retval=1;
    pid_t pid=fork();
    if(pid<0)
    {
        printf("Error occured while calling fork\n");
    }
    if(pid==0)
    {
        printf("The process is in Child function\nThe pid of child function is:%d\nThe pid of parent function is:%d",getpid(),getppid());
        execl("./add",argv[1],NULL);
    }
    else
    {
        printf("The process is in the main function\nThe pid of the main function is:%d",getpid());
        wait(&retval);
        if(WIFEXITED(retval)==1)
        {
            printf("The child terminated properly\n");
        }
        else
        {
            printf("The child terminated abnormally\n");
            exit(0);
        }
    }
    return 0;
}