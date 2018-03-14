# Resources
## Coding
### http://www.mysqltutorial.org/python-mysql-query/
### https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-select.html
## Install mysql connector
### https://dev.mysql.com/doc/connector-python/en/connector-python-installation-binary.html
### https://askubuntu.com/questions/656610/trying-to-install-mysql-connector-for-python-3

import mysql.connector
from mysql.connector import Error

#Question 1.1
try:
    conn = mysql.connector.connect(host='localhost', database='SalesOrdersExampleTest', user='root',
                                       password='rooter')
    cursor = conn.cursor()
#    cursor.execute("SELECT * FROM Categories")
    cursor.execute("""select Customers.CustomerID, Customers.CustFirstName, Customers.CustLastName
from Customers
where Customers.CustomerID not in (
select distinct o.CustomerID
from Order_Details od
inner join Products p on od.ProductNumber = p.ProductNumber
inner join Orders o on od.OrderNumber = o.OrderNumber
inner join Customers c on o.CustomerID = c.CustomerID
inner join Categories cat on p.CategoryID = cat.CategoryID
where cat.CategoryID in (2, 6)
order by o.CustomerID);""")
    rows = cursor.fetchall()

    print('Question 2.1')
    print('Total Rows:', cursor.rowcount)
    for row in rows:
        print(row)

except Error as e:
    print(e)

finally:
    cursor.close()
    conn.close()

#Question 1.2
try:
    conn = mysql.connector.connect(host='localhost', database='SalesOrdersExampleTest', user='root',
                                       password='rooter')
    cursor = conn.cursor()
    cursor.execute("""select distinct c.CustomerID, c.CustFirstName, c.CustLastName
from Order_Details od
inner join Products p on od.ProductNumber = p.ProductNumber
inner join Orders o on od.OrderNumber = o.OrderNumber
inner join Customers c on o.CustomerID = c.CustomerID
where p.CategoryID in (2)
and not exists
(select distinct c2.CustomerID, c2.CustFirstName, c2.CustLastName
from Order_Details
inner join Products on Order_Details.ProductNumber = Products.ProductNumber
inner join Orders on Order_Details.OrderNumber = Orders.OrderNumber
inner join Customers c2 on Orders.CustomerID = c2.CustomerID
where Products.CategoryID = 1 and Products.ProductName like '%Helmet'
and c.CustomerID = c2.CustomerID)
order by c.CustomerID;""")
    rows = cursor.fetchall()

    print('')
    print('Question 2.2')
    print('Total Rows:', cursor.rowcount)
    for row in rows:
        print(row)

except Error as e:
    print(e)

finally:
    cursor.close()
    conn.close()

#Question 1.3
try:
    conn = mysql.connector.connect(host='localhost', database='SalesOrdersExampleTest', user='root',
                                       password='rooter')
    cursor = conn.cursor()
    cursor.execute("""select distinct OrderNumber
from Order_Details, Products, Categories
where Order_Details.ProductNumber = Products.ProductNumber
and Products.CategoryID = Categories.CategoryID
and Categories.CategoryID = 2
and OrderNumber not in
(select distinct OrderNumber
from Order_Details, Products, Categories
where Order_Details.ProductNumber = Products.ProductNumber
and Products.CategoryID = Categories.CategoryID
and Categories.CategoryID = 1
and ProductName like '%Helmet')
order by OrderNumber;""")
    rows = cursor.fetchall()

    print('')
    print('Question 2.3')
    print('Total Rows:', cursor.rowcount)
    for row in rows:
        print(row)

except Error as e:
    print(e)

finally:
    cursor.close()
    conn.close()

#Question 1.4
try:
    conn = mysql.connector.connect(host='localhost', database='SalesOrdersExampleTest', user='root',
                                       password='rooter')
    cursor = conn.cursor()
    cursor.execute("""select distinct c.CustomerID, c.CustFirstName, c.CustLastName, od.OrderNumber
from Order_Details od
inner join Products p on od.ProductNumber = p.ProductNumber
inner join Orders o on od.OrderNumber = o.OrderNumber
right join Customers c on o.CustomerID = c.CustomerID
where p.CategoryID = 2
and od.OrderNumber in
(select distinct od.OrderNumber
from Order_Details od
inner join Products p on od.ProductNumber = p.ProductNumber
inner join Orders o on od.OrderNumber = o.OrderNumber
right join Customers c on o.CustomerID = c.CustomerID
where p.CategoryID = 1
and p.productname like '%Helmet')
order by c.CustomerID, od.OrderNumber;""")
    rows = cursor.fetchall()

    print('')
    print('Question 2.4')
    print('Total Rows:', cursor.rowcount)
    for row in rows:
        print(row)

except Error as e:
    print(e)

finally:
    cursor.close()
    conn.close()

#Question 1.5
try:
    conn = mysql.connector.connect(host='localhost', database='SalesOrdersExampleTest', user='root',
                                   password='rooter')
    cursor = conn.cursor()
    cursor.execute("""select distinct pv.VendorID, v.VendName
from Product_Vendors pv
inner join Products p on pv.ProductNumber = p.ProductNumber
inner join Categories cat on p.CategoryID = cat.CategoryID
inner join Vendors v on pv.VendorID = v.VendorID
where cat.CategoryID in (1, 5, 3)
order by pv.VendorID;""")
    rows = cursor.fetchall()

    print('')
    print('Question 2.5')
    print('Total Rows:', cursor.rowcount)
    for row in rows:
        print(row)

except Error as e:
    print(e)

finally:
    cursor.close()
    conn.close()
