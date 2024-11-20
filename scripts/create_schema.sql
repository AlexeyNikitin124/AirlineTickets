CREATE TABLE planes (
    serial_number varchar,
    model varchar,
    number_of_passengers int,
    load_capacity int,
    airline_owner varchar,
);

INSERT INTO planes (serial_number, model, number_of_passengers, load_capacity, airline_owner) VALUES
('A320-231L', 'Airbus_A320', 180, 16, 'Победа'),
('B737-8PL', 'Boeing_737_MAX_8', 189, 18, 'УралАэроЛайн'),
('IL76-TD-375', 'ТУ-204-300', 210, 25, 'Снежный_экспресс');
