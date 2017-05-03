#!/usr/bin/node
$(document).ready(function () {
  const request = require('request');

  $('INPUT#city_search').keypress(function (e) {
    if (e.which === 13) {
      $('#btn_search').click();
    }
  });

  $('#btn_search').on('click', function () {
    let cityName = $('#city_search').val();
    $('#city_search').val('');

    let url = 'https://query.yahooapis.com/v1/public/yql?q=select%20wind%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22' + cityName + '%22)&format=json';

    request(url, (err, res, body) => {
      if (err) {
        return console.log(err);
      }

      $('DIV#wind_speed').text(JSON.parse(body).query.results.channel.wind.speed);
    });
  });
});
