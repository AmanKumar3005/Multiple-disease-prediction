<?php
// Retrieve the form data
if(isset($_POST['name'])){
$name = $_POST['name'];
$phone = $_POST['phone'];
$email = $_POST['email'];
$password = $_POST['password'];

// Connect to the database
$servername = "localhost"; // Replace with your server name
$username = "root"; // Replace with your database username
$password1 = ""; // Replace with your database password
$dbname = "healthcare";

$conn = new mysqli($servername, $username, $password1, $dbname);

// Check the connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Prepare and execute the SQL query to insert the user data
$sql = "INSERT INTO users (name, phone, email, password) VALUES ('$name', '$phone', '$email', '$password')";

if ($conn->query($sql) === TRUE) {
    header("location:login.html");
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

// Close the database connection
$conn->close();
}
?>
