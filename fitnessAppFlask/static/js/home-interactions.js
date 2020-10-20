const buttons = document.querySelectorAll('a');
buttons.forEach(btn => {
    btn.addEventListener('click', function(e) {
        
        let x = e.clientX - e.target.offsetLeft;
        let y = e.clientY - e.target.offsetTop;

        let ripples = document.createElement('span');
        ripples.style.left = x + 'px';
        ripples.style.top = x + 'px';
        this.appendChild(ripples);

        setTimeout(() => {
            ripples.remove()
            }, 1000);
    })
})

function switchLayout() {
    var icon = document.getElementById("layout-icon");
    var para = document.getElementById("layout-paragraph");
    if (icon.style.display === "none") {
        icon.style.display = "block";
        para.style.display = "none";
    } else {
        icon.style.display = "none";
        para.style.display = "block";
    }
  } 

