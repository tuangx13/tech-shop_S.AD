import React from 'react';
import ProductCard from '../ProductCard';
import './ProductGridSection.css';

function ProductGridSection({ title, brands = [], products = [], type, onAddToCart }) {
  return (
    <div className="product-section-wrapper">
      <div className="product-section-header">
        <h2 className="product-section-title">{title}</h2>
      </div>
      
      {brands.length > 0 && (
        <div className="product-brand-tabs">
          <div className="brand-list">
            {brands.map((brand, idx) => (
              <button key={idx} className="brand-tab">{brand}</button>
            ))}
          </div>
          <a href={`/${type}s`} className="view-all-link">Xem tất cả {title.toLowerCase()} &gt;</a>
        </div>
      )}

      <div className="product-section-content">
        {/* Left Side Promotional Banner */}
        <div className={`product-side-banner ${type}-banner`}>
          <div className="side-banner-content">
            {type === 'laptop' ? (
              <div className="banner-text">MACBOOK<br/>ƯU ĐÃI KHỦNG</div>
            ) : (
              <div className="banner-text">REDMI Note 15<br/>Bền vô đối<br/><span style={{fontSize:'16px'}}>Giá từ 5.49 Triệu</span></div>
            )}
          </div>
        </div>

        {/* Product Grid */}
        <div className="product-grid-area">
          {products.length > 0 ? (
            <div className="product-grid-inner">
              {products.slice(0, 8).map(product => (
                <ProductCard 
                  key={`${type}-${product.id}`}
                  product={product}
                  type={type}
                  onAddToCart={onAddToCart}
                />
              ))}
            </div>
          ) : (
            <div className="no-products">Không có sản phẩm nào.</div>
          )}
        </div>
      </div>
    </div>
  );
}

export default ProductGridSection;
