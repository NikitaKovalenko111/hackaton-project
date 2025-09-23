import { JSX } from "react"
import { NavLink } from "react-router-dom"
import logo from './../../images/logo-sign.png'

interface PropsType {
    isActive: boolean
    changeIsActive: (isActive: boolean) => void
}

const Header: React.FC<PropsType> = ({ changeIsActive, isActive }): JSX.Element => {
    return (
        <header className="header">
            <div className="container header__container">
                <div className="header__logo logo">
                    <img width="50px" src={logo} alt="logo" />
                </div>
                <nav className="header__nav">
                    <ul className="header__nav-list">
                        <li className="header__nav-list-item"><NavLink to="/">О проекте</NavLink></li>
                        <li className="header__nav-list-item"><NavLink to="/faq">FAQ</NavLink></li>
                        <li className="header__nav-list-item"><NavLink to="/navigator">Навигатор</NavLink></li>
                    </ul>
                    <div className="burger-menu header__menu" onClick={(e) => {
                        changeIsActive(true)
                    }}>
                        <input checked={isActive} type="checkbox" id="burger-checkbox" className="burger-checkbox" />
                        <label htmlFor="burger-checkbox" className="burger"></label>
                    </div>
                </nav>
            </div>
        </header>
    )
}

export default Header