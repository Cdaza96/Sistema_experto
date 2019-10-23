from peewee import *
import datetime
"""contraseña mysql portatil = Cdaza96!"""
db = MySQLDatabase('t_pers', user='root',passwd='root')

def main():
    
    command = str(input('''
        Sistema experto 
        [c]omenzar
    '''))
    if command.lower() == 'c':
        eval_gen()

    
     
def eval_gen():
    comp = 's'
    r1 = str(input(see_preg('1',Question)+'\n>>> '))
    if r1 == comp:
        preguntas_eval('1', '2', '3', '4', '5', Question_esp, 'diagnostico a')
    else:
        r2 = str(input(see_preg('2',Question)+'\n>>> '))
        if r2.lower() == comp:
            preguntas_eval('1', '2', '3', '4', '5', Question_esp, 'diagnostico b')
        else:
            r3 = str(input(see_preg('3',Question)+'\n>>> '))
            if r3.lower() == comp:
                preguntas_eval('1', '2', '3', '4', '5', Question_esp, 'diagnostico c')
            else:
                r4 = str(input(see_preg('4',Question)+'\n>>> '))
                if r4.lower() == comp:
                    preguntas_eval('1', '2', '3', '4', '5', Question_esp, 'diagnostico d')
                else:
                    r5 = str(input(see_preg('5',Question)+'\n>>> '))
                    if r5.lower() == comp:
                        preguntas_eval('1', '2', '3', '4', '5', Question_esp, 'diagnostico e')    





def create_preg(preg,n_table):
    d1 = n_table(pregunta = preg)
    d1.save()

def see_preg(id_preg,n_table):
    nombre = n_table.get(n_table.id == id_preg)
    return nombre.pregunta


def preguntas_eval(a, b, c, d, e, n_table,diagnostico):
    nombre = n_table.get(n_table.id == a)
    print(nombre.pregunta)
    r1 = input()
    nombre = n_table.get(n_table.id == b)
    print(nombre.pregunta)
    r2 = input()
    nombre = n_table.get(n_table.id == c)
    print(nombre.pregunta)
    r3 = input()
    nombre = n_table.get(n_table.id == d)
    print(nombre.pregunta)
    r4 = input()
    nombre = n_table.get(n_table.id == e)
    print(nombre.pregunta)
    r5 = input()
    if (r1 == r2) and (r3 == r4) and (r5 == r1):
        print(diagnostico)
    else:
        print('error')


class Question(Model,object):
    pregunta = CharField(unique=True)
    #email = CharField(index=True)
    #created_date = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
        db_table = 'preguntas'

    




    

class Question_esp(Model):
    pregunta = CharField(unique=True)
    #email = CharField(index=True)
    #created_date = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
        db_table = 'preguntas_esp1'
    

if __name__ == '__main__':
    main()
    """
    Question_esp.create_table()

    preguntas=[
        '¿a?',
        '¿b?',
        '¿c?',
        '¿d?',
        '¿e?',
    ]
      
    for i in range(0,5):
        create_preg(preguntas[i], Question_esp)
    
        
    """    

    
    #preguntas_eval('1','2','3','4','5',Question)
    
    
    


