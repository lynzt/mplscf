GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO mncf_web;
grant all on all sequences in schema public to mncf_web;

#  ########    ###    ########  ##       ########  ######
#     ##      ## ##   ##     ## ##       ##       ##    ##
#     ##     ##   ##  ##     ## ##       ##       ##
#     ##    ##     ## ########  ##       ######    ######
#     ##    ######### ##     ## ##       ##             ##
#     ##    ##     ## ##     ## ##       ##       ##    ##
#     ##    ##     ## ########  ######## ########  ######

DROP TABLE IF EXISTS candidates;
CREATE TABLE IF NOT EXISTS candidates (
    id serial,
    cfrs_id integer,
    first_name character varying,
    middle_name character varying,
    last_name character varying,
    slug_name character varying,
    committee_name character varying,
    committee_slug_name character varying,
    registration_date timestamp,
    termination_date timestamp,
    location character varying,
    office character varying,
    district character varying,
    ytd_revenues decimal(12,2),
    ytd_expenses decimal(12,2),
    cash_balance decimal(12,2),
    created_at timestamp,
    updated_at timestamp,
    CONSTRAINT candidates_pkey PRIMARY KEY (id)
);
CREATE INDEX candidates_cfrs_idx ON candidates (cfrs_id);
CREATE INDEX candidates_name_idx ON candidates (last_name, first_name, middle_name);
CREATE INDEX candidates_slug_idx ON candidates (slug_name);

CREATE INDEX candidates_committee_name_idx ON candidates (committee_name);
CREATE INDEX candidates_committee_slug_name_idx ON candidates (committee_slug_name);

CREATE INDEX candidates_location_idx ON candidates (location);
CREATE INDEX candidates_district_idx ON candidates (district);
CREATE INDEX candidates_office_idx ON candidates (office);

-- DROP TABLE IF EXISTS candidate_details;
-- CREATE TABLE IF NOT EXISTS candidate_details (
--     id serial,
--     sitting boolean,
--     party character varying,
--     committee_name character varying,
--     office character varying,
--     district character varying,
--     terms integer,
--     created_at timestamp,
--     updated_at timestamp,
--     CONSTRAINT candidate_details_pkey PRIMARY KEY (id)
-- );
-- CREATE INDEX candidate_details_district_idx ON candidate_details (district);
-- CREATE INDEX candidate_details_party_idx ON candidate_details (party);
-- CREATE INDEX candidate_details_office_idx ON candidate_details (office);

DROP TABLE IF EXISTS political_party_units;
CREATE TABLE IF NOT EXISTS political_party_units (
    id serial,
    registration_id integer,
    name character varying,
    slug_name character varying,
    party character varying,
    created_at timestamp,
    updated_at timestamp,
    CONSTRAINT political_party_units_pkey PRIMARY KEY (id)
);
CREATE INDEX political_party_units_name_idx ON political_party_units (name);
CREATE INDEX political_party_units_slug_idx ON political_party_units (slug_name);

DROP TABLE IF EXISTS political_committees;
CREATE TABLE IF NOT EXISTS political_committees (
    id serial,
    registration_id integer,
    name character varying,
    slug_name character varying,
    party character varying,
    created_at timestamp,
    updated_at timestamp,
    CONSTRAINT political_committees_pkey PRIMARY KEY (id)
);
CREATE INDEX political_committees_name_idx ON political_committees (name);
CREATE INDEX political_committees_slug_idx ON political_committees (slug_name);


DROP TABLE IF EXISTS individuals;
CREATE TABLE IF NOT EXISTS individuals (
    id serial,
    is_lobbyist boolean default false,
    first_name character varying,
    middle_name character varying,
    last_name character varying,
    slug_name character varying,
    address1 character varying,
    address2 character varying,
    city character varying,
    state character varying,
    zip character varying,
    employer character varying,
    created_at timestamp,
    updated_at timestamp,
    CONSTRAINT individuals_pkey PRIMARY KEY (id)
);
CREATE INDEX individuals_name_idx ON individuals (last_name, first_name, middle_name);
CREATE INDEX individuals_slug_idx ON individuals (slug_name);


DROP TABLE IF EXISTS contributions;
CREATE TABLE IF NOT EXISTS contributions (
    id serial,
    source_id integer,
    source_type character varying,
    target_id integer,
    date date,
    in_kind character varying,
    in_kind_description character varying,
    amount decimal(12,2),
    created_at timestamp,
    updated_at timestamp,
    CONSTRAINT individual_contributions_pkey PRIMARY KEY (id)
);
-- CREATE INDEX contributions_id_idx ON contributions (contributor_id);
CREATE INDEX contributions_source_id_idx ON contributions (source_id);
CREATE INDEX contributions_target_id_idx ON contributions (target_id);
CREATE INDEX contributions_date_id_idx ON contributions (date);
CREATE INDEX contributions_amount_id_idx ON contributions (amount);


DROP TABLE IF EXISTS alternate_names;
CREATE TABLE IF NOT EXISTS alternate_names (
    id serial,
    registration_id integer,
    name character varying,
    slug_name character varying,
    type character varying,
    created_at timestamp,
    updated_at timestamp,
    CONSTRAINT alternate_names_pkey PRIMARY KEY (id)
);
-- ALTER TABLE alternate_names ADD COLUMN type character varying;
CREATE INDEX alternate_names_registration_id_idx ON alternate_names (registration_id);
CREATE INDEX alternate_names_name_idx ON alternate_names (name);
CREATE INDEX alternate_names_slug_name_idx ON alternate_names (slug_name);
CREATE INDEX candidates_slug_idx ON candidates (slug_name);
