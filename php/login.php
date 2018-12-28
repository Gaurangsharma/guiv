<?php
$username=$_POST["username"];
$password=$_POST["password"];
$servername = "localhost";
$username = "root";
$password = "root";
$dbname = "guvi";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
echo ("connected");
$stmt = $conn->prepare("select * from user where name= $username ,password= $password);
$res= $stmt->execute();
if ($res[name]==$username && $res[password]==$password){
    echo ('sucessfully login');
    echo('<img src=\"resume_gau.PNG\" />');
}
else{

    echo " Incorrect username or password";
}
echo "New records created successfully";



?>