import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import { QueryClient, QueryClientProvider, useQuery } from 'react-query';

const root = ReactDOM.createRoot(document.getElementById('root'))
const Query_Client = new QueryClient();

root.render(
    <React.StrictMode>
        <QueryClientProvider client={Query_Client}>
            <App />
        </QueryClientProvider>
    </React.StrictMode>
)
