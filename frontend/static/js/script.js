function sendMail(){

    let parms = {
        name: document.getElementById("uname").value ,
        email : document.getElementById("email").value ,
    }
    emailjs.send("service_lx9ms2a","template_p6zy7zf",parms).then(alert("Notification Email Sent to Admin!!"))
}