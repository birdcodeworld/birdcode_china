CREATE EXTENSION postgis;

SELECT locality, COUNT(DISTINCT id) AS records, COUNT(DISTINCT species) AS species,
decimallat AS latitude, decimallon AS longitude
FROM birds_sichuan GROUP BY locality, latitude, longitude ORDER BY species DESC, records;

select species from birds_sichuan where locality = '成都植物园 (Chengdu Botanical Garden)' and
ordern = 'Accipitriformes';

