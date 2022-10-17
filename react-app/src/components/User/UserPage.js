import pigOutline from '../../icons/pig-outline.png'
import blueCam from '../../icons/userpage-icons/cam-up.png';
import upProf from '../../icons/userpage-icons/prof-up.png'
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
          <h3>Name's Profile</h3>
        </div>
        <div id='mid-col'>
          <div>
            <h1>(First) (LastIn.)</h1>
            <h2>From (City, State)</h2>
            <div>
              {/* <img src={} alt='cam-ora' */}
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
