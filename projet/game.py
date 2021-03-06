<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>STONE PAPER SCISSOR</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>

</head>
<body>
<div class="container">
    <div class="row">
        <div class="col-md-6 text-center" style="font-size: 50px">USER</div>
        <div class="col-md-6 text-center" style="font-size: 50px">COMPUTER</div>
    </div>
    <div class="row">
        <img height="400" class="col-md-6" id="user" src="" alt="Not Selected">
        <img height="400" class="col-md-6" id="system" src="" alt="Not Selected">
    </div>
    <div class="row">
        <div class="col-md-6" style="border: 2px solid black;">
            <button class="btn btn-outline-primary user ml-4 col-md-3" data-cap="1" >Stone</button>
            <button class="btn btn-outline-success user ml-4 col-md-3" data-cap="2">Paper</button>
            <button class="btn btn-outline-danger user ml-4 col-md-3" data-cap="3">Scissor</button>
        </div>
        <div class="col-md-6" style="border: 2px solid black;">
            <button class="btn btn-outline-warning system col-md-12" >Computer</button>
        </div>
        <div class="col-md-12 text-center" id="result" style="border: 2px solid black;font-size: 50px">

        </div>
    </div>
</div>
<script>
    $(document).ready(function () {
        var user;
        var i;
       $('.user').click(function (event) {
           if (event.target.getAttribute('data-cap')==1){
               user=1;
               $('#user').attr('src','stone.png');
           } else if(event.target.getAttribute('data-cap')==2){
               user=2;
               $('#user').attr('src','paper.png');
           } else{
               user=3;
               $('#user').attr('src','scissor.png');
           }
       });
       $('.system').click(function () {
           i = Math.floor((Math.random() * 3) + 1);
           if (i==1){
               $('#system').attr('src','stone.png');
           } else if (i==2){
               $('#system').attr('src','paper.png');
           } else {
               $('#system').attr('src','scissor.png');
           }
           if ((user==1 && i==2) || (user==2 && i==3) || (user==3 && i==1)){
               $('#result').text('You Lose!!');
           } else {
               $('#result').text('You Win!!');
           }
       });
    });
</script>
</body>
</html>