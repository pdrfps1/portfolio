const btn = document.querySelector(".switch");
const theme = document.querySelector("#theme-link");
btn.addEventListener("click", function(){
    if (theme.getAttribute("href") == "../styles/dark-mode.css"){
        theme.href = "../styles/light-mode.css";
    }else{
        theme.href = "../styles/dark-mode.css";
    }
});

