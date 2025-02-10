document.getElementById("registrationForm").addEventListener("submit", function (e){
    e.preventDefault();
    const errors = document.querySelectorAll(".error");
    errors.forEach((error) => (error.textContent = ""));

    let isValid = true;

    const fullName = document.getElementById("fullName").value.trim();
    if (!fullName) {
        document.getElementById("nameError").textContent = "Full name is required.";
        isValid = false;
    }

    const username = document.getElementById("username").value.trim();
    if (!username) {
        document.getElementById("usernameError").textContent = "Username is required.";
        isValid = false;
    }

    const email = document.getElementById("email").value.trim();
    const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    if (!email || !emailPattern.test(email)) {
        document.getElementById("emailError").textContent = "Valid email is required.";
        isValid = false;
    }

    const phoneNumber = document.getElementById("phoneNumber").value.trim();
    const phonePattern = /^[6-9][0-9]{9}$/;
    if (!phoneNumber || !phonePattern.test(phoneNumber)) {
        document.getElementById("phoneError").textContent = "Please enter a valid 10-digit phone number.";
        isValid = false;
    }

    const password = document.getElementById("password").value.trim();
    if (password.length < 6) {
        document.getElementById("passwordError").textContent = "Password must be at least 6 characters.";
        isValid = false;
    }

    const confirmPassword = document.getElementById("confirmPassword").value.trim();
    if (password !== confirmPassword) {
        document.getElementById("confirmPasswordError").textContent = "Passwords do not match.";
        isValid = false;
    }

    const gender = document.querySelector('input[name="gender"]:checked');
    if (!gender) {
        document.getElementById("genderError").textContent = "Select gender.";
        isValid = false;
    }
    if (isValid) {
        window.location.href = '/welcome?username=' + encodeURIComponent(username);
    }
});

