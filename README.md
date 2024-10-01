# GPT Survey

Frontend for the GPT Survey. 

## Frontend

- Install dependencies : `npm install`

- **Run in dev mode** : `npm run dev`. In dev mode, the app will use the backend defined in `.env.development`. The frontend will be served on localhost (typically http://localhost:5173/, see `npm run dev` output)

- **Build for production** : `npm run build`. In build mode, the app will use the backend defined in `.env.production`. The built files will be in the `dist` folder, those file can be statically hosted on any webserver. 

## Backend

The backend should implement the functions described in `utils/backend_example.md`.
