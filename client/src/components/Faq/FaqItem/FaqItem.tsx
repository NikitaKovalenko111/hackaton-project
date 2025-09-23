import { JSX, useState } from "react"
import cn from "classnames"
import plusSvg from './../../../images/plus.svg'

interface PropsType {
    question: string
    answer: string
}

const FaqItem: React.FC<PropsType> = ({ question, answer }): JSX.Element => {
    const [isActive, setIsActive] = useState<boolean>(false)

    return (
        <div className={cn('faq__item', {'faq__item--active': isActive})}>
            <div className="faq__item-wrapper">
                <p className="faq__item-question">{ question }</p>
                <img width="50px" src={plusSvg} className="faq__item-close-button" alt="plus" onClick={() => {
                    setIsActive(!isActive)
                }} />
            </div>
            <div className={cn("faq__item-answer", {"faq__item-answer--active": isActive})}>
                {answer}
            </div>
        </div>
    )
}

export default FaqItem