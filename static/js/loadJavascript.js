window.onload = (event) => {

    var script = document.getElementById('scriptJs')
    var elem = document.createElement("script");
    // add the source with a timestamp
    var dt = new Date();
    elem.src = script.getAttribute('name')+"?"+ dt.getTime().toString();
    script.parentNode.insertBefore(elem,script);
};