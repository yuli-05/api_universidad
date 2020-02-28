import web
import json
import csv
class Alumnos:
    def GET(self):
        try:
            datos=web.input()     
            if datos['token']=="1234":
                result=[]          
                result2={}          
                if datos['action']=="get":        
                    with open('static/csv/alumnos.csv','r') as csvfile:   
                        reader = csv.DictReader(csvfile)         
                        for row in reader:              
                            result.append(row)          
                            result2['Version']="0.5.0"
                            result2['status']="200 OK"
                            result2['alumnos']=result      
                    return json.dumps(result2)         
                
                elif datos['action']=="search":
                    consulta={}
                    consulta['version']="0.01"
                    consulta['status']="200 ok"
                   
                    with open('static/csv/alumnos.csv','r') as csvfile:
                        reader = csv.DictReader(csvfile)
                        result = []
                        for row in reader:
                            if str(row['matricula'])==datos['matricula']:
                                result.append(row)
                    return json.dumps(result)

                elif datos["action"] == "put":
                    p1 = datos["matricula"]
                    p2 = datos["nombre"]
                    p3 = datos["primer_apellido"]
                    p4 = datos["segundo_apellido"]
                    p5 = datos["carrera"]
                    result = []
                    result.append(p1)
                    result.append(p2)
                    result.append(p3)
                    result.append(p4)
                    result.append(p5)
                    #result="matricula,nombre,primer_apellido,segundo_apellido,carrera\n"
                    with open ('static/csv/alumnos.csv','a', newline = '') as csvfiles:
                        writer = csv.writer(csvfiles)
                        writer.writerow(result)
                    return("Insertado nuevo registro")
                
                elif datos['action'] == "update":
                    with open ('static/csv/alumnos.csv','r') as csvfiles:
                        reader =csv.DictReader(csvfiles)
                        lo = []
                        validator = 0
                        for row in reader:
                            result = []
                            if  str(row['matricula']) == datos['matricula']:
                 
                                with open ('static/csv/alumnos.csv','w') as csvfile:
                                    writer = csv.writer(csvfile)
                                    writer.writerow(row)
                                    u1 = datos["matricula"]
                                    u2 = datos["nombre"]
                                    u3 = datos["primer_apellido"]
                                    u4 = datos["segundo_apellido"]
                                    u5 = datos["carrera"]
                                    result.append(u1)
                                    result.append(u2)
                                    result.append(u3)
                                    result.append(u4)
                                    result.append(u5)
                                    lo.append(result)
                            else:
                                fila1 = row['matricula'] 
                                fila2 = row['nombre']
                                fila3 = row['primer_apellido']
                                fila4 = row['segundo_apellido']
                                fila5 = row['carrera']
                                result.append(fila1)
                                result.append(fila2)
                                result.append(fila3)
                                result.append(fila4)
                                result.append(fila5)
                                lo.append(result)
                        with open ('static/csv/alumnos.csv','a+', newline = '') as csvfiles:
                            writer = csv.writer(csvfiles)
                            for x in lo:
                                writer.writerow(x)
                        if validator == 0:
                            result.append("Dato no encontrado")
                    return json.dumps("Actualizado")

                elif datos['action'] == "delete":
                    with open ('static/csv/alumnos.csv','r') as csvfiles:
                        reader =csv.DictReader(csvfiles)
                        lo = []
                        validator = 0
                        for row in reader:
                            result = []
                            if  str(row['matricula']) == datos['matricula']:
                                with open ('static/csv/alumnos.csv','w') as csvfile:
                                    writer = csv.writer(csvfile)
                                    writer.writerow(row)
                                    print("ok")
                            else:
                                d1 = row['matricula'] 
                                d2 = row['nombre']
                                d3 = row['primer_apellido']
                                d4 = row['segundo_apellido']
                                d5 = row['carrera']
                                result.append(d1)
                                result.append(d2)
                                result.append(d3)
                                result.append(d4)
                                result.append(d5)
                                lo.append(result)
                            with open ('static/csv/alumnos.csv','a+', newline = '') as csvfiles:
                                writer = csv.writer(csvfiles)
                                writer.writerow(result)
                            if validator == 0:
                                result.append("No existe el valor")
                        return json.dumps("Realizado")
                else:                           #Si accion no es get va a poner comando no encontrado
                    result2={}
                    result2['Version']="0.5."
                    result2['status']="Command not found"
                    return json.dumps(result2)
            else:
                result={}
                result['Version']="0.5.0"
                result['status']="Los datos insertados son incorrectos"
                return json.dumps(result)
        except Exception as e:
            result={}
            text= "algo paso{}".format(e.args)
            result  ['status'] = text 
            return json.dumps(result)