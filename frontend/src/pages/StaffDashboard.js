import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { getUser, logout } from "../utils/auth";
import { laptopAPI, mobileAPI } from "../services/api";
import MainLayout from "../components/layout/MainLayout";

function StaffDashboard() {
  const [user, setUser] = useState(null);
  const [laptops, setLaptops] = useState([]);
  const [mobiles, setMobiles] = useState([]);
  const [showForm, setShowForm] = useState(false);
  const [editingProduct, setEditingProduct] = useState(null);
  const [productType, setProductType] = useState("laptop");
  const [formData, setFormData] = useState({
    name: "",
    brand: "",
    price: "",
    description: "",
    cpu: "",
    ram: "",
    storage: "",
    screen_size: "",
    battery: "",
    stock: 0,
    image_url: "",
  });
  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  useEffect(() => {
    const currentUser = getUser();
    setUser(currentUser);
    loadProducts();
  }, []);

  const loadProducts = async () => {
    try {
      setLoading(true);
      const [laptopRes, mobileRes] = await Promise.all([
        laptopAPI.getAll(),
        mobileAPI.getAll(),
      ]);
      const sortedLaptops = (laptopRes.data || []).sort((a, b) => a.id - b.id);
      const sortedMobiles = (mobileRes.data || []).sort((a, b) => a.id - b.id);
      setLaptops(sortedLaptops);
      setMobiles(sortedMobiles);
    } catch (error) {
      console.error("Error loading products:", error);
    } finally {
      setLoading(false);
    }
  };

  const handleLogout = () => {
    logout();
    navigate("/staff/login");
  };

  const resetForm = () => {
    setFormData({
      name: "",
      brand: "",
      price: "",
      description: "",
      cpu: "",
      ram: "",
      storage: "",
      screen_size: "",
      battery: "",
      stock: 0,
      image_url: "",
    });
    setEditingProduct(null);
    setShowForm(false);
  };

  const handleAddNew = (type) => {
    setProductType(type);
    resetForm();
    setShowForm(true);
  };

  const handleEdit = (product, type) => {
    setProductType(type);
    setEditingProduct(product);
    setFormData({
      name: product.name || "",
      brand: product.brand || "",
      price: product.price || "",
      description: product.description || "",
      cpu: product.cpu || "",
      ram: product.ram || "",
      storage: product.storage || "",
      screen_size: product.screen_size || "",
      battery: product.battery || "",
      stock: product.stock || 0,
      image_url: product.image_url || "",
    });
    setShowForm(true);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const api = productType === "laptop" ? laptopAPI : mobileAPI;
      const data = {
        ...formData,
        price: parseFloat(formData.price),
        stock: parseInt(formData.stock),
      };

      if (editingProduct) {
        await api.update(editingProduct.id, data);
        setMessage(
          `Đã cập nhật ${productType === "laptop" ? "laptop" : "điện thoại"} thành công!`,
        );
      } else {
        await api.create(data);
        setMessage(
          `Đã thêm ${productType === "laptop" ? "laptop" : "điện thoại"} mới thành công!`,
        );
      }
      resetForm();
      loadProducts();
    } catch (error) {
      setMessage(
        `Lỗi: ${error.response?.data?.error || "Không thể lưu sản phẩm"}`,
      );
    }
    setTimeout(() => setMessage(""), 3000);
  };

  const handleDelete = async (product, type) => {
    if (!window.confirm(`Bạn có chắc muốn xóa "${product.name}"?`)) return;

    try {
      const api = type === "laptop" ? laptopAPI : mobileAPI;
      await api.delete(product.id);
      setMessage("Đã xóa sản phẩm thành công!");
      loadProducts();
    } catch (error) {
      setMessage(
        `Lỗi: ${error.response?.data?.error || "Không thể xóa sản phẩm"}`,
      );
    }
    setTimeout(() => setMessage(""), 3000);
  };

  const formatPrice = (price) => {
    return new Intl.NumberFormat("vi-VN", {
      style: "currency",
      currency: "VND",
    }).format(price);
  };

  if (loading) {
    return (
      <div
        style={{
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          height: "100vh",
        }}
      >
        Đang tải...
      </div>
    );
  }

  return (
    <MainLayout>
      <div style={{ padding: '20px', background: '#f4f6f8' }}>
        <h2 style={{ marginBottom: '20px' }}>👨‍💼 Staff Dashboard - Xin chào {user?.username}</h2>

      {message && (
        <div
          style={{
            position: "fixed",
            top: "80px",
            right: "20px",
            background: message.includes("Lỗi") ? "#dc3545" : "#28a745",
            color: "white",
            padding: "15px 25px",
            borderRadius: "8px",
            zIndex: 1000,
          }}
        >
          {message}
        </div>
      )}

      <div className="container" style={{ marginTop: "20px" }}>
        {/* Stats */}
        <div
          style={{
            display: "grid",
            gridTemplateColumns: "repeat(3, 1fr)",
            gap: "20px",
            marginBottom: "20px",
          }}
        >
          <div
            className="card"
            style={{
              textAlign: "center",
              background: "linear-gradient(135deg, #1e3c72, #2a5298)",
              color: "white",
            }}
          >
            <h3 style={{ margin: 0 }}>💻 Laptops</h3>
            <p
              style={{ fontSize: "36px", fontWeight: "bold", margin: "10px 0" }}
            >
              {laptops.length}
            </p>
          </div>
          <div
            className="card"
            style={{
              textAlign: "center",
              background: "linear-gradient(135deg, #28a745, #218838)",
              color: "white",
            }}
          >
            <h3 style={{ margin: 0 }}>📱 Mobiles</h3>
            <p
              style={{ fontSize: "36px", fontWeight: "bold", margin: "10px 0" }}
            >
              {mobiles.length}
            </p>
          </div>
          <div
            className="card"
            style={{
              textAlign: "center",
              background: "linear-gradient(135deg, #ff6b35, #ff5722)",
              color: "white",
            }}
          >
            <h3 style={{ margin: 0 }}>📦 Tổng</h3>
            <p
              style={{ fontSize: "36px", fontWeight: "bold", margin: "10px 0" }}
            >
              {laptops.length + mobiles.length}
            </p>
          </div>
        </div>

        {/* Add Form */}
        {showForm && (
          <div className="card" style={{ marginBottom: "20px" }}>
            <div
              style={{
                display: "flex",
                justifyContent: "space-between",
                alignItems: "center",
                marginBottom: "20px",
              }}
            >
              <h3>
                {editingProduct ? "Sửa" : "Thêm"}{" "}
                {productType === "laptop" ? "💻 Laptop" : "📱 Điện thoại"}
              </h3>
              <button onClick={resetForm} className="btn btn-secondary">
                Hủy
              </button>
            </div>
            <form onSubmit={handleSubmit}>
              <div
                style={{
                  display: "grid",
                  gridTemplateColumns: "repeat(2, 1fr)",
                  gap: "15px",
                }}
              >
                <div className="form-group">
                  <label>Tên sản phẩm *</label>
                  <input
                    type="text"
                    value={formData.name}
                    onChange={(e) =>
                      setFormData({ ...formData, name: e.target.value })
                    }
                    required
                  />
                </div>
                <div className="form-group">
                  <label>Thương hiệu *</label>
                  <input
                    type="text"
                    value={formData.brand}
                    onChange={(e) =>
                      setFormData({ ...formData, brand: e.target.value })
                    }
                    required
                  />
                </div>
                <div className="form-group">
                  <label>Giá (VND) *</label>
                  <input
                    type="number"
                    value={formData.price}
                    onChange={(e) =>
                      setFormData({ ...formData, price: e.target.value })
                    }
                    required
                  />
                </div>
                <div className="form-group">
                  <label>Tồn kho *</label>
                  <input
                    type="number"
                    value={formData.stock}
                    onChange={(e) =>
                      setFormData({ ...formData, stock: e.target.value })
                    }
                    required
                  />
                </div>
                <div className="form-group">
                  <label>CPU</label>
                  <input
                    type="text"
                    value={formData.cpu}
                    onChange={(e) =>
                      setFormData({ ...formData, cpu: e.target.value })
                    }
                  />
                </div>
                <div className="form-group">
                  <label>RAM</label>
                  <input
                    type="text"
                    value={formData.ram}
                    onChange={(e) =>
                      setFormData({ ...formData, ram: e.target.value })
                    }
                  />
                </div>
                <div className="form-group">
                  <label>Bộ nhớ</label>
                  <input
                    type="text"
                    value={formData.storage}
                    onChange={(e) =>
                      setFormData({ ...formData, storage: e.target.value })
                    }
                  />
                </div>
                <div className="form-group">
                  <label>Màn hình</label>
                  <input
                    type="text"
                    value={formData.screen_size}
                    onChange={(e) =>
                      setFormData({ ...formData, screen_size: e.target.value })
                    }
                  />
                </div>
                {productType === "mobile" && (
                  <div className="form-group">
                    <label>Pin</label>
                    <input
                      type="text"
                      value={formData.battery}
                      onChange={(e) =>
                        setFormData({ ...formData, battery: e.target.value })
                      }
                    />
                  </div>
                )}
                <div className="form-group">
                  <label>URL Hình ảnh</label>
                  <input
                    type="url"
                    value={formData.image_url}
                    onChange={(e) =>
                      setFormData({ ...formData, image_url: e.target.value })
                    }
                  />
                </div>
              </div>
              <div className="form-group">
                <label>Mô tả</label>
                <textarea
                  value={formData.description}
                  onChange={(e) =>
                    setFormData({ ...formData, description: e.target.value })
                  }
                  rows="3"
                  style={{
                    width: "100%",
                    padding: "10px",
                    borderRadius: "5px",
                    border: "1px solid #ddd",
                  }}
                />
              </div>
              <button type="submit" className="btn btn-success">
                {editingProduct ? "Cập nhật" : "Thêm mới"}
              </button>
            </form>
          </div>
        )}

        {/* Laptops Table */}
        <div className="card" style={{ marginBottom: "20px" }}>
          <div
            style={{
              display: "flex",
              justifyContent: "space-between",
              alignItems: "center",
              marginBottom: "15px",
              gap: "20px" /* Thêm gap để tạo khoảng cách */,
            }}
          >
            <h3 style={{ margin: 0, whiteSpace: "nowrap" }}>
              💻 Quản lý Laptops ({laptops.length})
            </h3>
            <button
              onClick={() => handleAddNew("laptop")}
              className="btn btn-primary"
              style={{
                width: "max-content",
                whiteSpace: "nowrap",
              }} /* FIX NÚT */
            >
              + Thêm Laptop
            </button>
          </div>
          <div style={{ overflowX: "auto" }}>
            <table>
              <thead>
                <tr>
                  <th>ID</th>
                  <th>Tên</th>
                  <th>Thương hiệu</th>
                  <th>Giá</th>
                  <th>CPU</th>
                  <th>RAM</th>
                  <th>Tồn kho</th>
                  <th>Thao tác</th>
                </tr>
              </thead>
              <tbody>
                {laptops.map((laptop) => (
                  <tr key={laptop.id}>
                    <td>{laptop.id}</td>
                    <td>{laptop.name}</td>
                    <td>{laptop.brand}</td>
                    <td>{formatPrice(laptop.price)}</td>
                    <td>{laptop.cpu}</td>
                    <td>{laptop.ram}</td>
                    <td>
                      <span
                        style={{
                          color: laptop.stock <= 5 ? "#dc3545" : "#28a745",
                        }}
                      >
                        {laptop.stock}
                      </span>
                    </td>
                    <td>
                      <button
                        onClick={() => handleEdit(laptop, "laptop")}
                        className="btn btn-primary"
                        style={{ marginRight: "5px", padding: "5px 10px" }}
                      >
                        Sửa
                      </button>
                      <button
                        onClick={() => handleDelete(laptop, "laptop")}
                        className="btn btn-danger"
                        style={{ padding: "5px 10px" }}
                      >
                        Xóa
                      </button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>

        {/* Mobiles Table */}
        <div className="card">
          <div
            style={{
              display: "flex",
              justifyContent: "space-between",
              alignItems: "center",
              marginBottom: "15px",
              gap: "20px",
            }}
          >
            <h3 style={{ margin: 0, whiteSpace: "nowrap" }}>
              📱 Quản lý Điện thoại ({mobiles.length})
            </h3>
            <button
              onClick={() => handleAddNew("mobile")}
              className="btn btn-success"
              style={{
                width: "max-content",
                whiteSpace: "nowrap",
              }} /* FIX NÚT */
            >
              + Thêm Điện thoại
            </button>
          </div>
          <div style={{ overflowX: "auto" }}>
            <table>
              <thead>
                <tr>
                  <th>ID</th>
                  <th>Tên</th>
                  <th>Thương hiệu</th>
                  <th>Giá</th>
                  <th>CPU</th>
                  <th>RAM</th>
                  <th>Pin</th>
                  <th>Tồn kho</th>
                  <th>Thao tác</th>
                </tr>
              </thead>
              <tbody>
                {mobiles.map((mobile) => (
                  <tr key={mobile.id}>
                    <td>{mobile.id}</td>
                    <td>{mobile.name}</td>
                    <td>{mobile.brand}</td>
                    <td>{formatPrice(mobile.price)}</td>
                    <td>{mobile.cpu}</td>
                    <td>{mobile.ram}</td>
                    <td>{mobile.battery}</td>
                    <td>
                      <span
                        style={{
                          color: mobile.stock <= 5 ? "#dc3545" : "#28a745",
                        }}
                      >
                        {mobile.stock}
                      </span>
                    </td>
                    <td>
                      <button
                        onClick={() => handleEdit(mobile, "mobile")}
                        className="btn btn-primary"
                        style={{ marginRight: "5px", padding: "5px 10px" }}
                      >
                        Sửa
                      </button>
                      <button
                        onClick={() => handleDelete(mobile, "mobile")}
                        className="btn btn-danger"
                        style={{ padding: "5px 10px" }}
                      >
                        Xóa
                      </button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>
      </div>
    </MainLayout>
  );
}

export default StaffDashboard;
