// import { useDispatch, useSelector } from "react-redux";
// import { useEffect } from "react";

// import { getAllBiz } from '../../store/businesses';

// export function BizToFront() {
//   const biz = useSelector(state => state.businesses.allBusinesses);
//   const bizArr = Object.values(biz);
//   const dispatch = useDispatch();
//   const bizNames = [];

//   useEffect(() => {
//     dispatch(getAllBiz())
//   }, [dispatch])

//   bizArr.map(biz => bizNames.push(biz.name))
//   return bizNames;
// }
