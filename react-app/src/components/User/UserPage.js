import pigOutline from '../../icons/pig-outline.png'
import cam from '../../icons/user-page-icons/cam.png';
import upProf from '../../icons/user-page-icons/prof-up.png'
import pig from '../../icons/user-page-icons/pig-head.png';
import starGrey from '../../icons/user-page-icons/star-grey.png';
import savedBiz from '../../icons/user-page-icons/save.png';
import './UserPage.css';

const UserPage = () => {
  return (
    <>
      <div id='bckgrd'></div>
      <div className='user-prof'>
        <div id='left-col'>
          <button id='user-img'>
            <img id='pig-outline' src={pigOutline} alt='pig-outline' width='130px' />
          </button>
          <h3 id='bar-name'>Name's Profile</h3>
          <div className='side-bar'>
            <div id='bar-row'>
              <img id='bar-img' src={pig} alt='pig' width='25px' />
              <div id='bar-txt'>Profile Overview</div>
            </div>
            <div id='bar-row'>
              <img id='bar-img' src={starGrey} alt='star-grey' width='25px' />
              <div id='bar-txt'>Reviews</div>
            </div>
            <div id='bar-row'>
              <img id='bar-img' src={savedBiz} alt='star-grey' width='25px' />
              <div id='bar-txt'>Saved Businesses</div>
            </div>
          </div>
        </div>
        <div id='mid-col'>
          <div>
            <h1>(First) (LastIn.)</h1>
            <h2>From (City, State)</h2>
            <div>
              <img src={cam} alt='cam' width='25px' />
              Review
            </div>
          </div>

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
          <div id='bot-rc'>

          </div>
        </div>
      </div>
    </>
  )
}

export default UserPage
