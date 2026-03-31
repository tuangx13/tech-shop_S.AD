import React, { useState } from "react";
import { Link, useNavigate, useSearchParams } from "react-router-dom";
import { getUser, logout, isAuthenticated } from "../utils/auth";
import "./Navbar.css";

function Navbar() {
  const navigate = useNavigate();
  const [searchParams] = useSearchParams();
  const [searchQuery, setSearchQuery] = useState(searchParams.get("q") || "");
  const user = getUser();
  const authenticated = isAuthenticated();

  const handleLogout = () => {
    logout();
    navigate("/");
  };

  const handleSearch = (e) => {
    e.preventDefault();
    if (searchQuery.trim()) {
      navigate(`/?q=${encodeURIComponent(searchQuery.trim())}`);
    } else {
      navigate("/");
    }
  };

  return (
    <nav className="navbar">
      <div className="navbar-brand">
        <Link to="/">TechShop</Link>
      </div>

      <form onSubmit={handleSearch} className="navbar-search">
        <input
          type="text"
          placeholder="Tìm kiếm sản phẩm..."
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
          className="search-input"
        />
        <button type="submit" className="search-btn">
          Tìm
        </button>
      </form>

      <div className="navbar-auth">
        {authenticated && user ? (
          <div className="user-menu">
            <span className="user-name">{user.username}</span>
            {user.role === "customer" && (
              <Link to="/customer/dashboard" className="btn btn-outline">
                Giỏ hàng
              </Link>
            )}
            {user.role === "staff" && (
              <Link to="/staff/dashboard" className="btn btn-outline">
                Quản lý
              </Link>
            )}
            <button onClick={handleLogout} className="btn btn-outline">
              Đăng xuất
            </button>
          </div>
        ) : (
          <div className="auth-buttons">
            <Link to="/login" className="btn btn-outline">
              Đăng nhập
            </Link>
            <Link to="/register" className="btn btn-primary">
              Đăng ký
            </Link>
          </div>
        )}
      </div>
    </nav>
  );
}

export default Navbar;
