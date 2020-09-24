$.getJSON('https://swapi-api.hbtn.io/api/people/5/?format=json', (data) => {
  let name = data['name'];
  $("#character").text(name);
})
