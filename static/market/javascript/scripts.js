const menuBtn = document.getElementById('menu-btn')
const menuLinks = document.getElementById('links')

const notify = document.querySelector('.notify')


var t = window.setTimeout(()=>{
		console.log(notify)
		notify.style.display = 'none';
	}, 5000)

const toggle =()=>{
    if(menuLinks.style.display == 'none'){
        menuLinks.style.display = 'flex'
        menuBtn.className = 'fa fa-times'
    }
    else{
        menuLinks.style.display = 'none'
        menuBtn.className='fa fa-bars'
    }
}


menuBtn.addEventListener('click',toggle)


