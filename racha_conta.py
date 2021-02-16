import sys
import re


class Error(Exception):
    pass


class InputError(Error):
    def __init__(self, message):
        self.message = message


def rachar_conta(compras, emails):
    try:
        compras = open(compras)
        emails = open(emails)
        lista_compras = compras.read()
        lista_emails = emails.read()
        lista_emails = set(filter(None, lista_emails.split('\n')))
        if len(lista_emails) == 0:
            raise InputError('Não foi encontrado nenhum email na lista, deve ser informado pelo menos um email!')
        lista_compras = list(filter(None, lista_compras.split('\n')))
        if len(lista_compras) == 0:
            raise InputError('Não foi encontrado nenhum item na lista de compras!')
        conta_soma = 0
        for items in lista_compras:
            items = items.split(',')
            conta_soma += (int(items[1])*int(items[2]))
        conta_divisao_inteira = conta_soma // len(lista_emails)
        conta_resto_divisao = conta_soma % len(lista_emails)
        emails_conta_dividida = {}
        for email in lista_emails:
            if not re.fullmatch(r"^[\w.-]+@([\w-]+.)+[\w-]{2,}$", email):
                raise InputError('Foi informado uma email inválido, por gentileza verifique a lista de emails')
            if conta_resto_divisao > 0:
                emails_conta_dividida[email] = conta_divisao_inteira + 1
                conta_resto_divisao -= 1
            else:
                emails_conta_dividida[email] = conta_divisao_inteira

        compras.close()
        emails.close()
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
