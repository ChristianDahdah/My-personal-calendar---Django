$(function(){

    $('#assignee_name').keyup(function() {
    
        $.ajax({
            type: "POST",
            url: "/taskmanager/searchassignee",
            data: { 
                'search_assignee' : $('#assignee_name').val(),
                'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
            },
            success: searchSuccess,
            dataType: 'html'
        });
        
    });

});

function searchSuccess(data, textStatus, jqXHR)
{
    $('#search-results').html(data);
}