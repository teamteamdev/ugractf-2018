triplesec.encrypt ({
    data: new triplesec.Buffer("ugra_alliance_cors_secrets_revealed"),
    key:  new triplesec.Buffer("correcthorsebatterystaple")
}, function(err, buff) {
    if (!err)
        console.log(buff.toString('hex'));
});
