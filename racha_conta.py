import sys
import re
import os


class Error(Exception):
    pass


class InputError(Error):
    def __init__(self, message):
        self.message = message


def rachar_conta(compras, emails):
    conta_soma = 0
    emails_conta_dividida = {}
    try:
        if os.stat(compras).st_size == 0:
            raise InputError('O arquivo com a lista de compras está vazio, por gentileza verifique!')
        if os.stat(emails).st_size == 0:
            raise InputError('O arquivo com a lista de emails está vazio, por gentileza verifique!')
        with open(compras) as compras:
            for line in compras:
                item = line.split(',')
                if (int(item[1]) < 0) or (int(item[2]) < 0):
                    raise ValueError
                conta_soma += (int(item[1]) * int(item[2]))
        with open(emails) as emails:
            lista_emails = set(emails.read().split())
            conta_divisao_inteira = conta_soma // len(lista_emails)
            conta_resto_divisao = conta_soma % len(lista_emails)
            for email in lista_emails:
                if not re.fullmatch(r"^[\w.-]+@([\w-]+.)+[\w-]{2,}$", email):
                    raise InputError('Foi informado uma email inválido, por gentileza verifique a lista de emails')
                if conta_resto_divisao > 0:
                    emails_conta_dividida[email] = conta_divisao_inteira + 1
                    conta_resto_divisao -= 1
                else:
                    emails_conta_dividida[email] = conta_divisao_inteira
        return emails_conta_dividida
    except FileNotFoundError:
        return 'Arquivo não encontrado, verifique nome dos arquivos com a lista de compras e os emails!'
    except IndexError:
        return 'A lista de compras deve conter um item por linha, com a quantidade e o preço separados por vírgula!'
    except ValueError:
        return 'A lista de compras contém algum valor inválido na quantidade ou no preço, por gentileza verifique!'
    except InputError as ex:
        return ex
    finally:
        pass


if __name__ == '__main__':
    print(rachar_conta(sys.argv[1], sys.argv[2]))
