/**
 * Created by Midoki on 31/05/2017.
 */
(function() {
  var button, buttonStyles, materialIcons;

  materialIcons = '<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">';

  buttonStyles = '<link href="https://codepen.io/andytran/pen/vLmRVp.css" rel="stylesheet">';

  button = '<a href="http://www.aiac.ma/" class="at-button"><i class="material-icons">link</i></a>';

  document.body.innerHTML += materialIcons + buttonStyles + button;

}).call(this);