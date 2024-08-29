import axios from 'axios';

// Set up the base URL and axios instance without default headers
const API_BASE_URL = 'http://localhost:8000';

const apiClient = axios.create({
  baseURL: API_BASE_URL,
});

// Add a request interceptor to include the Authorization header
apiClient.interceptors.request.use(
  (config) => {
    const authToken = localStorage.getItem('authToken');
    if (authToken) {
      config.headers.Authorization = `Bearer ${authToken}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

export const fetchAllProjects = async (page = 1, pageSize = 6, description_search = '') => {
  try {
    const response = await apiClient.get(`/project/all/?page=${page}&page_size=${pageSize}&description_search=${description_search}`);
    console.log(response.data);
    return response.data;
  } catch (error) {
    console.error('Error fetching projects data:', error);
    throw error;
  }
};

// API call for searching bugs
export const searchBugs = async (description, project_id) => {
  try {
    const response = await apiClient.get('bugs/search/', {
      params: {
        description,
        project_id,
      },
    });
    return response.data;
  } catch (error) {
    console.error('Error searching bugs:', error);
    throw error;
  }
};

// API call for updating bug status
export const updateBugStatus = async (bugId, status) => {
  try {
    await apiClient.patch(`bugs/update/${bugId}/`, {
      status: status,
    });
    console.log(`Bug ${bugId} status changed to ${status}.`);
    return true;
  } catch (error) {
    console.error(`Error updating bug ${bugId} status to ${status}:`, error);
    return false;
  }
};

// API call for deleting a bug
export const deleteBug = async (bugId) => {
  try {
    await apiClient.delete(`/bugs/delete/${bugId}/`, {
      status: status,
    });
    console.log(`Bug ${bugId} marked as deleted.`);
    return true;
  } catch (error) {
    console.error(`Error deleting bug ${bugId}:`, error);
    return false;
  }
};

// API call for creating the project
export const createProject = async (formData) => {
  try {
    const response = await apiClient.post('/project/create/', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    return response.data;
  } catch (error) {
    console.error('Error creating project:', error);
    throw error;
  }
};

export const fetchDevelopers = async () => {
  try {
    const response = await apiClient.get('/auth/all-developers/');
    return response.data;
  } catch (error) {
    console.error('Error fetching developers:', error);
    throw error;
  }
};

// API call for creating a new bug
export const createBug = async (formData) => {
  try {
    const response = await apiClient.post('/bugs/create/', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    return response.data;
  } catch (error) {
    console.error('Error creating bug:', error);
    throw error;
  }
};