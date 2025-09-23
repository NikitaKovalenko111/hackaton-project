import express from 'express';
import type { Request, Response } from 'express';
import data from './data.json' with { type: 'json' }
import data2 from './data2.json' with {type: 'json'}

const app = express();

interface IData {
    [key: string]: {
        [key: string]: {
            d: number,
            path: string
        }
    }
}

const dataObj: IData = data

console.log(Object.keys(data2));

app.use(express.json());

type ReqDictionary = {}
type ReqBody = { }
type ReqQuery = { start: string, end: string }
type ResBody = { }

type HandlerRequest = Request<ReqDictionary, ResBody, ReqBody, ReqQuery>

app.get('/navigate', (req: HandlerRequest, res: Response) => {
    const start: string = req.query.start
    const end: string = req.query.end

    // @ts-ignore
    res.send(dataObj[start][end].path.split('/'))
})

export default app;