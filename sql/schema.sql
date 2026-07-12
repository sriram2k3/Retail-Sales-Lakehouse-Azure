-- ======================================================
-- E-COMMERCE CAPSTONE DATABASE SCHEMA
-- ======================================================

-- PRODUCT TABLE
CREATE TABLE product (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(50) NOT NULL,
    category VARCHAR(25) DEFAULT 'others',
    price_per_qty DECIMAL(10,2) NOT NULL DEFAULT 0.00
);
ALTER TABLE product
    ADD COLUMN brand varchar(50),
    ADD COLUMN manufacturer varchar(50),
    ADD COLUMN cost_price decimal(10,2),
    ADD COLUMN mrp decimal(10,2),
    RENAME COLUMN price_per_qty TO unit_price;
    
-- CUSTOMER TABLE
CREATE TABLE customer (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_fname VARCHAR(25) NOT NULL,
    customer_lname VARCHAR(25) NOT NULL,
    email VARCHAR(100),
    location VARCHAR(20),
    age TINYINT UNSIGNED NOT NULL,
    mobile VARCHAR(15) NOT NULL
);
ALTER TABLE customer 
    ADD COLUMN customer_since DATE,
	ADD COLUMN loyalty_tier varchar(25) CHECK(loyalty_tier in ("Gold","Silver","Bronze")),
    RENAME COLUMN location TO city;

-- WAREHOUSE TABLE
CREATE TABLE warehouse (
    warehouse_id VARCHAR(5) PRIMARY KEY,
    location VARCHAR(25) NOT NULL
);
ALTER TABLE warehouse
    ADD COLUMN warehouse_name varchar(100),
    ADD COLUMN city varchar(25),
    DROP COLUMN location,
    ADD COLUMN state varchar(25),
    MODIFY COLUMN warehouse_id VARCHAR(10);

-- ORDERS TABLE
CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date DATETIME NOT NULL,
    order_status VARCHAR(25) NOT NULL CHECK (
        order_status IN (
            'Pending',
            'Out for delivery',
            'Delivered',
            'Cancelled'
        )
    ),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_customer
    FOREIGN KEY (customer_id)
    REFERENCES customer(customer_id)
);
ALTER TABLE orders
    ADD COLUMN delivery_date date,
    ADD COLUMN shipping_method varchar(30) CHECK (shipping_method IN ('Standard', 'Express', 'Same Day', 'Pickup')),
    MODIFY COLUMN order_status VARCHAR(25) NOT NULL CHECK (
        order_status IN (
            'Pending',
			'Confirmed',
			'Shipped',
			'Out for Delivery',
			'Delivered',
			'Cancelled',
			'Returned'
        )
    );

-- INVENTORY TABLE
-- tracks product stock per warehouse
CREATE TABLE inventory (
    inventory_id INT AUTO_INCREMENT PRIMARY KEY,
    warehouse_id VARCHAR(5),
    product_id INT,
    stock_qty BIGINT UNSIGNED NOT NULL,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_inventory_warehouse
    FOREIGN KEY (warehouse_id)
    REFERENCES warehouse(warehouse_id),

    CONSTRAINT fk_inventory_product
    FOREIGN KEY (product_id)
    REFERENCES product(product_id)
);
ALTER TABLE INVENTORY
    MODIFY last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP;
ALTER TABLE INVENTORY
    ADD COLUMN reorder_level INT,
    MODIFY COLUMN warehouse_id varchar(10);

-- ORDER ITEMS TABLE
CREATE TABLE order_items (
    order_item_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    qty BIGINT UNSIGNED NOT NULL,
    tot_price DECIMAL(10,2),

    CONSTRAINT fk_order_items_order
    FOREIGN KEY (order_id)
    REFERENCES orders(order_id),

    CONSTRAINT fk_order_items_product
    FOREIGN KEY (product_id)
    REFERENCES product(product_id)
);
alter table order_items
add column warehouse_id varchar(5),
add constraint fk_order_items_warehouse
foreign key(warehouse_id) references warehouse(warehouse_id);

alter table order_items
  add column discount decimal(10,2),
  rename column tot_price to line_total,
  modify column warehouse_id varchar(10);

-- PAYMENTS TABLE
CREATE TABLE payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,

    payment_type VARCHAR(15) CHECK (
        payment_type IN ('UPI','Debit/Credit','COD')
    ),

    payment_status VARCHAR(15) CHECK (
        payment_status IN ('Paid','Yet to Pay')
    ),

    CONSTRAINT fk_payment_order
    FOREIGN KEY (order_id)
    REFERENCES orders(order_id)
);
ALTER TABLE payments
    ADD COLUMN payment_date DATETIME,
    MODIFY COLUMN payment_status VARCHAR(15) CHECK (payment_status IN ('Paid','Pending','Failed','Refunded')),
    MODIFY COLUMN payment_type VARCHAR(15) CHECK (payment_type IN ('UPI','Card','Cash'));