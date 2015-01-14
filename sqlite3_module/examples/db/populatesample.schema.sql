

-- Running this script: 
-- Execute: .read myscript.sql 

-- This file is created if it doesn't exist.
.open "sampledb.sqlite"

INSERT INTO "OfficeSupplies" VALUES (
    'stapler', 
    'A stapler is used to staple papers together with one office staple.',
    200,
    'grams',
    '30',
    'ounces',
    '01-01-15',
    null );

