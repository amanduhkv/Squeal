import { NavLink, useLocation } from 'react-router-dom';
import { useSelector } from 'react-redux';

import pigOutline from '../../icons/pig-outline.png'
import cam from '../../icons/user-page-icons/cam.png';
import upProf from '../../icons/user-page-icons/prof-up.png'
import pig from '../../icons/user-page-icons/pig-head.png';
import starGrey from '../../icons/user-page-icons/star-grey.png';
import starOran from '../../icons/user-page-icons/star-oran.png';
import savedBiz from '../../icons/user-page-icons/save.png';
import './UserPage.css';

const UserPage = () => {
  const url = useLocation().pathname;
  const user = useSelector(state => state.session.user);

  let lastName = user.last_name.split('')
  let lastInitial = lastName[0];

  return (
    <>
      <div id='bckgrd'></div>
      <div className='user-prof'>
        <div id='left-col'>
          <button id='user-img'>
            <img id='pig-outline' src={user.profile_pic ? user.profile_pic : pigOutline} alt='pig-outline' width='100%' height='100%' />
          </button>
          <h3 id='bar-name'>{user.first_name}'s Profile</h3>
          <div className='side-bar'>
            {/* -----------------------OVERVIEW--------------------- */}
            <NavLink to='/current' id='bar-row'>
              <img id='bar-img' src={pig} alt='pig' width='25px' />
              <div id='bar-txt'>Profile Overview</div>
            </NavLink>
            {/* -----------------------REVIEWS--------------------- */}
            <NavLink to='/reviews/current' id='bar-row'>
              <img id='bar-img' src={starGrey} alt='star-grey' width='25px' />
              <div id='bar-txt'>Reviews</div>
            </NavLink>
            {/* -----------------------BIZ--------------------- */}
            <NavLink to='/biz/current' id='bar-row'>
              <img id='bar-img' src={savedBiz} alt='star-grey' width='25px' />
              <div id='bar-txt'>Saved Businesses</div>
            </NavLink>
          </div>
        </div>
        <div id='mid-col'>
          <div className='user-info'>
            <h1 id='user-name'>{user.first_name} {lastInitial}.</h1>
            <p id='user-loc'>From City, State</p>
            <div className='user-icons'>
              <div id='user-rev'>
                <img src={starOran} alt='star' />
                <p id='user-txt'>Review</p>
              </div>
              <div id='user-pht'>
                <img src={cam} alt='cam' width='24px' />
                <p id='user-txt'>Photos</p>
              </div>
            </div>
          </div>
          <br></br>
          <br></br>
          {url === '/current' && (
          <div>
            <h2 id='mid-title-over'>Recent Activity</h2>
          </div>
          )}
          {url === '/reviews/current' && (
          <div>
            <h2 id='mid-title'>Reviews</h2>
          </div>
          )}
        </div>
        <div id='right-col'>
          <div id='top-rc'>
            {/* <h5 id='top-rc-text'>
              <img src={blueCam} alt='add-prof-img' width='15px' />
              Add Profile Photo
            </h5> */}
            <h5 id='top-rc-text'>
              <img src={upProf} alt='up-prof' width='15px' />
              Update Your Profile
            </h5>
          </div>
          {url === '/current' && (
          <div id='bot-rc'>
            <div id='title-bot'>About {user.first_name} {lastInitial}.</div>
            <h5 id='bot-rc-title'>Stats</h5>
            <div id='bot-rc-1'>
              <img src={savedBiz} alt='save' width='16px' height='16px' />
              <p id='bot-rc-txt'>
                Saved Businesses (#)
              </p>
            </div>
            <h5 id='bot-rc-title'>Location</h5>
            <div id='bot-rc-1'>
            </div>
            <h5 id='bot-rc-title'>Squealing Since</h5>
            <div id='bot-rc-1'>
            </div>
          </div>
          )}
        </div>
      </div>
    </>
  )
}

export default UserPage
