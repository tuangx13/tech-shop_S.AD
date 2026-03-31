import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import Navbar from "../components/Navbar";
import { authAPI } from "../services/api";
import { setToken, setUser } from "../utils/auth";
import "./Auth.css";

function Login() {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    username: "",
    password: "",
  });
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setLoading(true);

    try {
      const response = await authAPI.login({
        ...formData,
        role: "customer",
      });
      setToken(response.data.token);
      setUser(response.data.user);
      navigate("/");
    } catch (err) {
      setError(
        err.response?.data?.error ||
          "Đăng nhập thất bại. Vui lòng kiểm tra lại thông tin.",
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="auth-page">
      <Navbar />
      <div className="auth-container">
        <div className="auth-card">
          <div className="auth-header">
            <h2>Đăng nhập Khách hàng</h2>
            <p>Chào mừng trở lại! Vui lòng đăng nhập để tiếp tục mua sắm.</p>
          </div>

          <form onSubmit={handleSubmit} className="auth-form">
            <div className="form-group">
              <label>Tên đăng nhập</label>
              <input
                type="text"
                name="username"
                value={formData.username}
                onChange={handleChange}
                placeholder="Nhập tên đăng nhập"
                required
              />
            </div>

            <div className="form-group">
              <label>Mật khẩu</label>
              <input
                type="password"
                name="password"
                value={formData.password}
                onChange={handleChange}
                placeholder="Nhập mật khẩu"
                required
              />
            </div>

            {error && <div className="error-message">{error}</div>}

            <button type="submit" className="btn-submit" disabled={loading}>
              {loading ? "Đang đăng nhập..." : "Đăng nhập"}
            </button>
          </form>

          <div className="auth-footer">
            <p>
              Chưa có tài khoản? <Link to="/register">Đăng ký ngay</Link>
            </p>
            <p className="staff-link">
              Bạn là nhân viên? <Link to="/staff/login">Đăng nhập Staff</Link>
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Login;
