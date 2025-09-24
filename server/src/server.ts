import app from './app.js';
import config from './config.js';
import type { Request, Response } from 'express';

app.listen(config.port, () => {
  console.log(`Server running on port ${config.port}`);
});

app.get("/", (req: Request, res: Response) => {
  res.send("Server is running")
})