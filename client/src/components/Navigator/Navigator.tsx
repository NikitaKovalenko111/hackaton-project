import axios from "axios"
import { JSX, useEffect, useState } from "react"
import cn from 'classnames'
import NavigatorPoint from "./NavigatorPoint/NavigatorPoint"

interface IPoint {
    photo: string
    text?: string
    nums: Array<string>
}

const Navigator = (): JSX.Element => {
    const [startPose, setStartPose] = useState<string>('')
    const [endPose, setEndPose] = useState<string>('')

    const [points, setPoints] = useState<Array<IPoint>>([])
    const [showInputs, setShowInputs] = useState<boolean>(true)
    const [status, setStatus] = useState<number>(1)
    const [currentIndex, setCurrentIndex] = useState<number>(0)

    const sendButtonHandler = () => {
        axios.get(`http://185.185.68.35:3001/navigate?start=${startPose}&end=${endPose}`).then(res => {
            setPoints(res.data.points)
            setStatus(res.data.status)

            if (res.data.status == 1) {
                setShowInputs(false)
            }

            else {
                alert("Неверный номер аудитории или точки!")
            }
        })
    }

    return (
        <div className="navigator">
            <div className={cn('navigator__inputs', { "navigator__inputs--shown": showInputs })}>
                <input type="text" placeholder="Начальная точка" value={startPose} onChange={(e) => {
                    setStartPose(e.currentTarget.value)
                }} className="navigator__input" />
                <input type="text" placeholder="Конечная точка" value={endPose} onChange={(e) => {
                    setEndPose(e.currentTarget.value)
                }} className="navigator__input" />
                <button type="submit" onClick={sendButtonHandler} className="navigator__send-button">Построить маршрут</button>
            </div>
            <div className={cn('navigator__path', { "navigator__path--shown": !showInputs && status && points.length > 0 })}>
                {
                    points.map((el, index) => {
                        if (index == currentIndex) {
                            return <NavigatorPoint setStartPoint={setStartPose} setEndPoint={setEndPose} setShowInput={setShowInputs} lastIndex={points.length - 1} currentIndex={currentIndex} setCurrentIndex={setCurrentIndex} index={index} key={el.photo} text={el.text} photoSrc={el.photo} />
                        }
                    })
                }
            </div>
        </div >
    )
}

export default Navigator