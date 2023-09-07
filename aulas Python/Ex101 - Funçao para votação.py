def voto(ano_Nasc):
    from datetime import date
    ano = date.today().year
    idade = ano - ano_Nasc
    if 16 <= idade < 18 or idade > 70:
        return(f'Com {idade} anos: Voto OPCIONAL')
    elif idade >= 18:
        return(f'Com {idade} anos, VOTO OBRIGATÓRIO')
    else:
        return(f'Com {idade} anos, NÃO VOTA')



#Programa Principal
ano_Nasc = int(input('Em que ano você nasceu? '))
print(voto(ano_Nasc))

