import { creatClient } from "redis";

const client = createClient();

client.on('error', (error) => {
  if (error) {
    console.log(`Redis client not connected to the server: ${error}`);
  }
})

const conn = client.connect();
conn.then(resp => {
  console.log('Redis client connected to the server');
});
