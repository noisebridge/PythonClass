

-- Running this script: 
-- Execute: .read myscript.sql 
-- Output will overwrite: sampledb.sqlite


-- This file is created if it doesn't exist.
.open "sampledb.sqlite"

ATTACH DATABASE "physics.sqlite" AS physics;

-- Note that this doesn't copy constraints!
-- We also lose our indexes... maybe we should physically copy the old DB and remove any unwanted data.
-- Also see: http://stackoverflow.com/questions/19600711/copy-sqlite-index-from-one-database-to-another
CREATE TABLE volScale AS SELECT * from physics.volScale;

CREATE TABLE "OfficeSupplies" (
  "Name" varchar(100) DEFAULT NULL,
  "Description" varchar(3000) DEFAULT NULL,
  "Mass" integer DEFAULT 0,
  "MassUnits" varchar(100) DEFAULT 'grams',
  "Volume" integer DEFAULT 0,
  "VolumeUnits" varchar(100) DEFAULT 'liters',
  "timePublished" integer DEFAULT 0,
  "pKey" integer PRIMARY KEY,
  -- Constraints say what can't be duplicated. This conflict is triggered if ALL listed items are equal.
  -- This disregards publish time, disallowing exact duplicates otherwise.
  -- Default behavior is to keep the original entry and discard the duplicate replacement.
  UNIQUE(Name, Description, Mass, MassUnits, Volume, VolumeUnits) ON CONFLICT IGNORE
);

CREATE INDEX "OfficeSupplies_Name" ON "OfficeSupplies" ("Name");
CREATE INDEX "OfficeSupplies_Description" ON "OfficeSupplies" ("Description");
CREATE INDEX "OfficeSupplies_Mass" ON "OfficeSupplies" ("Mass");
CREATE INDEX "OfficeSupplies_Volume" ON "OfficeSupplies" ("Volume");
CREATE INDEX "OfficeSupplies_timePublished" ON "OfficeSupplies" ("timePublished");


