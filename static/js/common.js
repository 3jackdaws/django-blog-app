function Form2Object(form){
    let data = $(form).serializeArray();
    let obj = {};

    $.each(data, function (i, param) {
        obj[param.name] = param.value;
    });
    return obj;
}

function AjaxForm(event, callback){
    event.preventDefault();
    let form = event.target;
    let formData = Form2Object(form) || null;

    let action = form.getAttribute("action") || "/";
    let method = (form.getAttribute("method") || "GET").toUpperCase();

    $.ajax({
        url: action,
        method: method,
        data: formData,
        complete: function(response){
            console.info(response);
            if(callback) callback(response.status, response.responseJSON || response.responseText);
        }

    })
}