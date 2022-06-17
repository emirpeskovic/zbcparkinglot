CREATE TYPE parkingstatus AS ENUM ('Available', 'Reserved', 'Occupied', 'Unknown');

CREATE TABLE users
(
    id            SERIAL,
    name          VARCHAR,
    address       VARCHAR,
    email         VARCHAR,
    phone_number  VARCHAR,
    administrator INTEGER,
    CONSTRAINT users_pkey
        PRIMARY KEY (id),
    CONSTRAINT users_email_key
        UNIQUE (email),
    CONSTRAINT users_phone_number_key
        UNIQUE (phone_number)
);

ALTER TABLE users
    ADD CONSTRAINT check_name
        CHECK ((name)::TEXT ~* '^[A-Za-z]+$'::TEXT);

ALTER TABLE users
    ADD CONSTRAINT check_email
        CHECK ((email)::TEXT ~* '^[A-Za-z0-9._+%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$'::TEXT);

ALTER TABLE users
    ADD CONSTRAINT check_phone_number
        CHECK ((phone_number)::TEXT ~* '^[0-9]{8}$'::TEXT);

CREATE TABLE cars
(
    id            SERIAL,
    license_plate VARCHAR,
    owner         INTEGER,
    CONSTRAINT cars_pkey
        PRIMARY KEY (id),
    CONSTRAINT cars_owner_fkey
        FOREIGN KEY (owner) REFERENCES users
);

CREATE TABLE sensors
(
    id             SERIAL,
    latitude       DOUBLE PRECISION,
    longitude      DOUBLE PRECISION,
    parking_status parkingstatus,
    updated_at     TIMESTAMP,
    user_id        INTEGER,
    CONSTRAINT sensors_pkey
        PRIMARY KEY (id),
    CONSTRAINT sensors_user_id_fkey
        FOREIGN KEY (user_id) REFERENCES users
);

CREATE TABLE cards
(
    card_number VARCHAR NOT NULL,
    cvv         VARCHAR,
    exp_year    VARCHAR,
    exp_month   VARCHAR,
    user_id     INTEGER,
    CONSTRAINT cards_pkey
        PRIMARY KEY (card_number),
    CONSTRAINT cards_user_id_fkey
        FOREIGN KEY (user_id) REFERENCES users
);

ALTER TABLE cards
    ADD CONSTRAINT check_card_number
        CHECK ((card_number)::TEXT ~* '^[0-9]{16}$'::TEXT);

ALTER TABLE cards
    ADD CONSTRAINT check_card_cvv
        CHECK ((cvv)::TEXT ~* '^[0-9]{3}$'::TEXT);

ALTER TABLE cards
    ADD CONSTRAINT check_card_exp_year
        CHECK ((exp_year)::TEXT ~* '^[0-9]{4}$'::TEXT);

ALTER TABLE cards
    ADD CONSTRAINT check_card_exp_month
        CHECK ((exp_month)::TEXT ~* '^(1[0-2]|[1-9])$'::TEXT);

CREATE TABLE invoices
(
    id            SERIAL,
    start_date    TIMESTAMP,
    end_date      TIMESTAMP,
    license_plate VARCHAR,
    parking_price INTEGER,
    user_id       INTEGER,
    CONSTRAINT invoices_pkey
        PRIMARY KEY (id),
    CONSTRAINT invoices_user_id_fkey
        FOREIGN KEY (user_id) REFERENCES users
);

