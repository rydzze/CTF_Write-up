#include <stdio.h>                                                                                                                                                             
#include <stdlib.h>                                                                                                                                                            
#include <string.h>                                                                                                                                                            
#include <signal.h> 
#include <sys/types.h>                                                                                                                                                            

//b *main+79
//b *main+170
//b *main+376
//echo -e "\x0aadmin\x00\x00\x00admin" | ./auth2                            

#define FLAGSIZE_MAX 64                                                                                                                                                        
                                                                                                                                                                               
char flag[FLAGSIZE_MAX];                                                                                                                                                       
                                                                                                                                                                               
void setup(){                                                                                                                                                                  
  FILE *f = fopen("flag.txt","r");                                                                                                                                             
  fgets(flag,FLAGSIZE_MAX,f);                                                                                                                                                  
  gid_t gid = getegid();                                                                                                                                                       
  setresgid(gid, gid, gid);                                                                                                                                                    
}                                                                                                                                                                              
                                                                                                                                                                               
int main(int argc, char **argv){                                                                                                                                               
  setup();                                                                                                                                                                     
  char user[8];                                                                                                                                                                
  char pass[8];                                                                                                                                                                
  printf("Authenticate Me 2.0\n");                                                                                                                                             
  printf("--------------------------------\n");                                                                                                                                
  printf("Enter your username: ");                                                                                                                                             
  gets(user);                                                                                                                                                                  
  if(strcmp(user,"admin") == 0){                                                                                                                                               
    printf("Don't pretent you're admin =(\n");                                                                                                                                 
    return 0;                                                                                                                                                                  
  }                                                                                                                                                                            
  printf("Enter your password: ");                                                                                                                                             
  gets(pass);                                                                                                                                                                  
  if(strcmp(user,"admin") == 0 && strcmp(pass,"admin") == 0){                                                                                                                  
    printf("Welcome admin! Here is your flag: %s",flag);                                                                                                                       
  }else if(strcmp(user,"user") == 0 && strcmp(pass,"user") == 0){                                                                                                              
    printf("Welcome %s! You're authenticated!\n");                                                                                                                             
  }else{                                                                                                                                                                       
    printf("Invalid Username %s or Password %s\n",user,pass);                                                                                                                  
    printf("Hint: Distance between user and pass is %i\n",user-pass);                                                                                                          
  }                                                                                                                                                                            
  return 0;                                                                                                                                                                    
}            