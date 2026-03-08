-- ==========
-- = Fridays at end of fiscal month
-- ==========
set heading off
set pagesize 0
spool calendar_monthending_fridays.txt
select target_date from (select max(full_week_end)-1 as target_date from aps_calendar group by fiscal_month_start) order by target_date;
spool off


-- ==========
-- = Saturdays at end of fiscal month
-- ==========
set heading off
set pagesize 0
spool calendar_monthending_saturdays.txt
select target_date from (select max(full_week_end) as target_date from aps_calendar group by fiscal_month_start) order by target_date;
spool off


-- ==========
-- = Fridays, all weeks EXCEPT last week of fiscal month
-- ==========
set heading off
set pagesize 0
spool calendar_nonmonthending_fridays.txt
select target_date from 
	(select distinct (full_week_end-1) as target_date from aps_calendar) 
	MINUS
	(select (max(full_week_end)-1) as target_date from aps_calendar group by fiscal_month_start)
	order by target_date;
spool off


-- ==========
-- = Saturdays, all weeks EXCEPT last week of fiscal month
-- ==========
set heading off
set pagesize 0
spool calendar_nonmonthending_saturdays.txt
select target_date from 
	(select distinct full_week_end as target_date from aps_calendar) 
	MINUS
	(select max(full_week_end) as target_date from aps_calendar group by fiscal_month_start)
	order by target_date;
spool off


#---
# exit
#---
exit;
exit;

