from peewee import *
import datetime
#-*-coding:utf8;
"""contraseña mysql portatil = Cdaza96!"""
db = MySQLDatabase('t_pers', user='root',passwd='Cdaza96!')

def main():
    
    command = str(input('''
        herramienta SE dd
        Sistema experto 
        [c]omenzar
    '''))
    if command.lower() == 'c':
        eval_gen()

    
     
def eval_gen():
    comp = 's'
    r1 = str(input(see_preg('1',Question)+'\n>>> '))
    if r1 == comp:
        preguntas_eval('1', '2', '3', '4', '5', Question_esp, 'Instrumentación médica')
    else:
        r2 = str(input(see_preg('2',Question)+'\n>>> '))
        if r2.lower() == comp:
            preguntas_eval('6', '7', '8', '9', '10', Question_esp, 'Imagenología médica y procesamiento de imágenes')
        else:
            r3 = str(input(see_preg('3',Question)+'\n>>> '))
            if r3.lower() == comp:
                preguntas_eval('11', '12', '13', '14', '15', Question_esp, 'Procesamiento digital de señales')
            else:
                r4 = str(input(see_preg('4',Question)+'\n>>> '))
                if r4.lower() == comp:
                    preguntas_eval('16', '17', '18', '19', '20', Question_esp, 'Biomecánica y rehabilitación')
                else:
                    r5 = str(input(see_preg('5',Question)+'\n>>> '))
                    if r5.lower() == comp:
                        preguntas_eval('21', '22', '23', '24', '25', Question_esp, 'Ingeniería clínica hospitalaria y Gestión tecnológica')    





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
        print('El campo de acción de la ingeniería biomédica es: {}.'.format(diagnostico))
    else:
        print('error')

def cargar_preguntas_esp():
    Question_esp.create_table()

    preguntas=[
        '¿1?', '¿2?', '¿3?', '¿4?', '¿5?',
        '¿6?', '¿7?', '¿8?', '¿9?', '¿10?',
        '¿11?', '¿12?', '¿13?', '¿14?', '¿15?',
        '¿16?', '¿17?', '¿18?', '¿19?', '¿20?',
        '¿21?', '¿22?', '¿23?', '¿24?', '¿25?'
    ]
      
    for i in range(0,25):
        create_preg(preguntas[i], Question_esp)
    
def cargar_preguntas_gen():
    Question.create_table()

    preguntas=[
        '¿1?',
        '¿2?',
        '¿3?',
        '¿4?',
        '¿5?'
            ]
      
    for i in range(0,5):
        create_preg(preguntas[i], Question)


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
    #cargar_preguntas_esp()
    #cargar_preguntas_gen()
    main()
   

    
    
    
    
    


