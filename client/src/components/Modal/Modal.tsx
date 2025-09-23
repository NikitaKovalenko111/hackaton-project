import { JSX } from "react";
import closeIcon from './../../images/close.png'
import cn from 'classnames'
import { NavLink } from "react-router-dom";
import logo from './../../images/logo-sign.png';

interface PropsType {
    isActive: boolean
    changeModalActive: (isActive: boolean) => void
}

const Modal: React.FC<PropsType> = ({ isActive, changeModalActive }): JSX.Element => {
    const onClickHandler = () => {
        changeModalActive(false)
    }

    return (
        <div className={cn('modal', {'modal--active': isActive})}>
            <img src={closeIcon} onClick={(e) => {
                changeModalActive(false)
            }} alt="close" className="modal__close-icon" />
            <div className="modal__wrapper">
                <div className="logo modal__logo">
                    <img width="100px" src={logo} alt="logo" />
                </div>
                <nav className="nav modal__nav">
                    <ul className="modal__nav-list">
                        <li className="modal__nav-list-item"><NavLink onClick={onClickHandler} to="/">О проекте</NavLink></li>
                        <li className="modal__nav-list-item"><NavLink onClick={onClickHandler} to="/faq">FAQ</NavLink></li>
                        <li className="modal__nav-list-item"><NavLink onClick={onClickHandler} to="/navigator">Навигатор</NavLink></li>
                    </ul>
                </nav>
            </div>
        </div>
    )
}

export default Modal