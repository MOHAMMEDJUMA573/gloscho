/*~~~~~~~~~~~~~~~ TOGGLE BUTTON ~~~~~~~~~~~~~~~*/
const navMenu = document.getElementById("nav-menu");
const navLinks = document.querySelectorAll(".nav-link");
const hamburger = document.getElementById("hamburger");
const themeButton = document.getElementById("theme-toggle-btn");

hamburger.addEventListener("click", ()=> {
    navMenu.classList.toggle("left-[0]");
    hamburger.classList.toggle("ri-close-large-line");
})

navLinks.forEach((link, index) =>{
    link.addEventListener("click", ()=>{
        navMenu.classList.toggle("left-[0]");
        hamburger.classList.toggle("ri-close-large-line");
    })
})
themeButton.addEventListener('click', ()=> {
    const currentTheme = document.documentElement.getAttribute('data-theme')
    if (currentTheme == 'dark') {
        document.documentElement.setAttribute('data-theme', 'light');
    }else{
        document.documentElement.setAttribute('data-theme', 'dark');
    }
})
/*for data urls */
const login = document.getElementById("loginbutton");
login.addEventListener("click", ()=> {
    window.location.href = login.dataset.url;
})
const signin = document.getElementById("signupbutton");
signin.addEventListener("click", ()=> {
    window.location.href = signin.dataset.url
})
/*Header border*/
const scrollHeader = () => {
    const header = document.getElementById("navbar")
    if (this.scrollY >= 30){
        header.classList.remove("md:border-none");
    }else{
        header.classList.add("md:border-none");
    }
}
window.addEventListener("scroll", scrollHeader)
/*Active link show */
const activeLink = () => {
    const sections = document.querySelectorAll("section")
    let current = "home"
    
    sections.forEach((section, index) => {
        const sectionTop = section.offsetTop;
        if (this.scrollY >= sectionTop -60) {
            current = section.getAttribute("id")
        }

    })

    navLinks.forEach((item, index) => {
        item.classList.remove("active")
        if (item.href.includes(current)) {
            item.classList.add("active")
        }
    })
}
window.addEventListener("scroll", activeLink)
