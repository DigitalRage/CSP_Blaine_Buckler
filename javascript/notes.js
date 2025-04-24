let images = ["https://upload.wikimedia.org/wikipedia/en/4/44/Crash_Bandicoot_Cover.png", "https://static.tvtropes.org/pmwiki/pub/images/cashbanooca.png", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRzlPDIGglIikjE4_uXmPpzjGOaP9ePdxNTjw&s"]
function hello(){
    document.getElementById("title"). innerHTML = "Hello World!"
}

    count = 0
function change(){
    document.getElementById("img").src = images[count]
    if (count === 2){
        count = 0
    }else{
        count += 1
    }
}

function highlight(){
    document.getElementById("btn").style.backgroundColor = "orange"
    document.getElementById("btn").style.backgroundColor = "white"
}
function normal(){
    
    document.getElementById("btn").style.backgroundColor = "black"
    document.getElementById("btn").style.backgroundColor = "gray"
}
function show(){
    document.getElementById("hidden").style.display = "block"
}

function more(){
    if(document.getElementById("extra").style.display != "flex"){
    document.getElementById("extra").style.display = "flex" 
    document.getElementById("shw").innerHTML = "Show Less"
    }else{
        document.getElementById("extra").style.display = "none"
    document.getElementById("shw").innerHTML = "Show More"
    }
}
