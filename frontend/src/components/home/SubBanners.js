import React from 'react';
import './SubBanners.css';

function SubBanners() {
  return (
    <div className="sub-banners-container">
      {/* Student/Teacher Promo Banner */}
      <div className="promo-banner-large" style={{ background: '#e0ffe8' }}>
        <div className="promo-large-inner">
          <div className="promo-large-content">
            <h2 className="promo-large-title">
              <span className="text-red">Say Hi!</span> S-STUDENT S-TEACHER
            </h2>
          </div>
          <div className="promo-large-badge">
            <div className="badge-text-small">Giảm thêm<br/>lên đến</div>
            <div className="badge-text-large">10%</div>
          </div>
          <button className="promo-large-btn">XEM CHI TIẾT</button>
        </div>
      </div>
    </div>
  );
}

export default SubBanners;
