               <link rel="stylesheet" href="{% static "css/dropdown.css" %}">
                <script src="{% static "js/dropdown.js" %}"></script>
                <div class="dropdown">
                    <div onclick="myFunction()" class="dropbtn">Dropdown
                        <div><small class='dropsmall'>UGX 28000</small></div> 
                    </div>
                <div id="myDropdown" class="dropdown-content">
                    <p class="dropsmall">MY STUFF</p>
                    <a href="#">My Profile</a>
                    <a href="#">Messages</a>
                    <a href="#">Log Out</a>
                </div>
            </div>


            /* Dropdown Button */
.dropbtn {
    color: black;
    padding: 3px;
    font-size: 12px;
    border: none;
    cursor: pointer;
    background-color: white;
    width: 100px;
}

/* Dropdown button on hover & focus */
.dropbtn:hover, .dropbtn:focus {
    background-color: rgb(250, 250, 250);
    border-color: none;
}

/* The container <div> - needed to position the dropdown content */
.dropdown {
    position: relative;
    display: inline-block;
}

/* Dropdown Content (Hidden by Default) */
.dropdown-content {
    display: none;
    position: absolute;
    background-color: white;
    min-width: 100px;
    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
    z-index: 1;
    border: 1px solid;
    border-left: #ddd;
    border-right: #ddd;
    border-bottom: #ddd;
    border-radius: 0 0 5px 5px;
}

/* Links inside the dropdown */
.dropdown-content a {
    color: black;
    padding: 2px 11px;
    text-decoration: none;
    display: block;
    font-size: 12px;
}

/* Change color of dropdown links on hover */
.dropdown-content a:hover {background-color: #ddd}

/* Show the dropdown menu (use JS to add this class to the .dropdown-content container when the user clicks on the dropdown button) */
.show {display:block;}

.dropsmall {
    color: rgb(83, 83, 83);
    font-size: 9px;
    padding-left: 3px;
    margin-top: 2px;
    margin-bottom: 2px;
}


/* When the user clicks on the button, 
toggle between hiding and showing the dropdown content */
function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
}

// Close the dropdown menu if the user clicks outside of it
window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {

    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}