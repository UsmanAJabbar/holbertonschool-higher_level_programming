$.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', (data) => {
  let greetings = data['hello'];
  $("#hello").text(greetings);
})
