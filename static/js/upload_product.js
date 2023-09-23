$(document).ready(function () {
    $('#id_product_name').on('input', function () {
        var product_name = $(this).val();
        var slug = product_name.toLowerCase().replace(/ /g, '-');
        $('#id_slug').val(slug);
    });
});

document.addEventListener("DOMContentLoaded", function() {
    var isAvailableCheckbox = document.getElementById("id_is_available");
    if (isAvailableCheckbox) {
        isAvailableCheckbox.checked = true;
    }
});