let move = function() {
    let getRandomShift = function() {
        return -300 + Math.floor(Math.random() * 600);
    }
    
    let buttonBlock = document.getElementById("button-block");
    
    buttonBlock.style.top = getRandomShift() + "px";
    buttonBlock.style.left = getRandomShift() + "px";
}

document.getElementById("button").addEventListener("mouseover", move);
document.getElementsByTagName("body")[0].addEventListener("click", move);
document.getElementById("button").addEventListener("click", function() {
    alert("dWdyYXdlYmlzc291bnNlY3VyZQ==");
});
