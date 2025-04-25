CREATE EXTENSION postgis;

SELECT locality, COUNT(DISTINCT id) AS records, COUNT(DISTINCT species) AS species,
decimallat AS latitude, decimallon AS longitude
FROM birds_sichuan GROUP BY locality, latitude, longitude ORDER BY species DESC, records;

select distinct species from birds_sichuan where locality = '成都植物园 (Chengdu Botanical Garden)' and
ordern = 'Accipitriformes';

select distinct species, count(distinct id) as records
from birds_sichuan where ordern = 'Accipitriformes'
group by species order by records desc;






