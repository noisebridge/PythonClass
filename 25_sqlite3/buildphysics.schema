

-- Running this script: 
-- Execute: .read myscript.sql 
-- Output will overwrite: physics.sqlite


-- This file is created if it doesn't exist.
.open "physics.sqlite"


CREATE TABLE "volScale" (
  -- Min and Max volumes aren't exclusive to a Physics system and may overlap.
  "minVolume" integer DEFAULT 0,
  "maxVolume" integer DEFAULT 0,
  -- Use Quantum, Newtonian, NewtonianStellar, and Universal categories for now.
  "physicsCategory" varchar(100) DEFAULT NULL,
  "pKey" integer PRIMARY KEY
);

CREATE INDEX "volScale_minVolume" ON "volScale" ("minVolume");
CREATE INDEX "volScale_maxVolume" ON "volScale" ("maxVolume");
CREATE INDEX "volScale_physicsCategory" ON "volScale" ("physicsCategory");


