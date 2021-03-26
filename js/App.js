{
    const items = Array.from(document.querySelectorAll('.aside__item'));
    const links = Array.from(document.querySelectorAll('.aside__link'));
    items.forEach(item => {
        item.addEventListener('click',e => {
          const self = e.target;
            items.forEach(cur => {
                cur.classList.remove('active')
            })
            self.classList.add('active');
        })

       
    })
}