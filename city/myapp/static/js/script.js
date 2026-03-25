function goToReport() {
    window.location.href = "/add-report/";
}

console.log("Smart City JS Loaded Successfully!");

// Mobile nav toggle
document.addEventListener('DOMContentLoaded', function(){
    const toggle = document.getElementById('nav-toggle');
    const nav = document.getElementById('main-nav');
    if(toggle && nav){
        toggle.addEventListener('click', function(){
            if(nav.style.display === 'flex' || nav.style.display === ''){
                nav.style.display = 'none';
            } else {
                nav.style.display = 'flex';
            }
        });
    }
});

// Interactive report filtering and modal
document.addEventListener('DOMContentLoaded', function(){
    const search = document.getElementById('report-search');
    const category = document.getElementById('report-category');
    const clear = document.getElementById('clear-filters');
    const cards = document.querySelectorAll('.report-card');
    const modal = document.getElementById('report-modal');
    const modalClose = modal && modal.querySelector('.modal-close');

    function applyFilters(){
        const q = search ? search.value.trim().toLowerCase() : '';
        const cat = category ? category.value : '';
        cards.forEach(c => {
            const title = c.dataset.title || '';
            const ccat = c.dataset.category || '';
            const matchesQ = !q || title.indexOf(q) !== -1;
            const matchesCat = !cat || ccat === cat;
            c.style.display = (matchesQ && matchesCat) ? '' : 'none';
        });
    }

    if(search){ search.addEventListener('input', applyFilters); }
    if(category){ category.addEventListener('change', applyFilters); }
    if(clear){ clear.addEventListener('click', function(){ if(search) search.value=''; if(category) category.value=''; applyFilters(); }); }

    // modal open
    cards.forEach(c => {
        c.addEventListener('click', openCardModal);
        c.addEventListener('keypress', function(e){ if(e.key=== 'Enter') openCardModal.call(this,e); });
    });

    function openCardModal(e){
        if(!modal) return;
        const img = modal.querySelector('.modal-image img');
        const title = modal.querySelector('.modal-title');
        const desc = modal.querySelector('.modal-desc');
        const cat = modal.querySelector('.modal-category');
        const st = modal.querySelector('.modal-status');

        img.src = this.dataset.image || '/static/img/placeholder.png';
        title.textContent = this.dataset.title || 'Report';
        desc.textContent = this.dataset.description || '';
        cat.textContent = (this.dataset.category || 'Unknown').replace(/_/g,' ');
        st.textContent = this.dataset.status || '';

        modal.style.display = 'flex';
        modal.setAttribute('aria-hidden','false');
    }

    if(modalClose){ modalClose.addEventListener('click', function(){ modal.style.display='none'; modal.setAttribute('aria-hidden','true'); }); }
    // close when clicking outside modal content
    if(modal){ modal.addEventListener('click', function(e){ if(e.target === modal){ modal.style.display='none'; modal.setAttribute('aria-hidden','true'); } }); }

});

// Smooth scroll for anchor links and back-to-top button
document.addEventListener('DOMContentLoaded', function(){
    // Smooth scroll for in-page links
    document.querySelectorAll('a[href^="#"]').forEach(function(anchor){
        anchor.addEventListener('click', function(e){
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if(target){ target.scrollIntoView({behavior: 'smooth', block: 'start'}); }
        });
    });

    const back = document.getElementById('back-to-top');
    window.addEventListener('scroll', function(){
        if(window.scrollY > 300){ back.style.display = 'block'; } else { back.style.display = 'none'; }
    });
    if(back){ back.addEventListener('click', function(){ window.scrollTo({top:0, behavior:'smooth'}); }); }
});
