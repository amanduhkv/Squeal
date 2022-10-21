import chefPig from '../../icons/chef-pig.png'
import './ErrorPage.css'

function ErrorPage() {
    return (
        <div id='error-page'>
            <img id='chef-pig' src={chefPig} alt='chef-pig' width='300px' />
            <div id='error-text'>
                <h2 id='cooking'>This page is still being cooked up.</h2>
                <h4 id='apologies'>We apologize for the inconvenience.</h4>
            </div>
        </div>
    )
}

export default ErrorPage
