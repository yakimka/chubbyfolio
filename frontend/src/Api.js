import axios from 'axios';
import config from './config';

axios.defaults.baseURL = config.VUE_APP_ROOT_API;

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
  },
  createMessage(params = {}) {
    return axios.post('/feedback/message/', params);
  }
};
