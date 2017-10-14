DROP VIEW IF EXISTS names_vw;
CREATE VIEW names_vw AS
select c.registration_id, concat_ws(' ', c.first_name, c.middle_name, c.last_name) as name, c.slug_name, 'cand' as type from candidates c
where c.slug_name is not null
union all
select pc.registration_id, pc.name as name, pc.slug_name, 'pc' as type from political_committees pc
union all
select ppu.registration_id, ppu.name as name, ppu.slug_name, 'ppu' as type from political_party_units ppu
order by name
