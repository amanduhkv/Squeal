import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getAllBiz } from '../../store/businesses';

import x from '../../icons/all-biz-page/x.svg';
import check from '../../icons/all-biz-page/check.svg';
import txtbub from '../../icons/all-biz-page/text-bubble.svg';
import './Biz.css';

export default function Biz() {
    const biz = useSelector(state => state.businesses.allBusinesses);

    const bizArr = Object.values(biz);
    const dispatch = useDispatch();

    // const reviews = useSelector(state => state.reviews.business)

    let current_time;
    const settingTime = () => {
        const today = new Date();
        let hours = today.getHours().toString()
        let mins = today.getMinutes().toString()
        if (hours.length === 1) hours = "0" + hours;
        if (mins.length === 1) mins = "0" + mins;
        return hours + mins
    }
    current_time = settingTime()

    useEffect(() => {
        dispatch(getAllBiz())
    }, [dispatch])

    return (
        <main>
            <br></br>
            <br></br>
            <br></br>
            <h1>Best Type Near Me in City, State</h1>
            <ol>
                {bizArr.map(biz => (
                    <div className="biz-box">
                        <div className="img-box">

                        </div>
                        <div className="biz-info-box">
                            <li id='biz-title'>
                                {biz.name}
                            </li>
                            <div id='biz-rev-info'>
                                <div id='rev-stars'>
                                    Review Logic Here
                                </div>
                                <div id='rev-rating'>
                                    {biz.avg_rating}
                                </div>
                                <div id='biz-text-rev'>
                                    (# reviews)
                                </div>
                            </div>
                            <div id='biz-type-loc'>
                                <div id='biz-type-butts'>
                                    {Object.values(biz.types).map(type => (
                                        <button>
                                            {type.type}
                                        </button>
                                    ))}
                                </div>
                                <div id='biz-price'>
                                    {biz.price_range}
                                </div>
                            </div>
                            <div id='biz-hours'>
                                {current_time > biz.start_time && current_time < biz.end_time ?
                                    (<div id='biz-open'>Open</div>) : (<div id='biz-closed'>Closed</div>)
                                }
                            </div>
                            <div id='biz-rev'>
                                <img src={txtbub} alt='txtbubble' />
                                <div>"Review Text goes here"</div>
                            </div>
                            <div id='biz-tras'>

                                <div>
                                    {Object.values(biz.transactions).map(tra => (
                                        <span>
                                            <img src={check} alt='checkmark' width='16px' height='10px' />
                                            {tra.transaction}
                                        </span>
                                    ))}
                                </div>
                            </div>
                        </div>

                    </div>
                ))}
            </ol>
        </main>
    )
}
