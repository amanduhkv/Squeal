import pigOutline from '../../icons/pig-outline.png'
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
        <div id='mid-col'>mid</div>
        <div id='right-col'>right</div>
      </div>
    </>
  )
}

export default UserPage
