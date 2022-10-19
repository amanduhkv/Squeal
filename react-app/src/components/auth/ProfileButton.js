import React, { useState, useEffect } from "react";
import { useSelector } from 'react-redux';
import { NavLink } from "react-router-dom";

import LogoutButton from "./LogoutButton";
import userIcon from '../../icons/user-pig.png'
import aboutPig from '../../icons/about-pig.png'
import bizPig from '../../icons/biz-pig.png'
import reviewPig from '../../icons/review-pig.png'
import './ProfileButton.css'

function ProfileButton() {
  const user = useSelector(state => state.session.user)
  const [showMenu, setShowMenu] = useState(false);
  // console.log('this is the user',user)
  const openMenu = () => {
    if (showMenu) return;
    setShowMenu(true);
  };

  useEffect(() => {
    if (!showMenu) return;

    const closeMenu = () => {
      setShowMenu(false);
    };

    document.addEventListener('click', closeMenu);

    return () => document.removeEventListener("click", closeMenu);
  }, [showMenu]);


  return (
    <>
    <div className='profile-button tooltip-profile' onClick={openMenu}>
      <img className='user-icon' src={userIcon} alt='user' />
      {/* <div id='hover-dropdown-name'>{user}</div> */}
      <div className="tooltiptext-below-user">
        {user.first_name} {user.last_name[0]}.
      </div>
    </div>
      {showMenu && (
        <div className="profile-dropdown">
          <div >
            <NavLink id='dropdown-text' to='/current'>
              <img src={aboutPig} alt='about-pig' id='about' width='30px'/>
              About Me
            </NavLink>
          </div>
          <div>
            <NavLink id='dropdown-text-b' to='/biz/current'>
              <img src={bizPig} alt='pig' width='35px' />
              My Businesses
            </NavLink>
          </div>
          <div>
            <NavLink id='dropdown-text-b' to='/reviews/current'>
              <img src={reviewPig} alt='pig' width='35px' />
              My Reviews
            </NavLink>
          </div>

          <div id='logout'>
            <img src='https://www.svgrepo.com/show/115080/logout.svg' alt='exit' width='20px' />
            <LogoutButton />
          </div>
        </div>
      )}
    </>
  );
}

export default ProfileButton;
