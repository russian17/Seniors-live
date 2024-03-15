--
-- PostgreSQL database dump
--

-- Dumped from database version 16.1
-- Dumped by pg_dump version 16.1

-- Started on 2024-03-16 00:13:07

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
-- TOC entry 216 (class 1259 OID 16495)
-- Name: Categories; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Categories" (
    category_id integer NOT NULL,
    category_name character varying
);


ALTER TABLE public."Categories" OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 16519)
-- Name: Guests; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Guests" (
    guest_id integer NOT NULL,
    younger_id integer,
    senior_id integer,
    meeting_id integer NOT NULL
);


ALTER TABLE public."Guests" OWNER TO postgres;

--
-- TOC entry 218 (class 1259 OID 16514)
-- Name: Meetings; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Meetings" (
    meeting_id integer NOT NULL,
    senior_id integer
);


ALTER TABLE public."Meetings" OWNER TO postgres;

--
-- TOC entry 215 (class 1259 OID 16488)
-- Name: Seniors; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Seniors" (
    senior_id integer NOT NULL,
    senior_fullname character varying NOT NULL,
    senior_username character varying,
    senior_password character varying,
    senior_skills character varying,
    category_id integer
);


ALTER TABLE public."Seniors" OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 16507)
-- Name: Youngers; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Youngers" (
    younger_id integer NOT NULL,
    younger_fullname character varying,
    younger_username character varying,
    younger_password character varying
);


ALTER TABLE public."Youngers" OWNER TO postgres;

--
-- TOC entry 4652 (class 2606 OID 16501)
-- Name: Categories category_id; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Categories"
    ADD CONSTRAINT category_id PRIMARY KEY (category_id);


--
-- TOC entry 4658 (class 2606 OID 16523)
-- Name: Guests guest_id; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Guests"
    ADD CONSTRAINT guest_id PRIMARY KEY (guest_id);


--
-- TOC entry 4656 (class 2606 OID 16518)
-- Name: Meetings meeting_id; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Meetings"
    ADD CONSTRAINT meeting_id PRIMARY KEY (meeting_id);


--
-- TOC entry 4650 (class 2606 OID 16494)
-- Name: Seniors senior_id; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Seniors"
    ADD CONSTRAINT senior_id PRIMARY KEY (senior_id);


--
-- TOC entry 4654 (class 2606 OID 16513)
-- Name: Youngers younger_id; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Youngers"
    ADD CONSTRAINT younger_id PRIMARY KEY (younger_id);


--
-- TOC entry 4659 (class 2606 OID 16502)
-- Name: Seniors category_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Seniors"
    ADD CONSTRAINT category_id FOREIGN KEY (category_id) REFERENCES public."Categories"(category_id) NOT VALID;


--
-- TOC entry 4661 (class 2606 OID 16534)
-- Name: Guests meeting_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Guests"
    ADD CONSTRAINT meeting_id FOREIGN KEY (meeting_id) REFERENCES public."Meetings"(meeting_id) NOT VALID;


--
-- TOC entry 4662 (class 2606 OID 16529)
-- Name: Guests senior_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Guests"
    ADD CONSTRAINT senior_id FOREIGN KEY (senior_id) REFERENCES public."Seniors"(senior_id) NOT VALID;


--
-- TOC entry 4660 (class 2606 OID 16539)
-- Name: Meetings senior_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Meetings"
    ADD CONSTRAINT senior_id FOREIGN KEY (senior_id) REFERENCES public."Seniors"(senior_id) NOT VALID;


--
-- TOC entry 4663 (class 2606 OID 16524)
-- Name: Guests younger_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Guests"
    ADD CONSTRAINT younger_id FOREIGN KEY (younger_id) REFERENCES public."Youngers"(younger_id) NOT VALID;


-- Completed on 2024-03-16 00:13:07

--
-- PostgreSQL database dump complete
--

