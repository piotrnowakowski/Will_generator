function generateWillPart(group) {
    $.ajax({
        url: '/generate-will-part',
        type: 'POST',
        contentType: 'application/json',  // This is what is missing from your current code
        data: JSON.stringify({ 'group': group }),
        dataType: 'json',
        success: function(data) {
            $('#will-text').val(data.willPart);
        }
    });
}
$('#personal-information').click(function() {
    generateWillPart('Personal Information');
});

$('#executor').click(function() {
    generateWillPart('Executor');
});

$('#administrator').click(function() {
    generateWillPart('Administator of the Estate');
});

$('#children').click(function() {
    generateWillPart('Children');
});

$('#debts-expenses').click(function() {
    generateWillPart('Debts and Expenses');
});

$('#special-gifts').click(function() {
    generateWillPart('Special Gifts and Legacies');
});
