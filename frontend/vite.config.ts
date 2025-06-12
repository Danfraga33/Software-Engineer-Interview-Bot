import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// No remix plugin ?
export default defineConfig({
	plugins: [react()],
	server: {
		host: '0.0.0.0',
		port: process.env.PORT ? parseInt(process.env.PORT) : 5175,
	},
	preview: {
		host: '0.0.0.0',
		port: process.env.PORT ? parseInt(process.env.PORT) : 5175,
		allowedHosts: ['software-engineer-interview-bot.fly.dev'],
	},
});
