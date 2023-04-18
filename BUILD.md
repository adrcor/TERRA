# How to build

## Clone the repository

```sh
git clone https://github.com/AdrCor/TERRA.git
cd TERRA
```

## Setup a Supabase project

Refer to [SUPABASE.md](./SUPABASE.md).

## Setup the backend

You will need Python 3.11 installed on your machine.

### Backend environment variables

Create a .env files with the following environment variables :

- ENVIRONMENT=local
- DOMAIN=http://127.0.0.1:5173
- SUPABASE_URL=<your_supabase_url> (Can be found in your supabase project API settings)
- SUPABASE_SECRET_KEY=<your_supabase_secret_key> (Can be found in your supabase project API settings)
- SUPABASE_JWT=<your_supabase_jwt> (Can be found in your supabase project API settings)

### Virtual environment

```sh
cd backend
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

### Run the Flask application

```sh
python src/main.py
```

## Setup the frontend

You will need npm installed on your machine.

### Frontend environment variables

Create a .env files with the following environment variables :

- VITE_BACKEND_URL=http://127.0.0.1:5000
- VITE_SUPABASE_URL=<your_supabase_url> (Can be found in your supabase project API settings)
- VITE_SUPABASE_ANON_KEY=<your_supabase_anon_key> (Can be found in your supabase project API settings)

### Setup npm

In a new terminal:

```sh
cd frontend
npm install
```

### Run the Vue.js application

```sh
npm run dev
```
