const fs = require("fs");

const originalData = fs.readFileSync("input_2750.txt", "utf-8");

const splitData = originalData
  .split("")
  .map((data) => Number(data))
  .filter((data) => typeof data === "number" && data !== 0)
  .splice(1)
  .sort()
  .join("\n");

console.log(splitData);
