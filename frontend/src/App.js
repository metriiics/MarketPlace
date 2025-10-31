import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import HomeTrade from "./components/HomeTrade";
import CartPage from "./components/CartPage";
import './css/HomeTrade.css';
import './css/CartPage.css';

export default function App() {
  return (
    <>
      <Router>
         <Routes>
            <Route path="/" element={<HomeTrade />} />
            <Route path="/checkout" element={<CartPage />} />
  
         </Routes>
      </Router>
    </>
  );
}