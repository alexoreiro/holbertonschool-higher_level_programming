#!/usr/bin/node
function callMeMoby (a, func) {
  for (let i = 0; i < a; i++) {
    func();
  }
}

module.exports.callMeMoby = callMeMoby;
