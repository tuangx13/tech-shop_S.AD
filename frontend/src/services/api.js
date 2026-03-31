import axios from "axios";
import { getToken } from "../utils/auth";

const API_BASE_URL =
  process.env.REACT_APP_API_GATEWAY || "http://localhost:8080";

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

// Add token to requests
api.interceptors.request.use(
  (config) => {
    const token = getToken();
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error),
);

// Auth API
export const authAPI = {
  login: (credentials) => api.post("/api/auth/login/", credentials),
  register: (userData) => api.post("/api/auth/register/", userData),
  verify: () => api.get("/api/auth/verify/"),
  getMe: () => api.get("/api/auth/me/"),
};

// Customer API
export const customerAPI = {
  getCart: () => api.get("/api/customer/cart/"),
  addToCart: (item) => api.post("/api/customer/cart/", item),
  updateCartItem: (itemId, data) =>
    api.put(`/api/customer/cart/${itemId}/`, data),
  removeFromCart: (itemId) => api.delete(`/api/customer/cart/${itemId}/`),
  search: (query) => api.get("/api/customer/search/", { params: { q: query } }),
};

// Staff API
export const staffAPI = {
  getProducts: () => api.get("/api/staff/products/"),
  // Laptops
  getLaptops: () => api.get("/api/staff/laptops/"),
  addLaptop: (data) => api.post("/api/staff/laptops/", data),
  updateLaptop: (id, data) => api.put(`/api/staff/laptops/${id}/`, data),
  deleteLaptop: (id) => api.delete(`/api/staff/laptops/${id}/`),
  // Mobiles
  getMobiles: () => api.get("/api/staff/mobiles/"),
  addMobile: (data) => api.post("/api/staff/mobiles/", data),
  updateMobile: (id, data) => api.put(`/api/staff/mobiles/${id}/`, data),
  deleteMobile: (id) => api.delete(`/api/staff/mobiles/${id}/`),
};

// Product APIs (public read)
export const laptopAPI = {
  getAll: () => api.get("/api/laptops/"),
  getOne: (id) => api.get(`/api/laptops/${id}/`),
  // Write operations (requires staff token)
  create: (data) => api.post("/api/laptops/", data),
  update: (id, data) => api.put(`/api/laptops/${id}/`, data),
  delete: (id) => api.delete(`/api/laptops/${id}/`),
};

export const mobileAPI = {
  getAll: () => api.get("/api/mobiles/"),
  getOne: (id) => api.get(`/api/mobiles/${id}/`),
  // Write operations (requires staff token)
  create: (data) => api.post("/api/mobiles/", data),
  update: (id, data) => api.put(`/api/mobiles/${id}/`, data),
  delete: (id) => api.delete(`/api/mobiles/${id}/`),
};

export default api;
