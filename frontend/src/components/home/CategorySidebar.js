import React from 'react';
import { 
  Smartphone, Laptop, Tablet, Headphones, 
  Watch, Tv, Camera, Gamepad, Mouse, ChevronRight 
} from 'lucide-react';
import './CategorySidebar.css';

const categories = [
  { id: 1, name: 'Điện thoại, Tablet', icon: <Smartphone size={18} /> },
  { id: 2, name: 'Laptop', icon: <Laptop size={18} /> },
  { id: 3, name: 'Âm thanh, Mic thu âm', icon: <Headphones size={18} /> },
  { id: 4, name: 'Đồng hồ, Camera', icon: <Watch size={18} /> },
  { id: 5, name: 'Đồ gia dụng, Làm đẹp', icon: <Tv size={18} /> },
  { id: 6, name: 'Phụ kiện', icon: <Mouse size={18} /> },
  { id: 7, name: 'PC, Màn hình, Máy in', icon: <Laptop size={18} /> },
  { id: 8, name: 'Tivi, Điện máy', icon: <Tv size={18} /> },
  { id: 9, name: 'Thu cũ đổi mới', icon: <Gamepad size={18} /> },
  { id: 10, name: 'Hàng cũ', icon: <Camera size={18} /> },
  { id: 11, name: 'Khuyến mãi', icon: <Watch size={18} /> },
  { id: 12, name: 'Tin công nghệ', icon: <Smartphone size={18} /> },
];

function CategorySidebar() {
  return (
    <div className="category-sidebar">
      <ul className="category-list">
        {categories.map((cat) => (
          <li key={cat.id} className="category-item">
            <span className="category-icon">{cat.icon}</span>
            <span className="category-name">{cat.name}</span>
            <span className="category-arrow"><ChevronRight size={14} /></span>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default CategorySidebar;
