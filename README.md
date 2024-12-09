# GPT Survey

Frontend for the GPT Survey. 

## Start the frontend

- Install dependencies : 

        npm install

- **Run in dev mode** : 

        npm run dev
        
    In dev mode, the app will use the backend defined in `.env.development`. The frontend will be served on localhost (typically http://localhost:5173/, see `npm run dev` output)

- **Build for production** : `npm run build`. In build mode, the app will use the backend defined in `.env.production`. The built files will be in the `dist` folder, those file can be statically hosted on any webserver. 

## Backend

### For ML4ED members

The backend on `ml4ed_server_next`

### For external developers

The backend should implement the functions described in `utils/backend_example.md`. There is an example of such server implemented with in : `utils/backend_example.py`. 

To run it first intall :

    pip install "fastapi[standard]"

Then run 

    fastapi dev utils/backend_example.py 

(it should serve it on `localhost:8000` which must be the same address as in `.env.development`)
