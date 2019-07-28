var update_links = function() {
  var links = document.links;
  for (var i = 0, linklen = links.length; i < linklen; i++) {
    if (links[i].hostname != window.location.hostname) {
      links[i].target = "_blank";
      links[i].setAttribute("rel", "noopender noreferrer");
      links[i].className += " external-link";
    } else {
      links[i].className += " local-link";
    }
  }
};

$(document).ready(function(){
  // $('[data-toggle="tooltip"]').tooltip();
  update_links();
})
