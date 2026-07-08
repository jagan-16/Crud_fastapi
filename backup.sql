--
-- PostgreSQL database dump
--

\restrict XpkJUE9TJf3ZNp7pQOTWefo7LvuTi7x23N8amg0w5kczfZx1Lne21CV4d2kmjvy

-- Dumped from database version 16.14 (Ubuntu 16.14-0ubuntu0.24.04.1)
-- Dumped by pg_dump version 16.14 (Ubuntu 16.14-0ubuntu0.24.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO postgres;

--
-- Name: customer_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.customer_id_seq
    START WITH 1000
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.customer_id_seq OWNER TO postgres;

--
-- Name: customers; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.customers (
    customer_id integer NOT NULL,
    name character varying NOT NULL,
    mobile_number character varying NOT NULL,
    email character varying NOT NULL,
    address character varying NOT NULL,
    created_at timestamp without time zone DEFAULT now() NOT NULL,
    updated_at timestamp without time zone DEFAULT now() NOT NULL
);


ALTER TABLE public.customers OWNER TO postgres;

--
-- Name: orderItem; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."orderItem" (
    order_item_id integer NOT NULL,
    order_id uuid,
    product_id integer,
    quantity integer NOT NULL,
    created_at timestamp without time zone DEFAULT now() NOT NULL,
    updated_at timestamp without time zone DEFAULT now() NOT NULL
);


ALTER TABLE public."orderItem" OWNER TO postgres;

--
-- Name: order_item_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.order_item_seq
    START WITH 10000
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.order_item_seq OWNER TO postgres;

--
-- Name: orders; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.orders (
    order_id uuid NOT NULL,
    customer_id integer,
    created_at timestamp without time zone DEFAULT now() NOT NULL,
    updated_at timestamp without time zone DEFAULT now() NOT NULL
);


ALTER TABLE public.orders OWNER TO postgres;

--
-- Name: products; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.products (
    id integer NOT NULL,
    name character varying NOT NULL,
    original_price double precision NOT NULL,
    quantity integer NOT NULL,
    created_at timestamp without time zone DEFAULT now() NOT NULL,
    updated_at timestamp without time zone DEFAULT now() NOT NULL,
    discount_percentage double precision,
    discounted_price double precision
);


ALTER TABLE public.products OWNER TO postgres;

--
-- Name: products_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.products_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.products_id_seq OWNER TO postgres;

--
-- Name: products_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.products_id_seq OWNED BY public.products.id;


--
-- Name: products id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.products ALTER COLUMN id SET DEFAULT nextval('public.products_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.alembic_version (version_num) FROM stdin;
421ccd8d7753
\.


--
-- Data for Name: customers; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.customers (customer_id, name, mobile_number, email, address, created_at, updated_at) FROM stdin;
1000	John Doe	1234567890	john.doe@example.com	123 Main St	2026-07-07 14:15:56.516866	2026-07-07 14:15:56.516866
1001	Jane Smith	0987654321	jane.smith@example.com	456 Oak Ave	2026-07-07 14:15:56.516866	2026-07-07 14:15:56.516866
1002	arun	94646w7282	guweuet@gmail	4/6 south street , adayaar	2026-07-07 14:15:56.516866	2026-07-07 14:15:56.516866
1003	arun	89765332	arun@talent	guindy 	2026-07-07 08:55:43.052248	2026-07-07 08:55:43.052254
\.


--
-- Data for Name: orderItem; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."orderItem" (order_item_id, order_id, product_id, quantity, created_at, updated_at) FROM stdin;
10000	a2fddbb6-cc7c-4e8e-b748-16f2cb1b26eb	1	3	2026-07-07 14:15:56.516866	2026-07-07 14:15:56.516866
10001	37b0641e-3522-4ee8-9adf-a0fb5dc3d236	2	3	2026-07-07 14:15:56.516866	2026-07-07 14:15:56.516866
10002	22f1b9a8-4156-4276-81c4-581b5d7f2b00	8	1	2026-07-07 14:15:56.516866	2026-07-07 14:15:56.516866
10003	22f1b9a8-4156-4276-81c4-581b5d7f2b00	3	1	2026-07-07 14:15:56.516866	2026-07-07 14:15:56.516866
\.


--
-- Data for Name: orders; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.orders (order_id, customer_id, created_at, updated_at) FROM stdin;
a2fddbb6-cc7c-4e8e-b748-16f2cb1b26eb	1001	2026-07-07 14:15:56.516866	2026-07-07 14:15:56.516866
37b0641e-3522-4ee8-9adf-a0fb5dc3d236	1002	2026-07-07 14:15:56.516866	2026-07-07 14:15:56.516866
22f1b9a8-4156-4276-81c4-581b5d7f2b00	1002	2026-07-07 14:15:56.516866	2026-07-07 14:15:56.516866
\.


--
-- Data for Name: products; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.products (id, name, original_price, quantity, created_at, updated_at, discount_percentage, discounted_price) FROM stdin;
1	chair	20	4	2026-07-07 14:15:56.516866	2026-07-07 14:15:56.516866	10	18
2	laptop 	19.99	0	2026-07-07 14:15:56.516866	2026-07-07 14:15:56.516866	20	15.991999999999999
3	fan	80	8	2026-07-07 14:15:56.516866	2026-07-07 14:15:56.516866	15	68
8	chair	60	9	2026-07-07 14:15:56.516866	2026-07-07 14:15:56.516866	15	48
9	stool	70	85	2026-07-07 08:52:58.171612	2026-07-07 08:54:06.924629	15	63
10	bottle	230	1000	2026-07-07 10:26:56.841686	2026-07-07 10:26:56.841692	40	\N
\.


--
-- Name: customer_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.customer_id_seq', 1003, true);


--
-- Name: order_item_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.order_item_seq', 10003, true);


--
-- Name: products_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.products_id_seq', 10, true);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: customers customers_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.customers
    ADD CONSTRAINT customers_pkey PRIMARY KEY (customer_id);


--
-- Name: orderItem orderItem_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."orderItem"
    ADD CONSTRAINT "orderItem_pkey" PRIMARY KEY (order_item_id);


--
-- Name: orders orders_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_pkey PRIMARY KEY (order_id);


--
-- Name: products products_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_pkey PRIMARY KEY (id);


--
-- Name: ix_customers_customer_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_customers_customer_id ON public.customers USING btree (customer_id);


--
-- Name: ix_orders_order_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_orders_order_id ON public.orders USING btree (order_id);


--
-- Name: ix_products_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_products_id ON public.products USING btree (id);


--
-- Name: orderItem orderItem_order_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."orderItem"
    ADD CONSTRAINT "orderItem_order_id_fkey" FOREIGN KEY (order_id) REFERENCES public.orders(order_id);


--
-- Name: orderItem orderItem_product_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."orderItem"
    ADD CONSTRAINT "orderItem_product_id_fkey" FOREIGN KEY (product_id) REFERENCES public.products(id);


--
-- Name: orders orders_customer_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_customer_id_fkey FOREIGN KEY (customer_id) REFERENCES public.customers(customer_id);


--
-- PostgreSQL database dump complete
--

\unrestrict XpkJUE9TJf3ZNp7pQOTWefo7LvuTi7x23N8amg0w5kczfZx1Lne21CV4d2kmjvy

