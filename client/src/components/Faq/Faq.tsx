import { JSX } from "react";
import FaqItem from "./FaqItem/FaqItem";

const questions = [
    {
        id: 1,
        question: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Quasi natus voluptatem tempora, perferendis sequi officiis ipsum amet, impedit asperiores eligendi aspernatur odio consequatur saepe praesentium qui, optio dicta aliquid mollitia.',
        answer: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Excepturi et aspernatur totam. Modi, maxime velit. Quia et minus veritatis quo voluptas iusto saepe enim. Soluta nemo magnam nam impedit animi?'
    },
    {
        id: 2,
        question: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Quasi natus voluptatem tempora, perferendis sequi officiis ipsum amet, impedit asperiores eligendi aspernatur odio consequatur saepe praesentium qui, optio dicta aliquid mollitia.',
        answer: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Excepturi et aspernatur totam. Modi, maxime velit. Quia et minus veritatis quo voluptas iusto saepe enim. Soluta nemo magnam nam impedit animi?'
    },
    {
        id: 3,
        question: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Quasi natus voluptatem tempora, perferendis sequi officiis ipsum amet, impedit asperiores eligendi aspernatur odio consequatur saepe praesentium qui, optio dicta aliquid mollitia.',
        answer: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Excepturi et aspernatur totam. Modi, maxime velit. Quia et minus veritatis quo voluptas iusto saepe enim. Soluta nemo magnam nam impedit animi?'
    },
]

const Faq = (): JSX.Element => {
    return (
        <div className="faq">
            <div className="container faq__container">
                <div className="faq__items">
                    {
                        questions.map(el => {
                            return <FaqItem key={el.id} question={el.question} answer={el.answer} />
                        })
                    }
                </div>
            </div>
        </div>
    )
}

export default Faq