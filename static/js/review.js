
$(function() {
    // Initialize the star rating widget
    $("#rating-stars").rateYo({
        onSet: function(rating, rateYoInstance) {
            // Update the hidden input field with the numerical rating
            $("#rating-input").val(rating);
        }
    });

    // Handle form submission
    $("#review-form").submit(function(e) {
        e.preventDefault();

        // Submit the form with the numerical rating and comment
        $.ajax({
            url: "{% url 'your_submit_url' %}",  // Replace with the actual URL for form submission
            method: "POST",
            data: $("#review-form").serialize(),
            success: function(data) {
                // Handle success response
                console.log("Review submitted successfully.");
            },
            error: function() {
                // Handle error
                console.error("Error submitting review.");
            }
        });
    });
});

