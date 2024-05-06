function toggleMenu() {
    var navLinks = document.getElementById("navLinks");
    if (navLinks.style.display === "flex") {
      navLinks.style.display = "none";
    } else {
      navLinks.style.display = "flex";
    }
  }
  

  function getLocation() {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(showPosition);
    } else {
      alert("Geolocation is not supported by this browser.");
    }
  }

  function showPosition(position) {
    var latitude = position.coords.latitude;
    var longitude = position.coords.longitude;
    var accuracy = position.coords.accuracy;

    var link = document.createElement('a');
    link.href = "https://www.google.com/maps/place/Truba+Group+of+Institutes+Bhopal/@23.3083793,77.3820292,17z/data=!3m1!4b1!4m6!3m5!1s0x397c6884e0b907f7:0x396d52f7f5065b5b!8m2!3d23.3083744!4d77.3866426!16s%2Fm%2F0qfnpn2?entry=ttu=" + latitude + "," + longitude;
    link.target = "_blank";
    link.textContent = "Click here for live location";

    var liveLocation = document.getElementById("liveLocation");
    liveLocation.innerHTML = '';
    liveLocation.appendChild(link);
  }