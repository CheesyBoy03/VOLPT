"use strict";

var popup = document.querySelector('.popup'); //Закрытие модального окна

function close_window() {
  popup.classList.remove('open');
} //Открытие модального окна


function open_menu() {
  popup.classList.add('open');
}