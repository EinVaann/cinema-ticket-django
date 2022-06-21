var movies = document.getElementById("id_movie_id");
var start_time = document.getElementById("id_start_time")
var end_time = document.getElementById("id_end_time")
movies.addEventListener("change", function() {
    var input = start_time.value;
    var data_from_django = document.getElementById("data_from_django").innerHTML; 
    data_from_django = data_from_django.slice(1, -1); 
    const words = data_from_django.split(',');
    const dur = parseInt(words[movies.selectedIndex-1])
    var t = input.split(':')
    var h = parseInt(t[0])
    var m = parseInt(t[1])
    m = m + dur
    h = h + Math.floor(m/60)
    m = m % 60
    end_time.value = h+':'+m
});