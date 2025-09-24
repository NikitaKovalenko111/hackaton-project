import axios from "axios"
import { JSX, useState } from "react"

interface IPoint {
    [key: string]: {
        photo: string
        nums: Array<string>
    }
}

const Navigator = (): JSX.Element => {
    const [startPose, setStartPose] = useState<string>('')
    const [endPose, setEndPose] = useState<string>('')

    const [points, setPoints] = useState<Array<IPoint>>([])

    const sendButtonHandler = () => {
        axios.get(`http://185.185.68.35:3001/navigate?start=${startPose}&end=${endPose}`).then(res => {
            setPoints(res.data)
            console.log(res.data);
        })
    }

    return (
        <div className="navigator">
            <div className="navigator__inputs">
                <input type="text" placeholder="Начальная точка" value={startPose} onChange={(e) => {
                    setStartPose(e.currentTarget.value)
                }} className="navigator__input" />
                <input type="text" placeholder="Конечная точка" value={endPose} onChange={(e) => {
                    setEndPose(e.currentTarget.value)
                }} className="navigator__input" />
                <button type="submit" onClick={sendButtonHandler} className="navigator__send-button">Построить маршрут</button>
            </div>
        </div>
    )
}

export default Navigator