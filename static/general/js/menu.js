"use strict";

var navmenu = document.getElementById('menu');

function actionWithMenu() {
  if (navmenu.className === "links") {
    navmenu.className += " topnav";
  } else {
    navmenu.className = 'links';
  }
}