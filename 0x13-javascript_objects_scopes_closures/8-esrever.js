#!/usr/bin/node

exports.esrever = function (list) {
  const RevList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    RevList.push(list[i]);
  }
  return (RevList);
};
