import { createClient } from "redis";

const client = createClient();

await client.connected()
.then((error) => {
  if (error) { console.log(`Redis client not connected to the server: ${error}`)};
  console.log("Redis client connected to the server");
});
