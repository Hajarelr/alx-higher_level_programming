#!/usr/bin/node
const dict = require('./101-data').dict;

const t = Object.entries(dict);
const v = Object.values(dict);
const u = [...new Set(v)];
const d = {};
for (const n in u) {
  const list = [];
  for (const m in t) {
    if (t[m][1] === u[n]) {
      list.unshift(t[m][0]);
    }
  }
  d[u[n]] = list;
}
console.log(d);
