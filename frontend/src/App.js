import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import HomeTrade from "./components/HomeTrade";
import CartPage from "./components/CartPage";
import ProductsAdd from "./components/ProductsAdd";
import './css/HomeTrade.css';
import './css/CartPage.css';
import './css/ProductsAdd.css';

export default function App() {
  return (
    <>
      <Router>
         <Routes>
            <Route path="/" element={<HomeTrade />} />
            <Route path="/checkout" element={<CartPage />} />
            <Route path="/products/add" element={<ProductsAdd />} />
         </Routes>
      </Router>
    </>
  );
}