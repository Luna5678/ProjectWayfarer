$('.modal').on('shown.bs.modal', function() {
    $(this).find('[autofocus]').focus();
});

$(document).ready(function(){
    $("#post_submit").change(function() {
        $(this).closest("form").submit();
    });
});

$(document).ready(function() {      
    if (window.location.pathname == "/accounts/signup/") {
        $('#signup_modal').modal('show');
    } else if (window.location.pathname == "/accounts/login/") {
        $('#signin_modal').modal('show');
    };
});