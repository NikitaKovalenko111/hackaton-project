import express from 'express';
import type { Request, Response } from 'express';
import data from './data.json' with { type: 'json' }
import data2 from './data2.json' with {type: 'json'}
import cors from 'cors'

const app = express();

app.use(cors())

interface IData {
    [key: string]: {
        [key: string]: {
            d: number,
            path: string
        }
    }
}

const dataObj: IData = data

app.use(express.json());

type ReqDictionary = {}
type ReqBody = {}
type ReqQuery = { start: string, end: string }
type ResBody = {}

type HandlerRequest = Request<ReqDictionary, ResBody, ReqBody, ReqQuery>

interface IPoint {
    [key: string]: {
        "photo": string,
        "nums": Array<string>
    }
}

app.get('/navigate', (req: HandlerRequest, res: Response) => {
    const start: string = req.query.start
    const end: string = req.query.end

    let startBlock: string = ''
    let endBlock: string = ''

    Object.keys(data2).forEach(el => {
        // @ts-ignore
        if (data2[el]["nums"].length > 0) {
            // @ts-ignore
            if (data2[el].nums.includes(start)) {
                startBlock = el
            }
        }
        else {
            if (el == start) {
                startBlock = start
            }
        }
    })

    Object.keys(data2).forEach(el => {
        // @ts-ignore
        if (data2[el]["nums"].length > 0) {
            // @ts-ignore
            if (data2[el].nums.includes(end)) {
                endBlock = el
            }
        }
        else {
            if (el == end) {
                endBlock = end
            }
        }
    })

    if (startBlock == '' || endBlock == '') {
        res.send({
            status: 0,
            points: []
        })
    }

    // @ts-ignore
    const points = dataObj[startBlock][endBlock].path.split('/')
    const finalPoints: Array<IPoint> = []

    points.forEach(el => {
        // @ts-ignore
        finalPoints.push(data2[el])
    })

    res.send({
        status: 1,
        points: finalPoints
    })
})

export default app;