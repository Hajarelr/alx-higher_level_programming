#!/usr/bin/node
exports.esrever = function (list) {
  const rev = [];
  for (let n = 0; n < list.length; n++) {
    rev.unshift(list[n]);
  }
  return rev;
};
