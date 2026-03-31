import React, { useState, useEffect } from "react";
import { useNavigate, useSearchParams } from "react-router-dom";
import Navbar from "../components/Navbar";
import ProductCard from "../components/ProductCard";
import { laptopAPI, mobileAPI, customerAPI } from "../services/api";
import { isAuthenticated, getUser } from "../utils/auth";
import "./Home.css";

function Home() {
  const navigate = useNavigate();
  const [searchParams] = useSearchParams();
  const searchQuery = searchParams.get("q") || "";

  const [laptops, setLaptops] = useState([]);
  const [mobiles, setMobiles] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [message, setMessage] = useState("");

  useEffect(() => {
    fetchProducts();
  }, []);

  const fetchProducts = async () => {
    try {
      setLoading(true);
      const [laptopRes, mobileRes] = await Promise.all([
        laptopAPI.getAll(),
        mobileAPI.getAll(),
      ]);
      setLaptops(laptopRes.data);
      setMobiles(mobileRes.data);
    } catch (err) {
      setError("Khong the tai san pham. Vui long thu lai sau.");
      console.error("Error fetching products:", err);
    } finally {
      setLoading(false);
    }
  };

  const handleAddToCart = async (product, type) => {
    if (!isAuthenticated()) {
      navigate("/login");
      return;
    }

    const user = getUser();
    if (user.role !== "customer") {
      setMessage("Chi khach hang moi co the them san pham vao gio hang.");
      setTimeout(() => setMessage(""), 3000);
      return;
    }

    try {
      await customerAPI.addToCart({
        product_id: product.id,
        product_type: type,
        product_name: `${product.brand} ${product.name}`,
        product_price: product.price,
        quantity: 1,
      });
      setMessage(`Da them ${product.name} vao gio hang!`);
      setTimeout(() => setMessage(""), 3000);
    } catch (err) {
      setMessage("Khong the them san pham vao gio hang.");
      setTimeout(() => setMessage(""), 3000);
    }
  };

  // Filter products based on search query
  const filterProducts = (products) => {
    if (!searchQuery.trim()) return products;
    const query = searchQuery.toLowerCase();
    return products.filter(
      (p) =>
        (p.name || "").toLowerCase().includes(query) ||
        (p.brand || "").toLowerCase().includes(query) ||
        (p.description || "").toLowerCase().includes(query),
    );
  };

  // Combine and filter all products for search results
  const getSearchResults = () => {
    const filteredLaptops = filterProducts(laptops).map((p) => ({
      ...p,
      type: "laptop",
    }));
    const filteredMobiles = filterProducts(mobiles).map((p) => ({
      ...p,
      type: "mobile",
    }));
    return [...filteredLaptops, ...filteredMobiles];
  };

  if (loading) {
    return (
      <div>
        <Navbar />
        <div className="loading-container">
          <div className="spinner"></div>
          <p>Dang tai san pham...</p>
        </div>
      </div>
    );
  }

  const isSearching = searchQuery.trim() !== "";
  const searchResults = isSearching ? getSearchResults() : [];

  return (
    <div className="home-page">
      <Navbar />

      {message && <div className="toast-message">{message}</div>}

      {/* Hero Section - only show when not searching */}
      {!isSearching && (
        <section className="hero">
          <div className="hero-content">
            <h1>Chào mừng đến với TechShop</h1>
            <p>Khám phá các sản phẩm cộng nghệ hàng đầu với giá tốt nhất</p>
          </div>
        </section>
      )}

      {error && <div className="error-banner">{error}</div>}

      {/* Search Results - unified view */}
      {isSearching ? (
        <section className="product-section">
          <div className="container">
            <div className="section-header">
              <h2>Kết quả tìm kiếm: "{searchQuery}"</h2>
              <p>Tìm thấy {searchResults.length} sản phẩm</p>
            </div>

            {searchResults.length > 0 ? (
              <div className="product-grid">
                {searchResults.map((product) => (
                  <ProductCard
                    key={`${product.type}-${product.id}`}
                    product={product}
                    type={product.type}
                    onAddToCart={handleAddToCart}
                  />
                ))}
              </div>
            ) : (
              <p className="no-products">Không tìm thấy sản phẩm phù hợp.</p>
            )}
          </div>
        </section>
      ) : (
        <>
          {/* Laptops Section */}
          <section id="laptops" className="product-section">
            <div className="container">
              <div className="section-header">
                <h2>Laptop</h2>
                <p>Laptop chính hãng từ các thương hiệu hàng đầu</p>
              </div>

              {laptops.length > 0 ? (
                <div className="product-grid">
                  {laptops.map((laptop) => (
                    <ProductCard
                      key={laptop.id}
                      product={laptop}
                      type="laptop"
                      onAddToCart={handleAddToCart}
                    />
                  ))}
                </div>
              ) : (
                <p className="no-products">Chưa có sản phâm laptop nào.</p>
              )}
            </div>
          </section>

          {/* Mobiles Section */}
          <section id="mobiles" className="product-section mobile-section">
            <div className="container">
              <div className="section-header">
                <h2>Điện thoại</h2>
                <p>Điện thoại thông minh với công nghệ tiên tiến</p>
              </div>

              {mobiles.length > 0 ? (
                <div className="product-grid">
                  {mobiles.map((mobile) => (
                    <ProductCard
                      key={mobile.id}
                      product={mobile}
                      type="mobile"
                      onAddToCart={handleAddToCart}
                    />
                  ))}
                </div>
              ) : (
                <p className="no-products">Chưa có sản phẩm điện thoại nào.</p>
              )}
            </div>
          </section>
        </>
      )}

      {/* Footer */}
      <footer className="footer">
        <div className="container">
          <div className="footer-content">
            <div className="footer-brand">
              <h3>TechShop</h3>
              <p>Cửa hàng công nghệ uy tín hàng đầu</p>
            </div>
            <div className="footer-links">
              <h4>Liên kết</h4>
              <a href="#laptops">Laptop</a>
              <a href="#mobiles">Điện thoại</a>
            </div>
            <div className="footer-contact">
              <h4>Liên hệ</h4>
              <p>Email: contact@techshop.vn</p>
              <p>Hotline: 1900-xxxx</p>
            </div>
          </div>
          <div className="footer-bottom">
            <p>&copy; 2024 TechShop. All rights reserved.</p>
          </div>
        </div>
      </footer>
    </div>
  );
}

export default Home;
