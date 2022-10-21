import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { NavLink, useLocation } from "react-router-dom";
import ReactPaginate from 'react-paginate';
import FuzzySearch from 'fuzzy-search';
import { search, clearData } from "../../store/businesses";
import { getAllBiz } from '../../store/businesses';

import x from '../../icons/all-biz-page/x.svg';
import check from '../../icons/all-biz-page/check.svg';
import txtbub from '../../icons/all-biz-page/text-bubble.svg';

import './Biz.css';

export default function Search({ data }) {
  const biz = useSelector(state => state.businesses.allBusinesses);
  const bizArr = Object.values(biz);

  const dispatch = useDispatch();

  const [priceArr, setPriceArr] = useState([]);
  const [price1, setPrice1] = useState(false);
  const [price2, setPrice2] = useState(false);
  const [price3, setPrice3] = useState(false);
  const [price4, setPrice4] = useState(false);
  const [activePrice, setActivePrice] = useState(false);
  const [activeOpen, setActiveOpen] = useState(false);
  const [activeDel, setActiveDel] = useState(false);
  const [activeTakeout, setActiveTakeout] = useState(false);
  const [activeRes, setActiveRes] = useState(false);
  const [activeAll, setActiveAll] = useState(false);
  const [showMenu, setShowMenu] = useState(false);

  const [pageNum, setPageNum] = useState(0);
  const [query, setQuery] = useState('');
  const searchStuff = useLocation().search;
  console.log('BIZARR', bizArr)
  // console.log('this is searchStuff', searchStuff);
  let cat;
  let location;

  // console.log('this is the data', data)

  /* ----------price dropdown logic---------- */
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


  /* -------USE EFFECT:get all bizzies------- */

  if (searchStuff) {
    cat = searchStuff.split('?type=').join('').split('&')[0];
    location = searchStuff.split('&loc=')[1];
    // console.log('heres my cat',cat)
  }

  useEffect(() => {
    if (location) dispatch(getAllBiz(location))
    else dispatch(getAllBiz())
  }, [dispatch])


  /* ------------SEARCH FXNS/LOGIC------------ */
  const searchFunc = new FuzzySearch(bizArr, ['transactions.transaction', 'types.alias', 'name', 'Review.preview_review']);

  // const res = searchFunc.search(query)


  let res = searchFunc.search(cat ?? query)
  //   console.log('using search', res)

  const handleSubmit = (e) => {
    e.preventDefault();
    dispatch(search(res))
    clearData()
    // console.log('SUCCESS')
  }

  if (priceArr.length) res = res.filter(biz => priceArr.includes(biz.price_range))

  /* -------------TIME FXNS/LOGIC------------- */
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

  const time_conversion = (time) => {
    if (Number(time) === 1200) time = 1200
    if (Number(time) === 0) time = 2400
    if (Number(time) > 1200) {
      time = time - 1200
    }
    let nums = time.toString().split('')

    if (nums.length === 3) return nums[0] + ':' + nums[1] + nums[2]
    if (nums.length === 4) return nums[0] + nums[1] + ':' + nums[2] + nums[3]
  }
  // console.log('TIME', time_conversion(2400))

  /* ------------TOGGLE FXNS/LOGIC------------ */

  const toggleIdPrice = () => {
    setActivePrice(!activePrice);
    openMenu();
  }
  // const toggleIdOpen = () => {
  //   setActiveOpen(!activeOpen);
  //   if(activeOpen) {
  //     if(activePrice) setActiveDel(!activePrice)
  //     if(activeDel) setActiveDel(!activeDel)
  //     if(activeTakeout) setActiveDel(!activeTakeout)
  //     if(activeRes) setActiveDel(!activeRes)
  //   }
  // }
  const toggleIdDel = () => {
    setActiveDel(!activeDel);
  }
  const toggleIdTakeout = () => {
    setActiveTakeout(!activeTakeout);
  }
  const toggleIdRes = () => {
    setActiveRes(!activeRes);
  }
  const toggleIdAll = () => {
    setActiveAll(!activeAll);
  }

  useEffect(() => {
    // console.log('hitting useEffect for Del')

    if (activeDel) {
      if (activePrice) setActivePrice(false);
      if (activeOpen) setActiveOpen(false);
      if (activeTakeout) setActiveTakeout(false);
      if (activeRes) setActiveRes(false);
      if (activeAll) setActiveAll(false);
    }

  }, [activeDel]);
  useEffect(() => {
    // console.log('hitting useEffect for Takeout')

    if (activeTakeout) {
      if (activePrice) setActivePrice(false);
      if (activeOpen) setActiveOpen(false);
      if (activeDel) setActiveDel(false);
      if (activeRes) setActiveRes(false);
      if (activeAll) setActiveAll(false);
    }

  }, [activeTakeout]);
  useEffect(() => {
    // console.log('hitting useEffect for Res')

    if (activeRes) {
      if (activePrice) setActivePrice(false);
      if (activeOpen) setActiveOpen(false);
      if (activeDel) setActiveDel(false);
      if (activeTakeout) setActiveTakeout(false);
      if (activeAll) setActiveAll(false);
    }
  }, [activeRes]);
  useEffect(() => {
    if (activeAll) {
      if (activePrice) setActivePrice(false);
      if (activeOpen) setActiveOpen(false);
      if (activeDel) setActiveDel(false);
      if (activeTakeout) setActiveTakeout(false);
      if (activeRes) setActiveRes(false);
    }
  }, [activeAll]);



  let title;
  if (query) title = query[0].toUpperCase() + query.substring(1)
  // console.log('CURRENT TITLE: ', title)
  if (title === 'Restaurant_reservation') title = 'Reservations'
  else title = title




  /* ----------PAGINATION FXNS/LOGIC---------- */
  const bizPerPage = 10;
  const visitedPages = pageNum * bizPerPage;
  const pageCount = Math.ceil(res.length / bizPerPage);

  const pageChange = ({ selected }) => {
    setPageNum(selected);
  }

  const bizzies = res.slice(visitedPages, visitedPages + bizPerPage)


  return (
    <div className="main">
      <form id='search-form' onSubmit={handleSubmit}>
        <input
          type='search'
          value={query}
          onChange={e => setQuery(e.target.value.toLowerCase())}
        />
        <button type='submit'>Submit</button>
      </form>

      <h1 className="allbiz-title">Best {query ? title : "Food"} Near Me</h1>

      <ol id='biz-list' start={(10 * pageNum) + 1}>
        <div className="types-buttons">
          <span id='price-dropdown'>

            <button
              id={activePrice ? 'type-butt-price-act' : 'type-butt'}
              onClick={() => {
                toggleIdPrice()
              }
              }
            >
              Price
              <svg width='12' height='12'><path d="M 8 10.25 a 0.746 0.746 0 0 1 -0.525 -0.215 l -3.055 -3 a 0.75 0.75 0 0 1 1.05 -1.07 L 8 8.449 l 2.53 -2.484 a 0.75 0.75 0 0 1 1.05 1.07 l -3.055 3 A 0.746 0.746 0 0 1 8 10.25 Z"></path></svg>
            </button>
            {showMenu && (
              <form id='dropdown-content'>
                <button id='dd-buttons'>
                  <input type='checkbox' id='$' checked={price1} onChange={() => {
                    setPrice1(!price1)
                    if (priceArr.includes('$')) {
                      const i = priceArr.indexOf("$")
                      setPriceArr([...priceArr.slice(0, i), ...priceArr.slice(i + 1)])
                    }
                    else {
                      setPriceArr([...priceArr, "$"])
                    }
                  }} />
                  <label for='$'>$</label>
                </button>
                <button id='dd-buttons'>
                  <input type='checkbox' id='$$' checked={price2} onChange={() => {
                    setPrice2(!price2)
                    if (priceArr.includes('$$')) {
                      const i = priceArr.indexOf("$$")
                      setPriceArr([...priceArr.slice(0, i), ...priceArr.slice(i + 1)])
                    }
                    else {
                      setPriceArr([...priceArr, "$$"])
                    }
                    setPageNum(0);
                  }} />
                  <label for='$$'>$$</label>
                </button>
                <button id='dd-buttons'>
                  <input type='checkbox' id='$$$' checked={price3} onChange={() => {
                    setPrice3(!price3)
                    if (priceArr.includes('$$$')) {
                      const i = priceArr.indexOf("$$$")
                      setPriceArr([...priceArr.slice(0, i), ...priceArr.slice(i + 1)])
                    }
                    else {
                      setPriceArr([...priceArr, "$$$"])
                    }
                    setPageNum(0);
                  }} />
                  <label for='$$$'>$$$</label>
                </button>
                <button id='dd-buttons'>
                  <input type='checkbox' id='$$$$' checked={price4} onChange={() => {
                    setPrice4(!price4)
                    if (priceArr.includes('$$$$')) {
                      const i = priceArr.indexOf("$$$$")
                      setPriceArr([...priceArr.slice(0, i), ...priceArr.slice(i + 1)])
                    }
                    else {
                      setPriceArr([...priceArr, "$$$$"])
                    }
                    setPageNum(0);
                  }} />
                  <label for='$$$$'>$$$$</label>
                </button>
                {/* <button type='submit'>Save</button> */}
              </form>
            )}
          </span>

          {/* <NavLink to='/biz?type=open'>
            <button
              id={activeOpen ? 'type-butt-act' : 'type-butt'}
              value={query}
              type='submit'
              onClick={() => {
                toggleIdOpen()
                // setQuery();
                setPageNum(0);
              }
              }
            >
              Open Now
            </button>
          </NavLink> */}
          <NavLink to='/biz?type=delivery'>
            <button
              id={activeDel ? 'type-butt-act' : 'type-butt'}
              value={query}
              type='submit'
              onClick={() => {
                toggleIdDel()
                if (activeDel) {
                  if (activePrice) setActivePrice(false);
                  if (activeOpen) setActiveOpen(false);
                  if (activeTakeout) setActiveTakeout(false);
                  if (activeRes) setActiveRes(false);
                }
                setQuery('delivery')
                setPageNum(0);
              }
              }
            >
              Offers Delivery
            </button>
          </NavLink>
          <NavLink to='/biz?type=pickup'>
            <button
              id={activeTakeout ? 'type-butt-act' : 'type-butt'}
              value={query}
              type='submit'
              onClick={() => {
                toggleIdTakeout()
                if (activeTakeout) {
                  if (activePrice) setActivePrice(false);
                  if (activeOpen) setActiveOpen(false);
                  if (activeDel) setActiveDel(false);
                  if (activeRes) setActiveRes(false);
                }
                setQuery('pickup')
                setPageNum(0);
              }
              }
            >
              Offers Takeout
            </button>
          </NavLink>
          <NavLink to='/biz?type=restaurant_reservation'>
            <button
              id={activeRes ? 'type-butt-act' : 'type-butt'}
              value={query}
              type='submit'
              onClick={() => {
                toggleIdRes()
                if (activeRes) {
                  if (activePrice) setActivePrice(false);
                  if (activeOpen) setActiveOpen(false);
                  if (activeDel) setActiveDel(false);
                  if (activeTakeout) setActiveTakeout(false);
                }
                setQuery('restaurant_reservation')
                setPageNum(0);
              }
              }
            >
              Reservations
            </button>
          </NavLink>
          <NavLink to='/biz'>
            <button
              id={activeAll ? 'type-butt-act' : 'type-butt'}
              value={query}
              onClick={() => {
                toggleIdAll()
                if (activeAll) {
                  if (activePrice) setActivePrice(false);
                  if (activeOpen) setActiveOpen(false);
                  if (activeDel) setActiveDel(false);
                  if (activeTakeout) setActiveTakeout(false);
                  if (activeRes) setActiveRes(false);
                }
                setQuery('')
                setPageNum(0);
              }
              }
            >
              All Businesses
            </button>
          </NavLink>
        </div>
        {bizzies.map(biz => (
          <div>
            {/* <NavLink className='search-biz' to={`/biz/${biz.id}`}>
              {biz.name}
            </NavLink> */}
            <NavLink
              className="biz-box"
              to={`/biz/${biz.id}`}
            >
              <div className="biz-img-box" >
                <img id='biz-img' src={biz.Business_Images[0].url} alt='biz-img' />
              </div>
              <div className="biz-info-box">
                <li key={biz.id} className="biz-title">
                  <NavLink id='biz-title-1' to={`/biz/${biz.id}`}>
                    {biz.name}
                  </NavLink>
                </li>
                <div id='biz-rev-info'>
                  <div id='rev-stars'>
                    <div className='review-card-stars'>
                      {/* FIRST STAR */}
                      <svg className='first-star' width="20" height="20" viewBox="0 0 20 20">
                        <path fill={biz.avg_rating >= 4.8 ? "rgba(251,67,60,1)" : biz.avg_rating >= 4.3 ? 'rgba(255, 100, 61, 1)' : biz.avg_rating >= 3.8 ? 'rgba(255, 100, 61, 1)' : biz.avg_rating >= 3.3 ? 'rgba(255, 135, 66, 1)' : biz.avg_rating >= 2.8 ? 'rgba(255, 135, 66, 1)' : biz.avg_rating >= 2.3 ? 'rgba(255, 173, 72, 1)' : biz.avg_rating >= 1.8 ? 'rgba(255, 173, 72, 1)' : biz.avg_rating >= 1.3 ? 'rgba(255, 204, 75, 1)' : 'rgba(255, 204, 75, 1)'}
                          d="M0 4C0 1.79086 1.79086 0 4 0H10V20H4C1.79086 20 0 18.2091 0 16V4Z">
                        </path>
                        <path fill={biz.avg_rating >= 4.8 ? "rgba(251,67,60,1)" : biz.avg_rating >= 4.3 ? 'rgba(255, 100, 61, 1)' : biz.avg_rating >= 3.8 ? 'rgba(255, 100, 61, 1)' : biz.avg_rating >= 3.3 ? 'rgba(255, 135, 66, 1)' : biz.avg_rating >= 2.8 ? 'rgba(255, 135, 66, 1)' : biz.avg_rating >= 2.3 ? 'rgba(255, 173, 72, 1)' : biz.avg_rating >= 1.8 ? 'rgba(255, 173, 72, 1)' : biz.avg_rating >= 1.3 ? 'rgba(255, 204, 75, 1)' : 'rgba(255, 204, 75, 1)'}
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
                  </div>
                  <div id='rev-rating'>
                    {biz.avg_rating}
                  </div>
                  <div id='biz-text-rev'>
                    ({biz.Review.review_length} reviews)
                  </div>
                </div>
                <div id='biz-type-loc'>
                  <div className='biz-type-butts-container'>
                    {Object.values(biz.types).map(type => (
                      <NavLink to={`/biz?type=${type.alias}`}
                        className='biz-type-butts'
                      >
                        {type.type}
                      </NavLink>
                    ))}
                  </div>
                  <div id='biz-price'>
                    {biz.price_range} • {biz.city}
                  </div>
                </div>
                {biz.start_time === biz.end_time ? (
                  <div id='biz-hours'>
                    <div id='biz-open'>Open All Day</div>
                  </div>
                ) :
                  (<div>
                    {biz.start_time !== biz.end_time && current_time > biz.start_time && current_time < biz.end_time ?
                      (<div id='biz-hours'>
                        <span id='biz-open'>Open</span>
                        <span id='biz-hours-1'>
                          until {time_conversion(biz.end_time)} {Number(biz.end_time) >= 1200 ? 'PM' : 'AM'}
                        </span>
                      </div>) :
                      (<div id='biz-hours'>
                        <span id='biz-closed'>Closed</span>
                        <span id='biz-hours-1'>
                          until {time_conversion(biz.start_time)} {Number(biz.start_time) >= 1200 ? 'PM' : 'AM'}
                        </span>
                      </div>)
                    }
                  </div>)
                }
                <div id='biz-rev'>
                  <img src={txtbub} alt='txtbubble' width='16px' height='14px' />
                  <div id='biz-rev-p'>
                    "{biz.Review.preview_review}"
                  </div>
                </div>
                <div id='biz-tras'>
                  <span id='tra-text'>
                    <img alt='tra-img' width='16px' height='10px' src={!!Object.values(biz.transactions).filter(ele =>
                      ele.transaction === 'pickup'
                    ).length ? check : x} /> Pickup
                  </span>
                  <span id='tra-text'>
                    <img alt='tra-img' width='16px' height='10px' src={!!Object.values(biz.transactions).filter(ele =>
                      ele.transaction === 'delivery'
                    ).length ? check : x} /> Delivery
                  </span>
                  <span id='tra-text'>
                    <img alt='tra-img' width='16px' height='10px' src={!!Object.values(biz.transactions).filter(ele =>
                      ele.transaction === 'restaurant_reservation'
                    ).length ? check : x} /> Reservations
                  </span>

                </div>
              </div>
            </NavLink>
          </div>
        ))}
      </ol>
      <div className={bizzies?.length ? "paginate-box" : "paginate-box-hide"}>
        <ReactPaginate
          breakLabel=''
          previousLabel={bizzies?.length ? "<" : ''}
          nextLabel={bizzies?.length ? '>' : ''}
          // previousLabel={'<'}
          // nextLabel={'>'}
          pageRangeDisplayed='9'
          marginPagesDisplayed=''
          pageCount={pageCount}
          onPageChange={pageChange}
          containerClassName='pagination-container'
          // activeClassName="pagination-active"
          activeLinkClassName="pagination-active"
          pageClassName="pag-num"
          pageLinkClassName='pag-txt'
          disabledLinkClassName='pag-hide'
          onPageActive={pageChange}
        />
        {pageCount && (
          <div id='paginate-count'>{pageNum + 1} of {pageCount}</div>
        )}
      </div>

    </div>
  )
}
