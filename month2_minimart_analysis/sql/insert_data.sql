-- SQL script to insert sample data
-- Insert 5 customers
INSERT INTO customers (customer_id, name, email, join_date) VALUES
(1, 'Alice Smith', 'alice@email.com', '2024-01-15'),
(2, 'Bob Johnson', 'bob@email.com', '2024-02-20'),
(3, 'Charlie Brown', 'charlie@email.com', '2024-03-05'),
(4, 'David Lee', 'david@email.com', '2024-04-10'),
(5, 'Eve Davis', 'eve@email.com', '2024-05-21');

-- Insert 5 products
INSERT INTO products (product_id, product_name, category, price) VALUES
(101, 'Apple', 'Fruit', 0.50),
(102, 'Milk', 'Dairy', 2.50),
(103, 'Bread', 'Bakery', 3.00),
(104, 'Soda', 'Drinks', 1.50),
(105, 'Cereal', 'Pantry', 4.00);

-- Insert 5+ orders (let's add a few more to make reports interesting)
INSERT INTO orders (order_id, customer_id, product_id, quantity, order_date) VALUES
(1001, 1, 101, 10, '2025-10-20'),  -- Alice buys 10 Apples
(1002, 2, 102, 2, '2025-10-21'),   -- Bob buys 2 Milks
(1003, 1, 103, 1, '2025-10-21'),   -- Alice buys 1 Bread
(1004, 3, 104, 6, '2025-10-22'),   -- Charlie buys 6 Sodas
(1005, 5, 105, 1, '2025-10-23'),   -- Eve buys 1 Cereal
(1006, 2, 104, 2, '2025-10-24'),   -- Bob buys 2 Sodas
(1007, 1, 102, 1, '2025-10-24');   -- Alice buys 1 Milk