import React, { useState, useEffect } from "react";
import { Link, useNavigate } from "react-router-dom";
import { getUser, logout } from "../utils/auth";
import { customerAPI } from "../services/api";
import MainLayout from "../components/layout/MainLayout";
import "./CustomerDashboard.css";

function CustomerDashboard() {
  const [user, setUser] = useState(null);
  const [cart, setCart] = useState({
    items: [],
    total_items: 0,
    total_price: "0",
  });
  const [loading, setLoading] = useState(true);
  const [message, setMessage] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    const currentUser = getUser();
    if (!currentUser || currentUser.role !== "customer") {
      navigate("/login");
      return;
    }
    setUser(currentUser);
    loadCart();
  }, [navigate]);

  const loadCart = async () => {
    try {
      setLoading(true);
      const response = await customerAPI.getCart();
      setCart(response.data);
    } catch (error) {
      console.error("Error loading cart:", error);
    } finally {
      setLoading(false);
    }
  };

  const handleRemoveFromCart = async (itemId) => {
    try {
      await customerAPI.removeFromCart(itemId);
      await loadCart();
      setMessage("Đã xóa sản phẩm khỏi giỏ hàng.");
      setTimeout(() => setMessage(""), 3000);
    } catch (error) {
      console.error("Error removing from cart:", error);
    }
  };

  const handleUpdateQuantity = async (itemId, newQuantity) => {
    try {
      if (newQuantity <= 0) {
        await handleRemoveFromCart(itemId);
        return;
      }
      await customerAPI.updateCartItem(itemId, { quantity: newQuantity });
      await loadCart();
    } catch (error) {
      console.error("Error updating quantity:", error);
    }
  };

  const formatPrice = (price) => {
    return new Intl.NumberFormat("vi-VN", {
      style: "currency",
      currency: "VND",
    }).format(price);
  };

  if (loading) {
    return (
      <MainLayout>
        <div className="loading-container">
          <div className="spinner"></div>
          <p>Đang tải giỏ hàng...</p>
        </div>
      </MainLayout>
    );
  }

  return (
    <MainLayout>
      <div className="customer-dashboard">

      {message && <div className="toast-message">{message}</div>}

      <div className="dashboard-container">
        <div className="cart-header">
          <h1>Giỏ hàng của bạn</h1>
          <p>{user?.username}</p>
        </div>

        {cart.items && cart.items.length === 0 ? (
          <div className="empty-cart">
            <div className="empty-cart-icon">🛒</div>
            <h2>Giỏ hàng trống</h2>
            <p>Bạn chưa có sản phẩm nào trong giỏ hàng.</p>
            <Link to="/" className="btn btn-primary">
              Tiếp tục mua sắm
            </Link>
          </div>
        ) : (
          <div className="cart-content">
            <div className="cart-items">
              <h3>Sản phẩm ({cart.total_items})</h3>
              {cart.items &&
                cart.items.map((item) => (
                  <div key={item.id} className="cart-item">
                    <div className="item-info">
                      <span className={`item-type ${item.product_type}`}>
                        {item.product_type === "laptop" ? "Laptop" : "Mobile"}
                      </span>
                      <h4>{item.product_name}</h4>
                      <p className="item-price">
                        {formatPrice(item.product_price)}
                      </p>
                    </div>
                    <div className="item-actions">
                      <div className="quantity-control">
                        <button
                          onClick={() =>
                            handleUpdateQuantity(item.id, item.quantity - 1)
                          }
                          className="qty-btn"
                        >
                          -
                        </button>
                        <span className="quantity">{item.quantity}</span>
                        <button
                          onClick={() =>
                            handleUpdateQuantity(item.id, item.quantity + 1)
                          }
                          className="qty-btn"
                        >
                          +
                        </button>
                      </div>
                      <p className="item-total">
                        {formatPrice(item.total_price)}
                      </p>
                      <button
                        onClick={() => handleRemoveFromCart(item.id)}
                        className="remove-btn"
                      >
                        Xóa
                      </button>
                    </div>
                  </div>
                ))}
            </div>

            <div className="cart-summary">
              <h3>Tổng cộng</h3>
              <div className="summary-row">
                <span>Số lượng sản phẩm:</span>
                <span>{cart.total_items}</span>
              </div>
              <div className="summary-row total">
                <span>Tổng tiền:</span>
                <span className="total-price">
                  {formatPrice(cart.total_price)}
                </span>
              </div>
              <button className="btn btn-checkout">Thanh toán</button>
              <Link to="/" className="btn btn-continue">
                Tiếp tục mua sắm
              </Link>
            </div>
          </div>
        )}
      </div>
      </div>
    </MainLayout>
  );
}

export default CustomerDashboard;
