$('.modal').on('shown.bs.modal', function() {
    $(this).find('[autofocus]').focus();
});

// $('#left_city_selector').click( function() {
//     $('#city_post_name').innerHTML('{{ city.city }}');
// });
