import argparse
import task_manager

if __name__ == "__main__":
    print("Test")

    parser = argparse.ArgumentParser(description='Process file requests')
    parser.add_argument('file_path', type=str, help="Must be a valid xml file")
    parser.add_argument('limit', type=int, help='Limit the number of requests')
    parser.add_argument('output_path',type=str,help='Must be a valid path')
    args = parser.parse_args(('./urls.xml','1','.')) #recebe os valores recebidos do 'add_argument' e os converte em um objeto!

    
    my_instance_class = task_manager.TaskManager() 
    my_instance_class.file_path = args.file_path
    my_instance_class.http_request_limit = args.limit
    my_instance_class.start()




"""
- Task Manager recebe os parâmetros: 'file_path' e o 'http_request_limit'
    - File_path: SET>Verifica se o arquivo existe; SETando-o no 'self._file_path'!
        TaskManager:Cria atributo privado self._file_path;
            HTTP_HELPER: verifica se o arquivo existe....
                TaskManager: Procura todos as linhas com a tag '<site>'
                    Report: adiciona um ítem do tipo 'RequestResult' na lista 'self.__report'
                        Request_Result: Recebe se foi bem sucedido a verificação do link e do get!
                            Report: Receber o valor do Request_Result(data) e adicionar na lista 'self.__report'
                            
    -Http_request: Mesma coisa só que no 'self._http_request_limit'!

"""


"""
Coisas a fazer:
    - Criação da pasta para output! ❌
    - Ver se o link funciona ou não!❌
    - Output em arquivo html! ❌
        - Pegar o diretório da pasta:❌
            Verificação de criação! ❌
            -Criar arquivos html:❌
                Tratamento no nome do arquivo! ✔️
    - 

"""