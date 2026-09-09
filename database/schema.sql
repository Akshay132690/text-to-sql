DROP TABLE IF EXISTS order_items;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    city VARCHAR(100) NOT NULL
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(100) NOT NULL,
    price NUMERIC(12,2) NOT NULL
);

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(id),
    order_date DATE NOT NULL,
    status VARCHAR(30) NOT NULL
);

CREATE TABLE order_items (
    id SERIAL PRIMARY KEY,
    order_id INT REFERENCES orders(id),
    product_id INT REFERENCES products(id),
    quantity INT NOT NULL
);

INSERT INTO customers (name, city) VALUES
('Rahul Sharma', 'Mumbai'),
('Priya Patil', 'Pune'),
('Amit Verma', 'Delhi'),
('Sneha Kulkarni', 'Pune'),
('Rohan Mehta', 'Mumbai');

INSERT INTO products (name, category, price) VALUES
('Laptop', 'Electronics', 65000),
('Phone', 'Electronics', 30000),
('Headphones', 'Electronics', 5000),
('Office Chair', 'Furniture', 8000),
('Desk', 'Furniture', 12000);

INSERT INTO orders (customer_id, order_date, status) VALUES
(1, '2026-01-10', 'completed'),
(2, '2026-01-15', 'completed'),
(1, '2026-02-02', 'completed'),
(3, '2026-02-10', 'completed'),
(4, '2026-02-18', 'cancelled'),
(5, '2026-03-01', 'completed'),
(2, '2026-03-05', 'completed');

INSERT INTO order_items (order_id, product_id, quantity) VALUES
(1, 1, 1),
(1, 3, 2),
(2, 2, 1),
(3, 4, 2),
(4, 1, 1),
(5, 5, 1),
(6, 2, 2),
(7, 3, 3);