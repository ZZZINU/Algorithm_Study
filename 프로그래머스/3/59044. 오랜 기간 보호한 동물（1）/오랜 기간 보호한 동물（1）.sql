select I.name, I.datetime
from ANIMAL_INS as I
left outer join ANIMAL_OUTS as O on I.ANIMAL_ID = O.ANIMAL_ID
where O.DATETIME is null
order by I.datetime
limit 3