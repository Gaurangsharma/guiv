<?php
$username=$_POST["username"];
$password=$_POST["password"];
$phone=$_POST["phone"];
$email=$_POST["email"];
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
$stmt = $conn->prepare("insert into user (name,email,phone,password) values(?,?, ?, ?)");
$stmt->bind_param("ssss", $username, $email, $phone,$password);
$stmt->execute();

echo "New records created successfully";

$stmt->close();
$conn->close();
?>