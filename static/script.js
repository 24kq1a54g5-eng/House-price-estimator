function predictPrice() {

    let area = Number(document.getElementById("area").value);
    let bedrooms = Number(document.getElementById("bedrooms").value);
    let bathrooms = Number(document.getElementById("bathrooms").value);
    let age = Number(document.getElementById("age").value);

    // Check if all fields are filled
    if (!area || !bedrooms || !bathrooms || age < 0) {
        document.getElementById("result").innerHTML =
            "<h2 style='color:red;'>Please fill all fields correctly.</h2>";
        return;
    }

    // Sample price calculation
    let price = (area * 5000) +
                (bedrooms * 200000) +
                (bathrooms * 100000) -
                (age * 10000);

    document.getElementById("result").innerHTML =
        "<h2>Estimated House Price: ₹" + price.toLocaleString("en-IN") + "</h2>";
}