import axios from 'axios';

axios.defaults.baseURL = 'http://127.0.0.1:8000/api';

export default {
  getPhotosets() {
    return axios.get('/photosets/');
  },
  getPhotos(id) {
    return axios.get(`/photosets/${id}/photos/`);
  },
  getPhotosetsForMainPage() {
    return axios.get('/photosets/', {
      params: {
        show_on_mainpage: true
      }
    });
  },
  getPreferences(params = {}) {
    return axios.get('/dynamic-settings/', {
      params: params
    });
  }
};
