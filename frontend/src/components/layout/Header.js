import React, { useState } from 'react';
import { Link, useNavigate, useSearchParams } from 'react-router-dom';
import { Search, MapPin, ShoppingCart, User, Menu, Phone, Truck, RotateCcw, ShieldCheck } from 'lucide-react';
import { getUser, logout, isAuthenticated } from '../../utils/auth';
import './Header.css';

function Header() {
  const navigate = useNavigate();
  const [searchParams] = useSearchParams();
  const [searchQuery, setSearchQuery] = useState(searchParams.get('q') || '');
  const user = getUser();
  const authenticated = isAuthenticated();

  const handleLogout = () => {
    logout();
    navigate('/');
  };

  const handleSearch = (e) => {
    e.preventDefault();
    if (searchQuery.trim()) {
      navigate(`/?q=${encodeURIComponent(searchQuery.trim())}`);
    } else {
      navigate('/');
    }
  };

  return (
    <header className="header-wrapper">
      {/* Top Header */}
      <div className="top-header">
        <div className="container-lg top-header-inner">
          <Link to="#" className="top-header-link">Chính hãng - Xuất VAT đầy đủ</Link>
          <Link to="#" className="top-header-link"><Truck size={14} /> Giao nhanh - Miễn phí cho đơn 300k</Link>
          <Link to="#" className="top-header-link"><RotateCcw size={14} /> Thu cũ giá ngon - Lên đời tiết kiệm</Link>
          <Link to="#" className="top-header-link"><ShieldCheck size={14} /> Cửa hàng gần bạn</Link>
          <Link to="#" className="top-header-link">Tra cứu đơn hàng</Link>
          <Link to="#" className="top-header-link"><Phone size={14} /> 1800 2097</Link>
        </div>
      </div>

      {/* Main Header */}
      <div className="main-header">
        <div className="container-lg main-header-inner">
          {/* Logo */}
          <Link to="/" className="header-logo">
            cellphone<span>S</span>
          </Link>

          {/* Category Button */}
          <button className="category-btn">
            <Menu size={20} />
            Danh mục
          </button>

          {/* Location Button */}
          <button className="location-btn">
            <MapPin size={18} />
            Hồ Chí Minh
          </button>

          {/* Search */}
          <form className="search-container" onSubmit={handleSearch}>
            <Search size={18} className="search-icon-header" />
            <input
              type="text"
              className="search-input-header"
              placeholder="Bạn muốn mua gì hôm nay?"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
            />
          </form>

          {/* Call to Action Buttons */}
          <div className="header-actions">
            {authenticated && user && user.role === 'customer' ? (
              <Link to="/customer/dashboard" className="header-action-btn">
                <ShoppingCart size={24} />
                Giỏ hàng
              </Link>
            ) : (
              <Link to="/login" className="header-action-btn">
                <ShoppingCart size={24} />
                Giỏ hàng
              </Link>
            )}

            {authenticated && user ? (
              <div className="header-action-btn" style={{ position: 'relative', cursor: 'pointer' }} onClick={handleLogout}>
                <User size={24} />
                <div className="auth-btn-group">
                  <span>Chào, {user.username}</span>
                  <span style={{ fontWeight: 'bold' }}>Đăng xuất</span>
                </div>
              </div>
            ) : (
              <Link to="/login" className="header-action-btn">
                <User size={24} />
                <div className="auth-btn-group">
                  <span>Đăng nhập</span>
                  <span style={{ fontWeight: 'bold' }}>Đăng ký</span>
                </div>
              </Link>
            )}
            
            {authenticated && user && user.role === 'staff' && (
              <Link to="/staff/dashboard" className="header-action-btn">
                Quản lý
              </Link>
            )}
          </div>
        </div>
      </div>
    </header>
  );
}

export default Header;
