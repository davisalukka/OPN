import axios from 'axios';
//import AuthService from '../auth/AuthService';
const API_URL = 'http://64.191.45.142:8081';

export class APIService{
    constructor(){
    }

    getMetric() {
        const url = '${API_URL}/api/valuationMetrics/';
        return axios.get(url, { headers: { Authorization: 'Bearer ${AuthService.getAuthToken()}' }}).then(response => response.data);
  }
    getMetric(pk) {
        const url = '${API_URL}/api/valuationMetrics/${pk}';
        return axios.get(url, { headers: {Authorization: 'Bearer ${AuthService.getAuthToken()}' }}).then(response => response.data);
    }

    getMetricByUrl(link){
        const url = '${API_URL}${link}';
        return axios.get(url, { headers: {Authorization: 'Bearer ${AuthService.getAuthToken()}' }}).then(response => response.data);
    }

    deleteMetric(pk) {
        const url = '${API_URL}/api/valuationMetrics/${pk}';
        return axios.delete(url, { headers: {Authorization: 'Bearer ${AuthService.getAuthToken()}' }});
    }

    createMetric(metric){
        const url='${API_URL}/api/valuationMetrics/';
        const headers = {Authorization: 'Bearer ${AuthService.getAuthToken()}'};
        return axios.post(url, metric, {headers: headers});
    }

    updateMetric(metric){
        const url = '${API_URL}/api/valuationMetrics/${valuationMetric.pk}';
        const headers = {Authorization: 'Bearer ${AuthService.getAuthToken()}'};
        return axios.put(url,metric,{headers: headers});
  }
}
