import React, { useState, useEffect } from "react";
import { useNavigate, useSearchParams } from "react-router-dom";
import MainLayout from "../components/layout/MainLayout";
import CategorySidebar from "../components/home/CategorySidebar";
import MainBanner from "../components/home/MainBanner";
import RightSidebar from "../components/home/RightSidebar";
import SubBanners from "../components/home/SubBanners";
import ProductGridSection from "../components/home/ProductGridSection";
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
      setError("Không thể tải sản phẩm. Vui lòng thử lại sau.");
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
      setMessage("Chỉ khách hàng mới có thể thêm sản phẩm vào giỏ hàng.");
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
      setMessage(`Đã thêm ${product.name} vào giỏ hàng!`);
      setTimeout(() => setMessage(""), 3000);
    } catch (err) {
      setMessage("Không thể thêm sản phẩm vào giỏ hàng.");
      setTimeout(() => setMessage(""), 3000);
    }
  };

  const filterProducts = (products) => {
    if (!searchQuery.trim()) return products;
    const query = searchQuery.toLowerCase();
    return products.filter(
      (p) =>
        (p.name || "").toLowerCase().includes(query) ||
        (p.brand || "").toLowerCase().includes(query) ||
        (p.description || "").toLowerCase().includes(query)
    );
  };

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
      <MainLayout>
        <div className="loading-container">
          <div className="spinner"></div>
          <p>Đang tải sản phẩm...</p>
        </div>
      </MainLayout>
    );
  }

  const isSearching = searchQuery.trim() !== "";
  const searchResults = isSearching ? getSearchResults() : [];

  return (
    <MainLayout>
      <div className="home-container container-lg">
        {message && <div className="toast-message">{message}</div>}
        {error && <div className="error-banner">{error}</div>}

        {!isSearching && (
          <>
            {/* Top Row: Sidebar, Banner, RightSidebar */}
            <div className="home-top-row">
              <CategorySidebar />
              <MainBanner />
              <RightSidebar />
            </div>

            {/* Sub banners */}
            <SubBanners />
          </>
        )}

        {isSearching ? (
          <div className="search-results-section">
            <h2 className="search-title">Kết quả tìm kiếm cho: "{searchQuery}"</h2>
            {searchResults.length > 0 ? (
              <div className="product-grid-inner" style={{marginTop:'20px'}}>
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
        ) : (
          <>
            <ProductGridSection
              title="ĐIỆN THOẠI NỔI BẬT"
              brands={['Apple', 'Samsung', 'Xiaomi', 'OPPO', 'Nokia']}
              products={mobiles}
              type="mobile"
              onAddToCart={handleAddToCart}
            />

            <ProductGridSection
              title="LAPTOP HOT"
              brands={['MacBook', 'Asus', 'Dell', 'HP', 'Lenovo', 'Acer']}
              products={laptops}
              type="laptop"
              onAddToCart={handleAddToCart}
            />
          </>
        )}
      </div>
      
      {/* Footer replacing the old one momentarily or keeping basic */}
      <footer className="footer-basic">
        <div className="container-lg text-center">
          <p>&copy; 2024 CellphoneS Clone - Designed for professional appearance</p>
        </div>
      </footer>
    </MainLayout>
  );
}

export default Home;
