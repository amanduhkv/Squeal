import React, { useState } from 'react';
import { NavLink, useLocation } from 'react-router-dom';
import squealnLogo from '../../icons/squealnLogo.png';
import squealnLogowht from '../../icons/squealnLogowht.png';
import search from '../../icons/search.svg';
import userIcon from '../../icons/user.png';
import './NavBar.css';

function NavBar(){
    // const sessionUser = null;
    const url = useLocation();
    const [ query, setQuery ] = useState('');
    const [ location, setLocation ] = useState('');

    // let sessionLinks;

    // if (sessionUser) {
    //     sessionLinks = (<>
                <div className='side-by-side-user-buttons'>
                    
                </div>
    //     </>)
    // }

    return (
        <div className={url === '/' ? 'header-container gradient' : 'header-container gradient header-container-fixed'}>
            <div className='header-top-portion'>
                <div className='logo-left-section'>
                    <NavLink className='logo' exact to="/">
                        <img src={url === '/' ? squealnLogowht : squealnLogo}
                                            alt='logo' className='squeal-logo'/>
                    </NavLink>
                </div>
                <div className='search-and-buttons-right-section'>
                    <div className='nav-search-section'>
                        <form className='search-query-section' action='/search'>
                            <input className='search-query-input search-input'
                                type='text' value={query} onChange={(e) => setQuery(e.target.value)} />
                            <input className='search-location-input search-input'
                                type='text' value={location} onChange={(e) => setLocation(e.target.value)} />
                            <button type='submit' className='search-button'>
                                <img src={search} alt='icon' className='search-icon' />
                            </button>
                        </form>
                    </div>
                    <span className='header-gap-search-buttons' />
                    <div className='buttons-user-stuff'>
                        <NavLink to='/businesses/new' className='navbar-button-left'>
                            <button className={url === '/' ? 'top-button-wht header-right-button' : 'top-button-blk header-right-button'}>
                                List a Business
                            </button>
                        </NavLink>
                        <NavLink to='/writeareview' className='navbar-button-right'>
                            <button className={url === '/' ? 'top-button-wht header-right-button' : 'top-button-blk header-right-button'}>
                                Write a Review
                            </button>
                        </NavLink>
                        <div className='user-icon-container'>
                            <img className='user-icon' src={userIcon} alt='user' />
                        </div>
                    </div>
                </div>
            </div>
            <div className='header-bottom-portion'>

            </div>
        </div>
    )
}

export default NavBar;
