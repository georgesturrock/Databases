### Q1.1 - All customers who have not purchased bikes or tires ###
select distinct c.CustomerID, c.CustFirstName, c.CustLastName
from Order_Details od
inner join Products p on od.ProductNumber = p.ProductNumber
inner join Orders o on od.OrderNumber = o.OrderNumber
right join Customers c on o.CustomerID = c.CustomerID
where p.CategoryID not in (2, 6)
or o.OrderNumber IS NULL;

### Q1.2 - All customers who have purchased a bike, but not a helmet ###
#https://dev.mysql.com/doc/refman/5.7/en/exists-and-not-exists-subqueries.html
select distinct c.CustomerID, c.CustFirstName, c.CustLastName
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
where Products.CategoryID = 1 and Products.ProductName like '%Helmet%'
and c.CustomerID = c2.CustomerID)
order by c.CustomerID;

### Q1.3 Customer Orders that have a bike but do not have a helmet ###
### Different method from 1.2 to experiment
select distinct OrderNumber
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
and ProductName like '%Helmet%')
order by OrderNumber;

### Q1.4 Customer Orders with a bike and a helmet ###
select distinct c.CustomerID, c.CustFirstName, c.CustLastName, od.OrderNumber
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
and p.productname like '%Helmet%')
order by c.CustomerID, od.OrderNumber;

### Q1.5 Vendors who sell accessories, car racks and clothing
select distinct pv.VendorID, v.VendName
from Product_Vendors pv
inner join Products p on pv.ProductNumber = p.ProductNumber
inner join Categories cat on p.CategoryID = cat.CategoryID
inner join Vendors v on pv.VendorID = v.VendorID
where cat.CategoryID in (1, 5, 3)
order by pv.VendorID;