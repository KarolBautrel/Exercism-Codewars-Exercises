var isSquare = function (n) {
    var number = Math.pow(n, 2)
    if (Number.isInteger(number) === true) {
        return true;
    } else return false;
}


var isSquare = function (n) {
    return Number.isInteger((Math.sqrt(n)))
}