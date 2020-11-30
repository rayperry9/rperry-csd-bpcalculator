import http from 'k6/http';
import { sleep } from 'k6';
export let options = {
  vus: 10,
  duration: '30s',

  ext: {
    loadimpact: {
      projectID: 3516378,
      // Test runs with the same name groups test runs together
      name: "YOUR TEST NAME"
    }
  }
};

export default function() {
  http.get('http://rayperry-qa-bpcalculator.azurewebsites.net/');
  sleep(1);
}