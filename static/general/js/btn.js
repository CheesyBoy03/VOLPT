"use strict";

var popup = document.querySelector('.popup');

function close_window() {
  popup.classList.remove('open');
}

function open_menu() {
  popup.classList.add('open');
}