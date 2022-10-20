import { NavLink } from 'react-router-dom'
import './Footer.css'
import logoWithText from '../../icons/squeal-in-logo.png'
import logo from '../../icons/squeal-logo-v2.png'

export default function Footer() {
    return (
        <footer id='footer-outer-wrapper' className='footer'>
            <div id='footer-inner-wrapper'>
                <div id='footer-lists-wrapper'>
                    <div id='footer-column-about' className='footer-column'>
                        <div className='footer-column-title-wrapper'>
                            <span id='footer-about-title' className='footer-column-title'>About</span>
                        </div>

                        <ul id='footer-column-ul-about' className='footer-column-ul'>
                            <li className='footer-column-li'>
                                <a className='footer-link' href='https://github.com/amanduhkv/Squeal' target='_blank' rel='noreferrer'>About Squeal</a>
                            </li>
                        </ul>
                    </div>

                    <div id='footer-column-developers' className='footer-column'>
                        <div className='footer-column-title-wrapper'>
                            <span id='footer-developers-title' className='footer-column-title'>Developers</span>
                        </div>

                        <ul id='footer-column-ul-developers' className='footer-column-ul'>
                            <li className='footer-column-li'>
                                <a className='linked-in' href='https://www.linkedin.com/in/amandakvien/' target='_blank' rel='noreferrer'>
                                    <i className="fa-brands fa-linkedin fa-sm" />
                                </a>
                                <a className='github' href='https://github.com/amanduhkv' target='_blank' rel='noreferrer'>
                                    <i className="fa-brands fa-github fa-sm" />
                                </a>
                                <span className='footer-dev-name'>Amanda Vien</span>
                            </li>
                            <li className='footer-column-li'>
                                <a className='linked-in' href='https://www.linkedin.com/in/brandon-tasaki/' target='_blank' rel='noreferrer'>
                                    <i className="fa-brands fa-linkedin fa-sm" />
                                </a>
                                <a className='github' href='https://github.com/MacFlyOSX' target='_blank' rel='noreferrer'>
                                    <i className="fa-brands fa-github fa-sm" />
                                </a>
                                <span className='footer-dev-name'>Brandon Tasaki</span>
                            </li>
                            <li className='footer-column-li'>
                                <a className='linked-in' href='https://www.linkedin.com/in/jaeyoung-hwang-71654490/' target='_blank' rel='noreferrer'>
                                    <i className="fa-brands fa-linkedin fa-sm" />
                                </a>
                                <a className='github' href='https://github.com/jaeyoungh1' target='_blank' rel='noreferrer'>
                                    <i className="fa-brands fa-github fa-sm" />
                                </a>
                                <span className='footer-dev-name'>Jae Hwang</span>
                            </li>
                            <li className='footer-column-li'>
                                <a className='linked-in' href='https://www.linkedin.com/in/michael-h-jung/' target='_blank' rel='noreferrer'>
                                    <i className="fa-brands fa-linkedin fa-sm" />
                                </a>
                                <a className='github' href='https://github.com/michaelhjung' target='_blank' rel='noreferrer'>
                                    <i className="fa-brands fa-github fa-sm" />
                                </a>
                                <span className='footer-dev-name' >Michael Jung</span>
                            </li>
                        </ul>
                    </div>

                    <div id='footer-column-business' className='footer-column'>
                        <div className='footer-column-title-wrapper'>
                            <span id='footer-business-title' className='footer-column-title'>Squeal for Business</span>
                        </div>

                        <ul id='footer-column-ul-business' className='footer-column-ul'>
                            <li className='footer-column-li'><NavLink to="/biz/new" className='footer-link'>Claim Your Business Page</NavLink></li>
                        </ul>
                    </div>

                    <div id='footer-column-languages-countries' className='footer-column'>
                        <div id='footer-languages-title-wrapper' className='footer-column-title-wrapper'>
                            <span id='footer-languages-title' className='footer-column-title'>Language</span>
                        </div>

                        <span className='footer-languages-countries-span'>English</span>


                        <div id='footer-countries-title-wrapper' className='footer-column-title-wrapper'>
                            <span id='footer-countries-title' className='footer-column-title'>Country</span>
                        </div>

                        <span className='footer-languages-countries-span'>United States</span>
                    </div>
                </div>


                <div id='footer-copyright-wrapper'>
                    <span id='footer-copyright'>
                        Copyright ©2022 Squeal Inc. Squeal, <img id='squeal-logo-with-text-copyright' src={logoWithText} alt='' />, <img id='squeal-logo-copyright' src={logo} alt='' /> and related marks are registered trademarks of Squeal.
                    </span>
                </div>
            </div>
        </footer>
    )
}
