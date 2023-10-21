document
  .getElementById("checkoutForm")
  .addEventListener("submit", function (e) {
    var paymentMethods = document.getElementsByName("payment");
    var paymentSelected = false;

    for (var i = 0; i < paymentMethods.length; i++) {
      if (paymentMethods[i].checked) {
        paymentSelected = true;
        break;
      }
    }

    if (!paymentSelected) {
      alert("Please select a payment method.");
      e.preventDefault();
    }
  });
