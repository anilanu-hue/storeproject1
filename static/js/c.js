$("select").replaceWith(buttons);
*/

$("select option").unwrap().each(function() {
    var btn = $('<div class="btn">'+$(this).text()+'</div>');
    if($(this).is(':checked')) btn.addClass('on');
    $(this).replaceWith(btn);
});

$(document).on('click', '.btn', function() {
    $('.btn').removeClass('on');
    $(this).addClass('on');
});