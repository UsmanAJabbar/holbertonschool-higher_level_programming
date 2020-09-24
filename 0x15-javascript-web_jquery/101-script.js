$(document).ready(() => {
  $('#add_item').click(() => {
    $('.my_list').append('<li>Item</li>');
  });

  // $('#remove_list').click(() => {
    // let li = $('.my_list li');
    // alert(li);
  // });

  $('#clear_list').click(() => {
    $('.my_list li').each((index, li) => {
      li.remove();
    })
  });

});
