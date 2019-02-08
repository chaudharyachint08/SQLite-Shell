import matplotlib.pyplot as plt
import numpy as np


def plot(cr1 , cr2 , rev=False, c1='black', z=False , n=False , f = False, c2 = 'blue' ):
    'Z is to connect with ORIGIN, n for NORMALISATION, f for FILL, c is COLOR'
    if z:
        x_points,y_points = [0],[0]
    else:
        x_points,y_points = [],[]
    
    with open('buffer.txt') as buf:
        for i in buf.readlines():
            tup = i.strip('()').split(',')
            try:
                t1 = float(tup[cr1])
            except:
                t1 = None
            try:
                t2 = float(tup[cr2])
            except:
                t2 = None
            x_points.append( t1 )
            y_points.append( t2 )

    if type(x_points[1]) not in (int,float):
        x_points = list(range(len(x_points)))
    if type(y_points[1]) not in (int,float):
        y_points = list(range(len(y_points)))

    x_points = np.array(x_points)
    y_points = np.array(y_points)

    if (x_points == y_points).all():
        x_points = list(range(len(x_points)))
    #print(*x_points)
    #print(*y_points)
    
    if   n == 1:    #MIN-MAX normalisation scheme
        sub,val  = y_points.min() , y_points.max()
        y_points = (y_points-sub) / (val-sub)
    elif n == 2:    #MEAN-VAR normalisation scheme
        y_points = (y_points-y_points.mean()) / y_points.var()

    if rev:
        y_points = y_points[::-1]
        
    _ = plt.plot(x_points, y_points, c1,linewidth = 0.5)

    if f:
        plt.fill_between(x_points,min(y_points),y_points,color=c2,alpha=0.5)


def sctr(cr1 , cr2 , n=False , S=0 ,  C = 'blue' ):
    'n for NORMALISATION, S if SIZE, C is COLOR,'
    x_points,y_points = [],[]
    
    with open('buffer.txt') as buf:
        for i in buf.readlines():
            tup = i.strip('()').split(',')
            try:
                t1 = float(tup[cr1])
            except:
                t1 = None
            try:
                t2 = float(tup[cr2])
            except:
                t2 = None
            x_points.append( t1 )
            y_points.append( t2 )

    if type(x_points[1]) not in (int,float):
        x_points = list(range(len(x_points)))
    if type(y_points[1]) not in (int,float):
        y_points = list(range(len(y_points)))

    x_points = np.array(x_points)
    y_points = np.array(y_points)

    if (x_points == y_points).all():
        x_points = list(range(len(x_points)))
    #print(*x_points)
    #print(*y_points)
    
    if   n == 1:    #MIN-MAX normalisation scheme
        sub,val  = y_points.min() , y_points.max()
        y_points = (y_points-sub) / (val-sub)
    elif n == 2:    #MEAN-VAR normalisation scheme
        y_points = (y_points-y_points.mean()) / y_points.var()

    if S:
        _ = plt.scatter(x_points, y_points, c=C ,s=S)
    else:
        _ = plt.scatter(x_points, y_points, c=C )


def hist(cr,B=10,C='blue',CU=False):
    'B for BINS, C for COLOR, CU for CUMULATIVE'
    L = []
    
    with open('buffer.txt') as buf:
        for i in buf.readlines():
            tup = i.strip('()').split(',')
            try:
                t = float(tup[cr])
            except:
                t = None
            L.append( t )

    if type(L[1]) not in (int,float):
        L = list(range(len(L)))

    L = np.array(L)

    #print(*L)
    
    _ = plt.hist(L, bins=B , color=C , cumulative=CU)


def grab(file,name):
    f1 = open(file)
    st = f1.readline()
    try:
        cur.execute( 'CREATE TABLE {}({})'.format(name,','.join([i+' REAL' for i in st.strip().split(',')])) )
    except Exception as err:
        print(err)
        print( 'CREATE TABLE {}({})'.format(name,','.join([i+' REAL' for i in st.strip().split(',')])) )
    else:
        con.commit()
        
    for st in f1.readlines():
        try:
            if '' not in st.strip().split(',') :
                cur.execute( 'INSERT INTO {} VALUES({})'.format(name,','.join([i for i in st.strip().split(',')])) )
        except Exception as err:
            print(err)
            print( 'INSERT INTO {} VALUES({})'.format(name,','.join([i for i in st.strip().split(',')[1:]])) )
            break
    

def show(t='',x='',y='',a=False):
	plt.title(t)
	plt.xlabel(x)
	plt.ylabel(y)
	if a:
		plt.ylabel('equal')
	plt.show()
	
import sqlite3
#con = sqlite3.connect('D:\\population.db') OR 'D:/population.db'
#if DB file is absent, it will be created


con = sqlite3.connect(input('Enter the Actual path of DataBase\n'))
print('''
#1. NULL : NoneType Means “know nothing about it”
#2. INTEGER : int Integers
#3. REAL : float 8-byte floating-point numbers
#4. TEXT : str Strings of characters
#5. BLOB : bytes Binary data
''')
cur = con.cursor()
while True:
    try:
        a = input('SQL>')
        if not a or a[0]=='#':
            continue
        if a[:4] in ('plot','sctr','hist','grab','show'):
            try:
                exec(a)
            except:
                pass
            continue
        else:
            pass
        a=a.replace('int,','integer,')
        a=a.replace('date,','integer,')
        a=a.replace('INT,','integer,')
        a=a.replace('DATE,','integer,')
        a=a.replace('int)','integer)')
        a=a.replace('date)','integer)')
        a=a.replace('INT)','integer)')
        a=a.replace('DATE)','integer)')
        a=a.replace('/','')
        a=a.replace('-','')
        flg = False if a.split()[0].upper()=='SELECT1' else True
        a=a.replace('select1','select')
        a=a.replace('SELECT1','SELECT')
        a=cur.execute(a)
        l=cur.fetchall()
        if l!=[]:
            buf = open('buffer.txt','w')
            k=len(l[0])
            m=[]
            for i in range(k):
                m.append(max([len(str(l[j][i])) for j in range(len(l))]))
            for i in l:
                buf.write('(')
                for j in range(len(i)):
                    if flg:
                        print('{0:{1}}'.format(i[j],m[j]),end='|')
                    buf.write( '{0:{1}},'.format(i[j],m[j]))
                if flg:
                    print()
                buf.write(')\n')
            buf.close()
        con.commit()
    except sqlite3.DataError as err:
        print('DataError : ',err)
    except sqlite3.DatabaseError as err:
        print('DatabaseError : ',err)
    except sqlite3.IntegrityError as err:
        print('IntegrityError : ',err)
    except sqlite3.InterfaceError as err:
        print('InterfaceError : ',err)
    except sqlite3.InternalError as err:
        print('InternalError : ',err)
    except sqlite3.IntegrityError as err:
        print('IntegrityError : ',err)
    except sqlite3.NotSupportedError as err:
        print('NotSupportedError : ',err)
    except sqlite3.OperationalError as err:
        print('OperationalError : ',err)
    except Exception as err:
        print('Unknown Error : ',err)
