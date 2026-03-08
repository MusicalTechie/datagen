#---
#---
# Create calendars for maestro
#---
#---

#---
# Get select data from APS_CALENDAR
#---
sqlplus ees_aps_ext/ees_aps_ext@apsnad85 @get_calendar_data.sql

#---
# Strip the date and leave the time for each file
#---
TARGET=calendar_monthending_fridays.txt
cut -d' ' -f 1,1 $TARGET > tempfile.txt
mv tempfile.txt $TARGET

TARGET=calendar_monthending_saturdays.txt
cut -d' ' -f 1,1 $TARGET > tempfile.txt
mv tempfile.txt $TARGET

TARGET=calendar_nonmonthending_fridays.txt
cut -d' ' -f 1,1 $TARGET > tempfile.txt
mv tempfile.txt $TARGET

TARGET=calendar_nonmonthending_saturdays.txt
cut -d' ' -f 1,1 $TARGET > tempfile.txt
mv tempfile.txt $TARGET


