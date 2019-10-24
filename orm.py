from peewee import *
import datetime
#-*-coding:utf8;
"""contraseña mysql portatil = Cdaza96!"""
db = MySQLDatabase('t_pers', user='root',passwd='Cdaza96!')

terminal = '>>> '

def main():
    
    command = str(input('''
        ************************************************************
        Sistema experto: Campos de acción de la Ingeniería Biomédica
        ************************************************************
        Para su correcto funcionamiento si su respuesta es:
        Al contestar Si por favor abreviar con >>> s
        Al contestar No por favor abreviar con >>> n
        ************************************************************
        [c]omenzar
    >>>'''))
    if command.lower() == 'c':
        eval_gen()

    
     
def eval_gen():
    comp = 's'
    r1 = str(input(see_preg('1',Question)+'\n'+terminal))
    if r1 == comp:
        preguntas_eval('1', '2', '3', '4', '5', Question_esp, 'Instrumentación médica')
    else:
        r2 = str(input(see_preg('2',Question)+'\n'+terminal))
        if r2.lower() == comp:
            preguntas_eval('6', '7', '8', '9', '10', Question_esp, 'Imagenología médica y procesamiento de imágenes')
        else:
            r3 = str(input(see_preg('3',Question)+'\n'+terminal))
            if r3.lower() == comp:
                preguntas_eval('11', '12', '13', '14', '15', Question_esp, 'Procesamiento digital de señales')
            else:
                r4 = str(input(see_preg('4',Question)+'\n'+terminal))
                if r4.lower() == comp:
                    preguntas_eval('16', '17', '18', '19', '20', Question_esp, 'Biomecánica y rehabilitación')
                else:
                    r5 = str(input(see_preg('5',Question)+'\n'+terminal))
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
    r1 = input(terminal)
    nombre = n_table.get(n_table.id == b)
    print(nombre.pregunta)
    r2 = input(terminal)
    nombre = n_table.get(n_table.id == c)
    print(nombre.pregunta)
    r3 = input(terminal)
    nombre = n_table.get(n_table.id == d)
    print(nombre.pregunta)
    r4 = input(terminal)
    nombre = n_table.get(n_table.id == e)
    print(nombre.pregunta)
    r5 = input(terminal)
    if (r1 == r2) and (r3 == r4) and (r5 == r1):
        print('El campo de acción de la ingeniería biomédica es: {}.'.format(diagnostico))
    else:
        print('Por favor realice nuevamente la evaluación.')

def cargar_preguntas_esp():
    Question_esp.create_table()

    preguntas=[
        '¿Desarrollar herramientas, metodos y procedimientos menos invasivos, que permitan una recuperación mucho mas rapida?',
        '¿Realizar investigaciones en nanotecnología para disponer de herramientas que aumentan la precisión de las mediciones?',
        '¿Desarrollar herramientas que permitan la identificación de la variabilidad en los dignosticos persona a persona?',
        '¿Comprender los requisitos de comtatibilidad y aspectos de seguridad de los sistemas biomédicos?',
        '¿Crear sistemas biomédicos usando sensores específicos y dispositivos móviles?',

        '¿Desarrollo e investigación para el mejoramiento de maquinas y procedimientos de rayos X?',
        '¿Desarrollo e investigación para el mejoramiento de maquinas y procedimientos de ultrasonido?',
        '¿Desarrollo e investigación para el mejoramiento de maquinas y procedimientos de resonancia magnética nuclear?',
        '¿Diseñar procedimientos de adquisición, almacenamiento, técnicas de procesamiento de imágenes digitales?',
        '¿Desarrollar procesamiento de imágenes a partir de tecnicas como convolución, filtraje no-lineal, detección de contorno?',

        '¿Analizar las caracteristicas de las señales electrofisiológicas para obtener información conllevando a nuevos avances en fisiología y biofísica?',
        '¿Desarrollar instrumentación que permita construir sensores y ropa inteligente?',
        '¿Desarrollar herramientas que permitan limpiar y aumentar la calidad de las señales?',
        '¿Realizar investigaciones que permitan el monitoreo de aspectos como (ritmo de sueño) identificando patologias como estrés y epilepsia?',
        '¿Diseñar tratamientos que permitan combatir trastornos neurodegenerativos como el Alzheimer?',

        '¿Desarrollo de dispositivos de asistencia a discapacidades visuales?',
        '¿Desarrollo de dispositivos de asistencia a discapacidades auditivas?',
        '¿Realizar investigaciones de interfases cerebro-humano?',
        '¿Realizar investigaciones para el analisis y decodificación de información neuronal?',
        '¿Desarrollar protesis que permitan mayor movilidad y funcionalidad en las personas que las van a usar?',

        '¿Garantizar el cumplimiento de las normas para la seguridad de los equipos y las instalaciones?',
        '¿Investigar los accidentes y daños relativos a la instrumentación biomédica?',
        '¿Cumplir con los procedimientos de medidas y de verificación estableciendo para la instrumentación biomédica?',
        '¿Programar y dirigir la ejecución del mantenimiento preventivo para el equipamiento biomédico instalado,?',
        '¿Realizar el mantenimiento correctivo del equipamiento que los requiera?'
    ]
      
    for i in range(0,25):
        create_preg(preguntas[i], Question_esp)
    
def cargar_preguntas_gen():
    Question.create_table()

    preguntas=[
        '¿Tener acceso a la información, procedimientos, variabilidad para la creación de instrumentación biomédica?',
        '¿Diseñar, desarrollar e implementar procedimientos que permitan procesar imágenes médicas?',
        '¿Desarrollar aplicaciones que permitan la extracción y procesamiento de señales en el cuerpo humano?',
        '¿Desarrollar herramientas que permitan mitigar las discapacidades de los pacientes por accidentes u otras causas?',
        '¿Realizar la coordinación de las nuevas inversiones de tecnologías biomédicas?'
    ]
      
    for i in range(0,5):
        create_preg(preguntas[i], Question)


class Question(Model,object):
    pregunta = CharField(unique=True)
    

    class Meta:
        database = db
        db_table = 'preguntas'


    

class Question_esp(Model):
    pregunta = CharField(unique=True)
    

    class Meta:
        database = db
        db_table = 'preguntas_esp1'
    


if __name__ == '__main__':
    #cargar_preguntas_esp()
    #cargar_preguntas_gen()
    main()
   

    
    
    
    
    


