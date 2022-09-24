let formFile = document.getElementById("FormImageFile")
formFile.onchange = function (e) {
    let image = document.getElementById('outputImage');
    image.src = URL.createObjectURL(e.target.files[0]);

    $('#alert-error').hide();
    $('#result').html('');

}

$(document).ready(function (e) {
    $('#alert-error').hide();
    $('#result').html('');
    $('#predictButton').on('click', function () {
        let file_data = $('#FormImageFile')[0].files[0];
        let form_data = new FormData();
        form_data.append('file', file_data);
        $('#result').html('');
        $('#alert-error').hide();
        $.ajax({
            url: '/predict',
            cache: false,
            contentType: false,
            processData: false,
            data: form_data,
            type: 'post',
            success: function (response) {
                if (response === false) {
                    $('#alert-error').show();
                } else {
                    $('#alert-error').hide();
                    var message = `<div class="alert alert-success" role="alert"> ${response}
                    </div>`
                    $('#result').html(message);
                }
            },complete: function (response) {
            },
            error: function (response) {
                $('#result').html("Fail Please Try Again");
            }
        });
    });
});
