window.onload = function() {
    let output = document.getElementById("flag");
    
    fetch("https://alliance.ugractf.ru/tmp.txt")
        .then(function(response) {
            if (response.status !== 200) {
                throw new RuntimeError("status == " + response.status);
                return;
            }
            return response.text();
        })
        .then(function(data) {
            triplesec.decrypt({
                data: new triplesec.Buffer(data, "hex"),
                key:  new triplesec.Buffer("correcthorsebatterystaple")
            }, function(err, buff) {
                if (err) {
                    console.log(err);
                    output.innerHTML = "Some error happened :(";
                    return;
                }
                
                output.innerHTML = buff.toString();
            });
        })
        .catch(function(err) {
            console.log(err);
            output.innerHTML = "Some error happened :(";
        });
};
