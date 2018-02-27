function validatePage(questions) {
    var shouldSubmit = true;

    for (var i = 0; i < questions.length; i++) {
        if (!isOneInputChecked(questions[i], "radio")) {
            alert("Please answer all the questions before continuing.");
            return false;
        }
    }

    return true;
}

function isOneInputChecked(sel) {
    var inputs = sel.getElementsByTagName("input");
    for (var i = 0; i < inputs.length; i++) {
        if (inputs[i].checked) {
            return true;
        }
    }
    return false;
}

