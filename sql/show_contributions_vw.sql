DROP VIEW IF EXISTS contributions_vw;
CREATE VIEW contributions_vw AS
select concat_ws(' ', i.first_name, i.middle_name, i.last_name) as name, c.* from contributions c
inner join individuals i on i.id = c.source_id and (c.source_type = 'Individual' or c.source_type = 'Lobbyist')
Union all
select pc.name as name, c.* from contributions c
inner join political_committees pc on pc.id = c.source_id and c.source_type = 'Political Committee'
Union all
select ppu.name as name, c.* from contributions c
inner join political_party_units ppu on ppu.id = c.source_id and c.source_type = 'Political Party'
