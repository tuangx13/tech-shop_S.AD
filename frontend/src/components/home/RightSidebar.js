import React from 'react';
import { User, Gift, GraduationCap, RefreshCw, Briefcase, ShieldCheck } from 'lucide-react';
import './RightSidebar.css';

function RightSidebar() {
  return (
    <div className="right-sidebar">
      {/* Smember Card */}
      <div className="smember-card">
        <div className="smember-header">
          <div className="smember-icon-bg">
            <User size={24} color="#d70018" />
          </div>
          <div>
            <div className="smember-title">Chào mừng bạn đến với CellphoneS</div>
          </div>
        </div>
        <div className="smember-desc">
          Nhập hội thành viên Smember để không bỏ lỡ các ưu đãi hấp dẫn.
        </div>
        <div className="smember-auth">
          <a href="/login" className="smember-login">Đăng nhập</a> hoặc <a href="/register" className="smember-register">Đăng ký</a>
        </div>
        <button className="smember-promo-btn">
          <Gift size={16} /> Xem ưu đãi Smember
        </button>
      </div>

      {/* Promos List */}
      <div className="promo-list">
        <a href="#" className="promo-item">
          <GraduationCap size={18} className="promo-icon" color="#d70018" />
          <div className="promo-content">
            <div className="promo-title">Ưu đãi cho giáo dục</div>
            <div className="promo-desc">Đăng ký nhận ưu đãi</div>
          </div>
        </a>
        <a href="#" className="promo-item">
          <RefreshCw size={18} className="promo-icon" color="#d70018" />
          <div className="promo-content">
            <div className="promo-title">Thu cũ lên đời giá hời</div>
            <div className="promo-desc">iPhone trợ giá đến 3 triệu</div>
          </div>
        </a>
        <a href="#" className="promo-item">
          <Briefcase size={18} className="promo-icon" color="#d70018" />
          <div className="promo-content">
            <div className="promo-title">Khách hàng doanh nghiệp (B2B)</div>
            <div className="promo-desc">Đăng ký S-Business</div>
          </div>
        </a>
        <a href="#" className="promo-item">
          <ShieldCheck size={18} className="promo-icon" color="#d70018" />
          <div className="promo-content">
            <div className="promo-title">Chính sách ưu đãi</div>
            <div className="promo-desc">Hàng mới đồ bộ GIẢM ĐẾN 50%</div>
          </div>
        </a>
      </div>
    </div>
  );
}

export default RightSidebar;
