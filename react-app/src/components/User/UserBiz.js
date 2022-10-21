import { NavLink } from "react-router-dom";
import { useDispatch } from "react-redux";
import './UserBiz.css'
import picture from '../../icons/user-page-icons/picture.svg';
import pencil from '../../icons/user-page-icons/pencil.svg';
import trash from '../../icons/user-page-icons/trash.svg';
import x from '../../icons/x.svg';
import * as bizActions from "../../store/businesses";



export default function UserBiz({ user, userBizzes }) {
    const dispatch = useDispatch();

    const deleteBizHandler = (bizId) => {
        try {
            dispatch(bizActions.removeBiz(bizId));
        }

        catch (res) {
            const data = res.json();
            if (data) console.log(data);
        }
    }

    const deleteImgHandler = (bizId, imgId) => {
        try {
            dispatch(bizActions.deleteImg(bizId, imgId));
        }

        catch (res) {
            const data = res.json();
            if (data) console.log(data);
        }
    }


    if (!userBizzes || !Object.values(userBizzes).length) {
        return (
            <div>
                <h2 id='mid-title'>Businesses</h2>
                <div>You haven't listed any businesses yet.</div>
            </div>
        )
    }

    else return (
        <div>
            <h2 id='mid-title'>Businesses</h2>
            <div className="all-user-reviews">
                {userBizzes && Object.values(userBizzes).map(biz => (
                    <div className="single-user-biz-card" key={biz.id}>
                        <div className="user-biz-info">
                            <NavLink exact to={`/biz/${biz.id}`}>
                                <img className="user-biz-prev-img" src={biz.Business_Images[0].url} alt={biz.name} />
                            </NavLink>
                            <div className="user-biz-text">
                                <NavLink className="user-biz-link" exact to={`/biz/${biz.id}`}>
                                    <div className="user-biz-name">{biz.name}</div>
                                </NavLink>
                                <div className="user-biz-price-range">{biz.price_range}</div>
                                <div className="user-biz-address">{biz.address}</div>
                                <div className="user-biz-city-state-zip">
                                    <span className="user-biz-city">{biz.city},</span>
                                    <span className="user-biz-state">{biz.state}</span>
                                    <span className="user-biz-zip">{biz.zipcode}</span>
                                </div>
                            </div>
                        </div>
                        <div className="user-biz-rating-imgs">
                            <div className="user-biz-rating-rev-count">
                                <div className="user-biz-rating">
                                    {/* FIRST STAR */}
                                    <svg className='first-star' width="20" height="20" viewBox="0 0 20 20">
                                        <path fill={biz.avg_rating >= 4.8 ? "rgba(251,67,60,1)" : biz.avg_rating >= 4.3 ? 'rgba(255, 100, 61, 1)' : biz.avg_rating >= 3.8 ? 'rgba(255, 100, 61, 1)' : biz.avg_rating >= 3.3 ? 'rgba(255, 135, 66, 1)' : biz.avg_rating >= 2.8 ? 'rgba(255, 135, 66, 1)' : biz.avg_rating >= 2.3 ? 'rgba(255, 173, 72, 1)' : biz.avg_rating >= 1.8 ? 'rgba(255, 173, 72, 1)' : biz.avg_rating >= 1.3 ? 'rgba(255, 204, 75, 1)' : biz.avg_rating > 0 ? 'rgba(255, 204, 75, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                            d="M0 4C0 1.79086 1.79086 0 4 0H10V20H4C1.79086 20 0 18.2091 0 16V4Z">
                                        </path>
                                        <path fill={biz.avg_rating >= 4.8 ? "rgba(251,67,60,1)" : biz.avg_rating >= 4.3 ? 'rgba(255, 100, 61, 1)' : biz.avg_rating >= 3.8 ? 'rgba(255, 100, 61, 1)' : biz.avg_rating >= 3.3 ? 'rgba(255, 135, 66, 1)' : biz.avg_rating >= 2.8 ? 'rgba(255, 135, 66, 1)' : biz.avg_rating >= 2.3 ? 'rgba(255, 173, 72, 1)' : biz.avg_rating >= 1.8 ? 'rgba(255, 173, 72, 1)' : biz.avg_rating >= 1.3 ? 'rgba(255, 204, 75, 1)' : biz.avg_rating > 0 ? 'rgba(255, 204, 75, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                            d="M20 4C20 1.79086 18.2091 0 16 0H10V20H16C18.2091 20 20 18.2091 20 16V4Z">
                                        </path>
                                        <path fill="white" fillRule="evenodd" clipRule="evenodd"
                                            d="M10 13.3736L12.5949 14.7111C12.7378 14.7848 12.9006 14.8106 13.0593
                                            14.7847C13.4681 14.718 13.7454 14.3325 13.6787 13.9237L13.2085 11.0425L15.2824
                                            8.98796C15.3967 8.8748 15.4715 8.72792 15.4959 8.569C15.5588 8.15958 15.2779
                                            7.77672 14.8685 7.71384L11.983 7.2707L10.6699 4.66338C10.5975 4.51978 10.481
                                            4.40322 10.3374 4.33089C9.96742 4.14458 9.51648 4.29344 9.33017 4.66338L8.01705
                                            7.2707L5.13157 7.71384C4.97265 7.73825 4.82577 7.81309 4.71261 7.92731C4.42109
                                            8.22158 4.42332 8.69645 4.71759 8.98796L6.79152 11.0425L6.32131 13.9237C6.29541
                                            14.0824 6.3212 14.2452 6.39486 14.3881C6.58464 14.7563 7.03696 14.9009 7.40514
                                            14.7111L10 13.3736Z">
                                        </path>
                                    </svg>
                                    {/* SECOND STAR */}
                                    <svg className='middle-star' width="20" height="20" viewBox="0 0 20 20">
                                        <path fill={biz.avg_rating >= 4.8 ? "rgba(251,67,60,1)" : biz.avg_rating >= 4.3 ? 'rgba(255, 100, 61, 1)' : biz.avg_rating >= 3.8 ? 'rgba(255, 100, 61, 1)' : biz.avg_rating >= 3.3 ? 'rgba(255, 135, 66, 1)' : biz.avg_rating >= 2.8 ? 'rgba(255, 135, 66, 1)' : biz.avg_rating >= 2.3 ? 'rgba(255, 173, 72, 1)' : biz.avg_rating >= 1.8 ? 'rgba(255, 173, 72, 1)' : biz.avg_rating >= 1.3 ? 'rgba(255, 204, 75, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                            d="M0 4C0 1.79086 1.79086 0 4 0H10V20H4C1.79086 20 0 18.2091 0 16V4Z">
                                        </path>
                                        <path fill={biz.avg_rating >= 4.8 ? "rgba(251,67,60,1)" : biz.avg_rating >= 4.3 ? 'rgba(255, 100, 61, 1)' : biz.avg_rating >= 3.8 ? 'rgba(255, 100, 61, 1)' : biz.avg_rating >= 3.3 ? 'rgba(255, 135, 66, 1)' : biz.avg_rating >= 2.8 ? 'rgba(255, 135, 66, 1)' : biz.avg_rating >= 2.3 ? 'rgba(255, 173, 72, 1)' : biz.avg_rating >= 1.8 ? 'rgba(255, 173, 72, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                            d="M20 4C20 1.79086 18.2091 0 16 0H10V20H16C18.2091 20 20 18.2091 20 16V4Z">
                                        </path>
                                        <path fill="white" fillRule="evenodd" clipRule="evenodd"
                                            d="M10 13.3736L12.5949 14.7111C12.7378 14.7848 12.9006 14.8106 13.0593
                                            14.7847C13.4681 14.718 13.7454 14.3325 13.6787 13.9237L13.2085 11.0425L15.2824
                                            8.98796C15.3967 8.8748 15.4715 8.72792 15.4959 8.569C15.5588 8.15958 15.2779
                                            7.77672 14.8685 7.71384L11.983 7.2707L10.6699 4.66338C10.5975 4.51978 10.481
                                            4.40322 10.3374 4.33089C9.96742 4.14458 9.51648 4.29344 9.33017 4.66338L8.01705
                                            7.2707L5.13157 7.71384C4.97265 7.73825 4.82577 7.81309 4.71261 7.92731C4.42109
                                            8.22158 4.42332 8.69645 4.71759 8.98796L6.79152 11.0425L6.32131 13.9237C6.29541
                                            14.0824 6.3212 14.2452 6.39486 14.3881C6.58464 14.7563 7.03696 14.9009 7.40514
                                            14.7111L10 13.3736Z">
                                        </path>
                                    </svg>
                                    {/* THIRD STAR */}
                                    <svg className='middle-star' width="20" height="20" viewBox="0 0 20 20">
                                        <path fill={biz.avg_rating >= 4.8 ? "rgba(251,67,60,1)" : biz.avg_rating >= 4.3 ? 'rgba(255, 100, 61, 1)' : biz.avg_rating >= 3.8 ? 'rgba(255, 100, 61, 1)' : biz.avg_rating >= 3.3 ? 'rgba(255, 135, 66, 1)' : biz.avg_rating >= 2.8 ? 'rgba(255, 135, 66, 1)' : biz.avg_rating >= 2.3 ? 'rgba(255, 173, 72, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                            d="M0 4C0 1.79086 1.79086 0 4 0H10V20H4C1.79086 20 0 18.2091 0 16V4Z">
                                        </path>
                                        <path fill={biz.avg_rating >= 4.8 ? "rgba(251,67,60,1)" : biz.avg_rating >= 4.3 ? 'rgba(255, 100, 61, 1)' : biz.avg_rating >= 3.8 ? 'rgba(255, 100, 61, 1)' : biz.avg_rating >= 3.3 ? 'rgba(255, 135, 66, 1)' : biz.avg_rating >= 2.8 ? 'rgba(255, 135, 66, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                            d="M20 4C20 1.79086 18.2091 0 16 0H10V20H16C18.2091 20 20 18.2091 20 16V4Z">
                                        </path>
                                        <path fill="white" fillRule="evenodd" clipRule="evenodd"
                                            d="M10 13.3736L12.5949 14.7111C12.7378 14.7848 12.9006 14.8106 13.0593
                                            14.7847C13.4681 14.718 13.7454 14.3325 13.6787 13.9237L13.2085 11.0425L15.2824
                                            8.98796C15.3967 8.8748 15.4715 8.72792 15.4959 8.569C15.5588 8.15958 15.2779
                                            7.77672 14.8685 7.71384L11.983 7.2707L10.6699 4.66338C10.5975 4.51978 10.481
                                            4.40322 10.3374 4.33089C9.96742 4.14458 9.51648 4.29344 9.33017 4.66338L8.01705
                                            7.2707L5.13157 7.71384C4.97265 7.73825 4.82577 7.81309 4.71261 7.92731C4.42109
                                            8.22158 4.42332 8.69645 4.71759 8.98796L6.79152 11.0425L6.32131 13.9237C6.29541
                                            14.0824 6.3212 14.2452 6.39486 14.3881C6.58464 14.7563 7.03696 14.9009 7.40514
                                            14.7111L10 13.3736Z">
                                        </path>
                                    </svg>
                                    {/* FOURTH STAR */}
                                    <svg className='middle-star' width="20" height="20" viewBox="0 0 20 20">
                                        <path fill={biz.avg_rating >= 4.8 ? "rgba(251,67,60,1)" : biz.avg_rating >= 4.3 ? 'rgba(255, 100, 61, 1)' : biz.avg_rating >= 3.8 ? 'rgba(255, 100, 61, 1)' : biz.avg_rating >= 3.3 ? 'rgba(255, 135, 66, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                            d="M0 4C0 1.79086 1.79086 0 4 0H10V20H4C1.79086 20 0 18.2091 0 16V4Z">
                                        </path>
                                        <path fill={biz.avg_rating >= 4.8 ? "rgba(251,67,60,1)" : biz.avg_rating >= 4.3 ? 'rgba(255, 100, 61, 1)' : biz.avg_rating >= 3.8 ? 'rgba(255, 100, 61, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                            d="M20 4C20 1.79086 18.2091 0 16 0H10V20H16C18.2091 20 20 18.2091 20 16V4Z">
                                        </path>
                                        <path fill="white" fillRule="evenodd" clipRule="evenodd"
                                            d="M10 13.3736L12.5949 14.7111C12.7378 14.7848 12.9006 14.8106 13.0593
                                            14.7847C13.4681 14.718 13.7454 14.3325 13.6787 13.9237L13.2085 11.0425L15.2824
                                            8.98796C15.3967 8.8748 15.4715 8.72792 15.4959 8.569C15.5588 8.15958 15.2779
                                            7.77672 14.8685 7.71384L11.983 7.2707L10.6699 4.66338C10.5975 4.51978 10.481
                                            4.40322 10.3374 4.33089C9.96742 4.14458 9.51648 4.29344 9.33017 4.66338L8.01705
                                            7.2707L5.13157 7.71384C4.97265 7.73825 4.82577 7.81309 4.71261 7.92731C4.42109
                                            8.22158 4.42332 8.69645 4.71759 8.98796L6.79152 11.0425L6.32131 13.9237C6.29541
                                            14.0824 6.3212 14.2452 6.39486 14.3881C6.58464 14.7563 7.03696 14.9009 7.40514
                                            14.7111L10 13.3736Z">
                                        </path>
                                    </svg>
                                    {/* FIFTH STAR */}
                                    <svg className='last-star' width="20" height="20" viewBox="0 0 20 20">
                                        <path fill={biz.avg_rating >= 4.8 ? "rgba(251,67,60,1)" : biz.avg_rating >= 4.3 ? 'rgba(255, 100, 61, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                            d="M0 4C0 1.79086 1.79086 0 4 0H10V20H4C1.79086 20 0 18.2091 0 16V4Z">
                                        </path>
                                        <path fill={biz.avg_rating >= 4.8 ? "rgba(251,67,60,1)" : 'rgba(187, 186, 192, 0.5)'}
                                            d="M20 4C20 1.79086 18.2091 0 16 0H10V20H16C18.2091 20 20 18.2091 20 16V4Z">
                                        </path>
                                        <path fill="white" fillRule="evenodd" clipRule="evenodd"
                                            d="M10 13.3736L12.5949 14.7111C12.7378 14.7848 12.9006 14.8106 13.0593
                                            14.7847C13.4681 14.718 13.7454 14.3325 13.6787 13.9237L13.2085 11.0425L15.2824
                                            8.98796C15.3967 8.8748 15.4715 8.72792 15.4959 8.569C15.5588 8.15958 15.2779
                                            7.77672 14.8685 7.71384L11.983 7.2707L10.6699 4.66338C10.5975 4.51978 10.481
                                            4.40322 10.3374 4.33089C9.96742 4.14458 9.51648 4.29344 9.33017 4.66338L8.01705
                                            7.2707L5.13157 7.71384C4.97265 7.73825 4.82577 7.81309 4.71261 7.92731C4.42109
                                            8.22158 4.42332 8.69645 4.71759 8.98796L6.79152 11.0425L6.32131 13.9237C6.29541
                                            14.0824 6.3212 14.2452 6.39486 14.3881C6.58464 14.7563 7.03696 14.9009 7.40514
                                            14.7111L10 13.3736Z">
                                        </path>
                                    </svg>
                                </div>
                                <div className="user-biz-review-count">{`(${biz.Review_Count})`}</div>
                            </div>


                            <div className="user-biz-imgs">
                                {biz.Business_Images.length > 0 && biz.Business_Images.map(img => (
                                    <div className="user-biz-img-container" key={img.id} onClick={() => deleteImgHandler(biz.id, img.id)}>
                                        <img className="user-biz-svg-x" src={x} width='100px' alt="x_svg" />
                                        <img className="user-biz-img" key={img.id} src={img.url} alt={img.url} />
                                    </div>
                                ))}
                            </div>
                        </div>


                        <div className="user-biz-edit-delete-icons">
                            <NavLink className="user-biz-add-img-button" to={`/biz/${biz.id}/images/new`}>
                                <img className="user-biz-svg" src={picture} width='16px' alt="pic_svg" />
                            </NavLink>
                            <NavLink className="user-biz-edit-button" to={`/biz/${biz.id}/update`}>
                                <img className="user-biz-svg" src={pencil} width='16px' alt="pencil_svg" />
                            </NavLink>
                            <div className="user-biz-delete-button" onClick={() => deleteBizHandler(biz.id)}>
                                <img className="user-biz-svg" src={trash} width='16px' alt="trash_svg" />
                            </div>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    )

}
