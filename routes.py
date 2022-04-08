from app import app
from flask import render_template,request
import sqlite3

##con=sqlite3.connect("slangweb.db")
##con.execute
##c=con.cursor()
##print("base de datos abierta")
##
##
##def creartabla():
##    c.execute("""
##    CREATE TABLE SLANGSWEB(
##    ID  INTEGER PRIMARY KEY AUTOINCREMENT,
##    SLANG        TEXT                 NOT NULL,
##    SIGNIFICADO  TEXT                 NOT NULL
##    )""")
##def rellenar_tabla():
##    c.execute("""
##         INSERT INTO slangsweb(ID,SLANG,SIGNIFICADO)
##         VALUES(1,'Que xopa','saludo')
##         """)
##
##    c.execute("""
##         INSERT INTO slangsweb(ID,SLANG,SIGNIFICADO)
##         VALUES(2,'Mopri','Amigo cercano')
##         """)
##
##    c.execute("""
##         INSERT INTO slangsweb(ID,SLANG,SIGNIFICADO)
##         VALUES(3,'Rantan','Bastante')
##         """)
##    con.commit()
##creartabla()
##rellenar_tabla()
##print("tabla creada")

@app.route("/")
def index():
    return render_template("index.html");

@app.route("/add")
def add():
    return render_template("add.html")
@app.route("/savedetails",methods =["POST","GET"])
def saveDetails():
    msg="msg"
    if request.method == "POST":
        try:
            Slang=request.form["Slang"]
            Significado=request.form["significado"]
            with sqlite3.connect("slangweb.db") as con:
                cur=con.cursor()
                cur.execute("INSERT into SLANGSWEB(Slang,Significado) values(?,?)",(Slang,Significado))
                con.commit()
                msg="Slang agregado con éxito!"
        except:
             con.rollback()
             msg="No se puede agregar slang al diccionario"
        finally:
            return render_template("success.html",msg=msg)
            con.close()
@app.route("/view")
def view():
    con=sqlite3.connect("slangweb.db")
    con.row_factory=sqlite3.Row
    cur=con.cursor()
    cur.execute("select * from SLANGSWEB")
    rows= cur.fetchall()
    return render_template("view.html",rows=rows)
@app.route("/delete")
def delete():
    return render_template("delete.html")
@app.route("/deleterecord",methods = ["POST"])  
def deleterecord():  
    ID = request.form["ID"]  
    with sqlite3.connect("slangweb.db") as con:  
        try:  
            cur = con.cursor()  
            cur.execute('DELETE FROM SLANGSWEB WHERE ID=?',ID)  
            msg = "eliminado con éxito!" 
        except:  
            msg = "no se puede eliminar" 
        finally:  
            return render_template("eliminar_registro.html")

@app.route('/edit')
def edit():
    return render_template("edit.html")
@app.route('/savedetails2',methods=["POST","GET"])
def savedetails2():
    msg="msg"
    if request.method =='POST':
        try:
            item_ID=number
            item_SLANG =request.form['SLANG']
            item_SIGNIFICADO=request.form['SIGNIFICADO']
            with sqlite3.connect("slangweb.db") as con:
                cur=con.cursor()
                cur.execute("UPDATE SLANGSWEB SET ID=?,SLANG=?,SIGNIFICADO=?",
                (item_ID,item_SLANG,item_SIGNIFICADO))
                con.commit()
                cur.execute("SELECT*FROM SLANGSWEB WHERE ID=?",(number,))
                item=cur.fetchone()
                con.close()
        except:
            con.rollback
            msg="No se puede editar"
        finally:
            return render_template("success.html",msg=msg)
if __name__== '__main__':
    app.run(debug=True)
