import http from 'k6/http';
import { sleep } from 'k6';
export let options = {
    ext: {
        loadimpact: {
          projectID: 3516378,
          }
         }
  vus: 10,
  duration: '30s',
};

export default function() {
  http.get('http://rayperry-qa-bpcalculator.azurewebsites.net/');
  sleep(1);
}