  function getParams(url) {
    var params = { };
    var parser = document.createElement('a');
    parser.href = url;
    var query = parser.search.substring(1);
    var vars = query.split('&');
    for (var i = 0; i < vars.length; i++) {
        var pair = vars[i].split('=');
        params[pair[0]] = decodeURIComponent(pair[1]);
    }
    return params;
}

function configureDownloadLinks() {
    var params = getParams(window.location.href);
    console.log(params);
    var br = document.createElement("br");
    document.body.appendChild(br);
    console.log(params[0]);
    if (params["file"] != undefined) {
        var anchor = document.createElement("a");
        anchor.href = "/static/crop/images/" + params["file"] + ".zip";
        anchor.innerHTML = "Download Photos";
        document.body.appendChild(anchor);
    }
}
