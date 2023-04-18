vwidth = screen.width;
vheight = screen.height;

channelI = document.getElementById("channel");
volI = document.getElementById("vol");

channelO = document.getElementById("chValue");
volO = document.getElementById("volValue");

channelI.addEventListener('change', function (evt) {
    channelO.innerHTML = channelI.value;
});

volI.addEventListener('change', function (evt) {
    volO.innerHTML = volI.value;
});