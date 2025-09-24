import { JSX } from "react"
import cn from 'classnames'

interface PropsType {
    index: number
    currentIndex: number
    photoSrc: string
    lastIndex: number
    setStartPoint: (num: string) => void
    setEndPoint: (num: string) => void
    setShowInput: (show: boolean) => void
    text?: string
    nums?: Array<string>
    setCurrentIndex: (index: number) => void
}

const NavigatorPoint: React.FC<PropsType> = ({ photoSrc, setStartPoint, setEndPoint, text, nums, index, setCurrentIndex, currentIndex, lastIndex, setShowInput }): JSX.Element => {
    const photo = require('./../../../../../photos/' + photoSrc);

    const nextButtonHandler = () => {
        setCurrentIndex(index + 1)
        if (currentIndex == lastIndex) {
            setShowInput(true)
            setCurrentIndex(0)
            setStartPoint("")
            setEndPoint("")
        }
    }

    return (

        <div className={cn('navigator__point', { "navigator__point--active": index == currentIndex })}>
            <span className="navigator__point-num"><span>{index + 1}</span> точка</span>
            <span className="navigator__point-num">{currentIndex == 0 ? "Вы находитесь здесь!" : currentIndex == lastIndex ? "Маршрут завершен!" : ""}</span>
            <img className="navigator__photo" src={photo} alt="point photo" />
            <span className="navigator__text">{text}</span>
            <button className="navigator__next-button" onClick={nextButtonHandler}>Я на месте!!!</button>
        </div>
    )
}

export default NavigatorPoint