# Bibliotecas
import os
import argparse
import subprocess

# Classe que representa o script Git
class GitScript:
    def __init__(self, message=None, update_submodule=False):
        self.message = message
        self.update_submodule = update_submodule

    # Método para executar o comando 'git pull'
    def pull(self):
        """
        Faz o git pull na branch atual
        """
        print("Fazendo git pull...")
        os.system("git pull")

    # Método para executar o comando 'git push'
    def push(self):
        """
        Faz o git push na branch atual
        """
        print("Fazendo git push...")
        os.system(f"git push origin $(git branch --show-current)")

    # Método para atualizar submódulos, se necessário
    def update_submodules(self):
        """
        Verifica se há submódulos atualizados e os atualiza automaticamente
        """
        print("Atualizando submódulos...")
        os.system("git submodule update --remote")

    # Método para fazer commit das alterações com uma mensagem especificada
    def commit_changes(self):
        """
        Faz o commit das alterações com a mensagem especificada pelo usuário
        """
        if not self.message:
            self.message = "Update"

        print(f"Fazendo commit com a mensagem '{self.message}'...")
        os.system(f"git add . && git commit -m '{self.message}'")

    # Método para lidar com conflitos durante o push
    def handle_conflicts(self):
        """
        Verifica se há conflitos no momento de fazer o push e tenta resolvê-los
        """
        while True:
            print("Tentando fazer push...")
            result = subprocess.run(["git", "push", "origin", "$(git branch --show-current)"], capture_output=True)
            output = result.stdout.decode("utf-8")
            error = result.stderr.decode("utf-8")

            if "Merge conflict" in error:
                print("Houve um conflito de mesclagem. Por favor, resolva manualmente usando a ferramenta de mesclagem do Git.")
                input("Pressione enter para continuar...")
            else:
                print(output)
                break

    # Método principal que executa os comandos Git
    def run(self):
        """
        Executa os comandos git pull, commit, push e atualiza submódulos (se necessário)
        """
        self.pull()

        if self.update_submodule:
            self.update_submodules()

        self.commit_changes()

        try:
            self.handle_conflicts()
            self.push()
        except subprocess.CalledProcessError as error:
            print(error)
            print("Ocorreu um erro ao fazer o push. Por favor, resolva os conflitos manualmente.")
            input("Pressione enter para continuar...")
            self.handle_conflicts()
            self.push()

# Ponto de entrada do script
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Script para automatizar comandos git.")
    parser.add_argument("-m", "--message", help="Mensagem do commit.", default=None)
    parser.add_argument("-u", "--update-submodule", help="Atualiza submódulos.", action="store_true")
    args = parser.parse_args()

    git_script = GitScript(args.message, args.update_submodule)
    git_script.run()
