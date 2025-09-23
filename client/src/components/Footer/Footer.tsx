import { JSX } from "react"
import topItLogo from './../../images/top-it-logo.png'
import teamLogo from './../../images/team-logo.png'
import uustLogo from './../../images/uust-logo.png'

const Footer = (): JSX.Element => {
    return (
        <footer className="footer">
            <div className="container footer__container">
                <img height="73px" src={teamLogo} alt="team logo" />
                <img src={uustLogo} alt="uust logo" />
                <img width="192px" src={topItLogo} alt="top-it logo" />
            </div>
        </footer>
    )
}

export default Footer