import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { authAPI } from "../services/api";
import { setToken, setUser } from "../utils/auth";
import "./Auth.css";

function StaffLogin() {
  const [formData, setFormData] = useState({ username: "", password: "" });
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setLoading(true);

    try {
      const response = await authAPI.login({ ...formData, role: "staff" });
      setToken(response.data.token);
      setUser(response.data.user);
      navigate("/staff/dashboard");
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
    <div className="auth-page staff-auth">
      <div className="auth-container">
        <div className="auth-card staff-card">
          <div className="auth-header">
            <div className="staff-icon">👨‍💼</div>
            <h2>Đăng nhập Nhân viên</h2>
            <p>Dành cho nhân viên TechShop</p>
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

            <button
              type="submit"
              className="btn-submit btn-staff"
              disabled={loading}
            >
              {loading ? "Đang đăng nhập..." : "Đăng nhập"}
            </button>
          </form>

          <div className="auth-footer">
            <p>
              Bạn là khách hàng? <Link to="/login">Đăng nhập tại đây</Link>
            </p>
            <p>
              <Link to="/">← Về trang chủ</Link>
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default StaffLogin;
