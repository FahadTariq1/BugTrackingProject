import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000/BugUsers';

// Api for sign up 

export const signupUser = async (userData) => {
  const response = await axios.post(`${API_BASE_URL}/signup/`, userData);
  return response.data;
};
