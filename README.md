<div style="display: flex; justify-content: space-between; align-items: flex-start;">
    <a href="https://github.com/EverWS/automate_git">
        <img src="https://img.shields.io/badge/GitHub-SEU_REPOSITORIO-brightgreen" alt="GitHub">
    </a>
        <img src="https://img.shields.io/badge/Python-3.7%2B-blue" alt="Python Version">
</div>


# Script Git Automatizado

Este é um script Python simples para automatizar algumas das tarefas Git comuns, como pull, push, commit e atualização de submódulos. Ele foi projetado para simplificar o fluxo de trabalho do Git, tornando as operações mais eficientes.

## O que o script faz

O script Git Automatizado executa as seguintes operações:

1. **Git Add**: Adiciona as alterações aos arquivos para prepará-los para o commit.

2. **Git Pull**: Atualiza o repositório local com as alterações do repositório remoto na branch atual.

3. **Git Commit**: Realiza um commit das alterações com a mensagem de commit especificada pelo usuário. Se nenhuma mensagem for fornecida, ele usará a mensagem padrão "Update".

4. **Atualização de Submódulos**: Verifica se há submódulos atualizados no repositório e os atualiza automaticamente.

5. **Tratamento de Conflitos**: Ao tentar fazer push, o script verifica se há conflitos de mesclagem. Se houver algum conflito, o script informará ao usuário e aguardará que o usuário resolva manualmente usando a ferramenta de mesclagem do Git. Após a resolução, o usuário pode continuar o push.

6. **Git Push**: Realiza o push das alterações para o repositório remoto.

## Como utilizar o script

1. **Pré-requisitos**:
    - Certifique-se de que o Git e o Python estão instalados no seu sistema.
    - Recomendado: Ative um ambiente virtual Python (venv) no diretório de trabalho, se aplicável.

2. **Baixe o Script**:
    - Faça o clone deste respositório.

3. **Execução**:
    - Abra um terminal na pasta do repositório onde deseja executar o script.

    - Execute o script com os seguintes argumentos opcionais:
        - `-m` ou `--message`: Especifique uma mensagem de commit personalizada.
        - `-u` ou `--update-submodule`: Use este argumento para atualizar submódulos.

    Exemplo de uso:
    ```shell
    python git_auto.py -m "Correção de bugs" -u
    ```

4. **Alias Git (opcional)**:
    - Você pode criar um alias Git para chamar o script com mais facilidade. Para criar um alias chamado "auto", adicione o seguinte alias ao seu arquivo `.gitconfig`:
    ```shell
    [alias]
    auto = !python /caminho/para/git_auto.py
    ```
    Certifique-se de substituir `/caminho/para/git_auto.py` pelo caminho real para o script em seu sistema.

5. **Usando o Alias Git**:
    - Após a configuração do alias, você pode usar o comando `git auto` no lugar de `python git_auto.py` para executar o script. Por exemplo:
    ```shell
    git auto -m "Correção de bugs" -u
    ```

6. **Siga as Instruções**:
    - O script solicitará que você siga as instruções e resolver quaisquer conflitos, se necessário.

7. **Aproveite a automação**:
    - O script simplificará o processo de atualização e manutenção do seu repositório Git.

## Notas

- Certifique-se de entender as operações do Git antes de usar este script, especialmente ao lidar com conflitos, já que eles podem exigir intervenção manual.

- Este script é uma ferramenta útil para agilizar as operações do Git, mas use-o com cuidado e sempre revise as alterações antes de fazer o commit e o push.

- Sinta-se à vontade para personalizar o script de acordo com suas necessidades específicas, se necessário.

- Para obter mais informações sobre as funcionalidades do Git, consulte a documentação oficial do Git em [https://git-scm.com/docs](https://git-scm.com/docs).

Esperamos que este script torne suas tarefas Git mais eficientes e seu fluxo de trabalho mais produtivo. Se você tiver alguma dúvida ou encontrar problemas, sinta-se à vontade para relatar problemas ou fazer sugestões de aprimoramento.

Happy coding!
