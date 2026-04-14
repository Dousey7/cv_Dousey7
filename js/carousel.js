document.addEventListener('DOMContentLoaded', function() {
    const track = document.querySelector('.carousel-track');
    const prevBtn = document.querySelector('.prev');
    const nextBtn = document.querySelector('.next');
    const dotsContainer = document.querySelector('.carousel-dots');
    
    if (!track || !prevBtn || !nextBtn) return;
    
    const slides = Array.from(track.children);
    let currentIndex = 0;
    
    // Définir le nombre de slides visibles selon la largeur d'écran
    const getSlidesToShow = () => {
        if (window.innerWidth <= 480) return 2;
        if (window.innerWidth <= 768) return 3;
        return 4;
    };
    
    // Calculer la largeur d'un slide (incluant le gap)
    const getSlideWidth = () => {
        const slide = slides[0];
        const slideStyles = window.getComputedStyle(slide);
        const slideWidth = slide.offsetWidth;
        const gap = parseInt(window.getComputedStyle(track).gap) || 30;
        return slideWidth + gap;
    };
    
    // Mettre à jour la position du carousel
    const updateCarousel = () => {
        const slideWidth = getSlideWidth();
        const slidesToShow = getSlidesToShow();
        const maxIndex = Math.max(0, slides.length - slidesToShow);
        
        // Empêcher de dépasser les limites
        if (currentIndex < 0) currentIndex = 0;
        if (currentIndex > maxIndex) currentIndex = maxIndex;
        
        const moveAmount = currentIndex * slideWidth;
        track.style.transform = `translateX(-${moveAmount}px)`;
        
        // Activer/désactiver les boutons
        prevBtn.disabled = currentIndex === 0;
        nextBtn.disabled = currentIndex === maxIndex;
        
        // Mettre à jour les dots
        updateDots();
    };
    
    // Créer les dots
    const createDots = () => {
        const slidesToShow = getSlidesToShow();
        const numDots = Math.max(1, slides.length - slidesToShow + 1);
        
        dotsContainer.innerHTML = '';
        for (let i = 0; i < numDots; i++) {
            const dot = document.createElement('button');
            dot.classList.add('dot');
            dot.dataset.index = i;
            dot.addEventListener('click', () => {
                currentIndex = i;
                updateCarousel();
            });
            dotsContainer.appendChild(dot);
        }
    };
    
    // Mettre à jour les dots actifs
    const updateDots = () => {
        const dots = document.querySelectorAll('.dot');
        dots.forEach((dot, index) => {
            if (index === currentIndex) {
                dot.classList.add('active');
            } else {
                dot.classList.remove('active');
            }
        });
    };
    
    // Événements des boutons
    prevBtn.addEventListener('click', () => {
        currentIndex--;
        updateCarousel();
    });
    
    nextBtn.addEventListener('click', () => {
        currentIndex++;
        updateCarousel();
    });
    
    // Recalculer quand la fenêtre est redimensionnée
    let resizeTimeout;
    window.addEventListener('resize', () => {
        clearTimeout(resizeTimeout);
        resizeTimeout = setTimeout(() => {
            const maxIndex = Math.max(0, slides.length - getSlidesToShow());
            if (currentIndex > maxIndex) {
                currentIndex = maxIndex;
            }
            createDots();
            updateCarousel();
        }, 150);
    });
    
    // Initialisation
    createDots();
    updateCarousel();
});