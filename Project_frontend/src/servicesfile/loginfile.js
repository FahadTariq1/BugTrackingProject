import axios from "axios";

const API_BASE_URL = 'http://localhost:8000/auth';

export const loginUser = async (userData) => {
    const response = await axios.post(`${API_BASE_URL}/login/`, userData);
    return response.data;
  };
  

// Api for sign up 

export const signupUser = async (userData) => {
  const response = await axios.post(`${API_BASE_URL}/sign-up/`, userData);
  return response.data;
};
