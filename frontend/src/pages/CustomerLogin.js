import React from "react";
import { Navigate } from "react-router-dom";

// Redirect to new login page
function CustomerLogin() {
  return <Navigate to="/login" replace />;
}

export default CustomerLogin;
