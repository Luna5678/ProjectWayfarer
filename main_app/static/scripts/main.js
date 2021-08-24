$('.modal').on('shown.bs.modal', function() {
    $(this).find('[autofocus]').focus();
});

$(document).ready(function(){
    $("#post_submit").change(function() {
        $(this).closest("form").submit();
    });
});