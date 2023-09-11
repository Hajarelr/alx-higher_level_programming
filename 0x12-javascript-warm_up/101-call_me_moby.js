#!/usr/bin/node
module.exports = {
  /**
   * callMeMoby - Function that invokes a function x times
   * @param {Number} x : The number of times to invoke the function.
   * @param {Number} theFunction : The function to be invoked.
   */
  callMeMoby: function (x, theFunction) {
    for (let n = 0; n < x; n++) {
      theFunction();
    }
  }
};
