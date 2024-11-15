#include <stdio.h>

int main(void) {
    // Primeira parte - Trabalhando com a variável 'call'
    printf("Holas o mundo\n");
    int call;
    printf("call: ");
    scanf("%d", &call); 
    call = call + 3;
    call = call / 2;
    printf("Resultado de call: %d\n", call);

    // Segunda parte - Pergunta de confirmação
    char c;
    printf("Você está certo? (Y/N): ");
    scanf(" %c", &c);  // Note que há um espaço antes de %c para capturar corretamente o caractere

    // Verificação da resposta
    if (c == 'Y' || c == 'y') {
        printf("Acordado.\n");
    } else if (c == 'N' || c == 'n') {
        printf("Não acordado.\n");
    } else {
        printf("Resposta inválida.\n");
    }
    
    return 0;
}
// printf("call is %i\n", call);
// int (%i)
// • float (%f)
// • char (%c)
// • string (%s)