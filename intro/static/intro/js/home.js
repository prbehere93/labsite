

// make sure all functions run after the HTML has been loaded
window.addEventListener("load", afterLoaded,false);
function afterLoaded(){
    let btn=document.querySelector("#btn");
    let sidebar=document.querySelector(".sidebar");
    let searchBtn=document.querySelector(".bx-search");
    
    btn.onclick=function(){
        sidebar.classList.toggle("active");
    }

    searchBtn.onclick=function(){
        sidebar.classList.toggle("active");
    }
}

