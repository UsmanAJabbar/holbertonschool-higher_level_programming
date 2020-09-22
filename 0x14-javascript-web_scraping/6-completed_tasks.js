#!/usr/bin/node
// Counts the number of tasks each user has completed
const req = require('request');
const url = process.argv[2];

if (url !== undefined) {
  req(url, function (err, response, jsonstr) {
    const json = JSON.parse(jsonstr);
    const tasks = {};

    for (var objects of json) {
      if (tasks[objects.userId] === undefined) {
        tasks[objects.userId] = 0;
      }

      if (objects.completed) {
        tasks[objects.userId] += 1;
      }
    }
    console.log(tasks);
  });
}
