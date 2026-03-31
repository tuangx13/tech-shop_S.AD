import React from 'react';
import './MainBanner.css';

function MainBanner() {
  return (
    <div className="main-banner">
      <div className="banner-slider">
        {/* Placeholder for actual carousel */}
        <div className="banner-slide active">
          <div className="banner-content">
            <h2 className="banner-title">SAMSUNG</h2>
            <h1 className="banner-headline">Galaxy S26 Series</h1>
            <p className="banner-price">Giá chỉ từ: <span>22.990.000 ₫</span></p>
            
            <div className="banner-features">
              <div className="feature-item">
                <span className="feature-title">Lên đời trợ giá đến</span>
                <span className="feature-value">5 Triệu</span>
              </div>
              <div className="feature-item feature-middle">
                <span className="feature-title">Tặng Bảo Hành</span>
                <span className="feature-value">12 Tháng 1 Đổi 1</span>
                <span className="feature-subtitle">Không lấy giảm 1 triệu</span>
              </div>
              <div className="feature-item">
                <span className="feature-title">Trả góp</span>
                <span className="feature-value">0%</span>
                <span className="feature-desc">Đến 18 tháng</span>
              </div>
            </div>

            <button className="banner-btn">MUA NGAY</button>
          </div>
          <div className="banner-image-placeholder">
            {/* Visual representation of phones */}
            <div className="mock-phone phone-1"></div>
            <div className="mock-phone phone-2"></div>
            <div className="mock-phone phone-3"></div>
          </div>
        </div>
      </div>
      
      <div className="banner-controls">
        <div className="control-item active">GALAXY S26 ULTRA<br/>Mở bán ưu đãi khủng</div>
        <div className="control-item">MACBOOK NÉO<br/>Đăng ký nhận tin</div>
        <div className="control-item">IPHONE 17e<br/>Mở bán ưu đãi đến 2.65 triệu</div>
        <div className="control-item">OPPO FIND N6<br/>Mở bán tặng quà 15 triệu</div>
      </div>
    </div>
  );
}

export default MainBanner;
