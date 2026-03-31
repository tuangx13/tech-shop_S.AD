import React from "react";
import "./ProductCard.css";

function ProductCard({ product, type, onAddToCart }) {
  const formatPrice = (price) => {
    return new Intl.NumberFormat("vi-VN", {
      style: "currency",
      currency: "VND",
    }).format(price);
  };

  const defaultImage =
    type === "laptop"
      ? "https://via.placeholder.com/300x200?text=Laptop"
      : "https://via.placeholder.com/300x200?text=Mobile";

  return (
    <div className="product-card">
      <div className="product-image">
        <img
          src={product.image_url || defaultImage}
          alt={product.name}
          onError={(e) => {
            e.target.src = defaultImage;
          }}
        />
        {product.stock <= 0 && <span className="out-of-stock">Hết hàng</span>}
        {product.stock > 0 && product.stock <= 5 && (
          <span className="low-stock">Còn {product.stock} sản phẩm</span>
        )}
      </div>

      <div className="product-info">
        <span className="product-brand">{product.brand}</span>
        <h3 className="product-name">{product.name}</h3>

        <div className="product-specs">
          {product.cpu && (
            <span className="spec">
              <i className="spec-icon">⚡</i> {product.cpu}
            </span>
          )}
          {product.ram && (
            <span className="spec">
              <i className="spec-icon">💾</i> {product.ram}
            </span>
          )}
          {product.storage && (
            <span className="spec">
              <i className="spec-icon">💿</i> {product.storage}
            </span>
          )}
          {product.screen_size && (
            <span className="spec">
              <i className="spec-icon">📱</i> {product.screen_size}
            </span>
          )}
          {type === "mobile" && product.battery && (
            <span className="spec">
              <i className="spec-icon">🔋</i> {product.battery}
            </span>
          )}
        </div>

        <div className="product-footer">
          <span className="product-price">{formatPrice(product.price)}</span>
          <button
            className="btn-add-cart"
            onClick={() => onAddToCart && onAddToCart(product, type)}
            disabled={product.stock <= 0}
          >
            {product.stock > 0 ? "Thêm vào giỏ" : "Hết hàng"}
          </button>
        </div>
      </div>
    </div>
  );
}

export default ProductCard;
