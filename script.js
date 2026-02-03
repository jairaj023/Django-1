function validation() {
    var username = document.myform.name.value.trim();
    var mail = document.myform.email.value.trim();
    var number = document.myform.no.value.trim();
    var password = document.myform.pass.value.trim();
    var cpass = document.myform.cpass.value.trim();

    if (username == "")
    {
        alert("Please fill name!");
        return false;
    }
    if (!isNaN(username))
    {
        alert("Use only alphabet!");
        return false;
    }
    if ((username.length < 5 )||(username.length > 15))
    {
        alert("Name must be between 5 to 15 characters!");
        return false;
    }
    if (mail == "")
    {
        alert("Please fill e-mail!");
        return false;
    }

    var atposition = mail.indexOf("@");
    var dotposition = mail.lastIndexOf(".");
    if (atposition < 1 || dotposition < atposition + 2 || dotposition + 2 >= mail.length)
    {  
        alert("Please enter a valid e-mail address \n atpostion:"+atposition+"\n dotposition:"+dotposition);  
        return false;  
    }  
    if(number == "")
    {
        alert("please fill your mobile number");
        return false;
    }
    //if(!isNaN(number))              
    //{
      //  alert("please fill only numeric number");
       // return false;
               
    //}
    if(number.length != 10)
    {
        alert("number must be 10 digits");
        return false;
    }
    if (password == "")
    {
        alert("Please enter your password!");
        return false;
    }
    if ((password.length <= 8))
    {
        alert("Must be greater than 8 characters!");
        return false;
    }
    if (cpass == "")
    {
        alert("Please confirm your password!");
        return false;
    }
    if (cpass != password)
    {
        alert("Please try again!");
        return false;
    }
}
