# Supabase Setup

## Create a new project

Create a new project at [supabase.com](https://supabase.com).

## Create the postgresql tables

### Geo table

- Create a new table named 'geo'
- Select the 'import data via spreadsheet' option and upload geo_rows.csv there.

### Test table

- Create a new table name 'test'
- Enter the following schema:
  - id: int8 (Primary)
  - id_user : uuid
  - timestamp: timestampz / default: now() at time zone utc
  - region: text
  - length: int2
  - score: int2
  - time: int4
  - speed: int4

### Highscore table

- Create a new table name 'highscore'
- Enter the following schema:
  - id_user: uuid (Primary)
  - region: text (Primary)
  - length: int2 (Primary)
  - id_test: int8 (ref -> test.id)

### Progress table

- Create a new table name 'practice_progress'
- Enter the following schema:
  - id_user: uuid (Primary)
  - region: text (Primary)
  - progress: int2

### Grade table

- Create a new table name 'practice_grade'
- Enter the following schema:
  - id_user: uuid (Primary)
  - AF: jsonb
  - AS: jsonb
  - EU: jsonb
  - NA: jsonb
  - OC: jsonb
  - SA: jsonb

## Google Auth (optionnal)

Google auth can be configured using the [official supabase tutorial](https://supabase.com/docs/guides/auth/social-login/auth-google).
