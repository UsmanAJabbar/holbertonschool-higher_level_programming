#!/usr/bin/node
// Counts the number of tasks each user has completed
const req = require('request');
const url = process.argv[2];

if (url !== undefined) {
  req(url, (err, response, jsonstr) => {
    const json = JSON.parse(jsonstr);
    const tasks = {};

    for (const objects of json) {
      // If the user ID doesn't exist in the dictionary, add it
      if (tasks[objects.userId] === undefined) {
        tasks[objects.userId] = 0;
      }

      // Else, check if the task was completed
      if (objects.completed) {
        tasks[objects.userId] += 1;
      }
    }
    console.log(tasks);
  });
}
