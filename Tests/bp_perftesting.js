import http from 'k6/http';
import { sleep } from 'k6';
export let options = {
    stages: [
        { duration: '30s', target: 20 },
        { duration: '1m30s', target: 10 },
        { duration: '20s', target: 0 },
      ],

  ext: {
    loadimpact: {
      projectID: 3516378,
      // Test runs with the same name groups test runs together
    }
  }
};

export default function() {
  http.get('http://rayperry-qa-bpcalculator.azurewebsites.net/');
  sleep(1);
}