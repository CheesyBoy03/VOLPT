"use strict";

function Check() {
  //  Получаем все предметы
  var subjects = document.querySelectorAll('.subs'); // Физика Математика История

  var li = document.querySelector('.li');

  for (var l = 0; l < subjects.length; l++) {
    if (subjects[l] == ' ') {
      subjects[l].replace(' ', '<br>');
    }
  }

  var result = [];
  var elem = '<li>';
  var _iteratorNormalCompletion = true;
  var _didIteratorError = false;
  var _iteratorError = undefined;

  try {
    for (var _iterator = subjects[Symbol.iterator](), _step; !(_iteratorNormalCompletion = (_step = _iterator.next()).done); _iteratorNormalCompletion = true) {
      var subject = _step.value;
      subject = subject.textContent;
      var _iteratorNormalCompletion2 = true;
      var _didIteratorError2 = false;
      var _iteratorError2 = undefined;

      try {
        for (var _iterator2 = subject[Symbol.iterator](), _step2; !(_iteratorNormalCompletion2 = (_step2 = _iterator2.next()).done); _iteratorNormalCompletion2 = true) {
          var letter = _step2.value;

          if (letter == ' ') {
            elem += '</li>';
            result.push(elem);
            elem = '<li>';
          } else {
            elem += letter;
          }
        }
      } catch (err) {
        _didIteratorError2 = true;
        _iteratorError2 = err;
      } finally {
        try {
          if (!_iteratorNormalCompletion2 && _iterator2["return"] != null) {
            _iterator2["return"]();
          }
        } finally {
          if (_didIteratorError2) {
            throw _iteratorError2;
          }
        }
      }
    }
  } catch (err) {
    _didIteratorError = true;
    _iteratorError = err;
  } finally {
    try {
      if (!_iteratorNormalCompletion && _iterator["return"] != null) {
        _iterator["return"]();
      }
    } finally {
      if (_didIteratorError) {
        throw _iteratorError;
      }
    }
  }

  console.log(result); //  Получаем все предметы
  //  Оформляем предметы

  for (var _i = 0, _result = result; _i < _result.length; _i++) {
    var Item = _result[_i];
    li.innerHTML += Item;
  }
}

;
document.addEventListener("DOMContentLoaded", Check);