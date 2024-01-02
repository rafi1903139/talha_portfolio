document.addEventListener('DOMContentLoaded', ()=>{
    highlightNavbar();
})

function highlightNavbar()
{
    var title = document.querySelector('title').innerHTML.trim()
    var navbar = document.querySelectorAll('.nav-link')
   
    for (nav of navbar){
        navSection = nav.innerHTML.trim()
        
        if (navSection == title)
        {
            
            nav.classList.add('active')
            nav.classList.add('underline')
        }
        else 
        {
            nav.classList.remove('active')
            nav.classList.remove('underline')
        }
    }
    
}