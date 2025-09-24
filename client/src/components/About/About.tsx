import { JSX } from "react"

const About = (): JSX.Element => {
   return (
      <div className="about">
         <div className="about__main">
            <h1>Общая информация</h1>
            <p>Прототип навигатора для помощи в ориентировании по университету (6 и 2 корпуса)</p>
            <span>Поддержка</span>
         </div>
         <div className="about__team">
            <h2>Команда "Код в сапоге"</h2>
            <ul>
               <li>Байсалямов Радмир</li>
               <li>Коваленко Никита</li>
               <li>Миргазямов Самир</li>
               <li>Стрельников Денис</li>
            </ul>
         </div>
      </div>
   )
}

export default About