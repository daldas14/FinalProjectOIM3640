var statCards = document.getElementsByClassName('stat-card');
var categoryItems = document.getElementsByClassName('category-item');
var topItems = document.getElementsByClassName('top-item');
var bars = document.getElementsByClassName('bar');

for (var i = 0; i < statCards.length; i++) {
    statCards[i].onmouseover = function() {
        this.style.transform = 'scale(1.05)';
    };
    statCards[i].onmouseout = function() {
        this.style.transform = 'scale(1)';
    };
}

for (var i = 0; i < categoryItems.length; i++) {
    categoryItems[i].onmouseover = function() {
        this.style.transform = 'translateX(10px)';
    };
    categoryItems[i].onmouseout = function() {
        this.style.transform = 'translateX(0)';
    };
}

for (var i = 0; i < topItems.length; i++) {
    topItems[i].onmouseover = function() {
        this.style.transform = 'scale(1.02)';
        this.style.boxShadow = '0 0 15px orange';
    };
    topItems[i].onmouseout = function() {
        this.style.transform = 'scale(1)';
        this.style.boxShadow = 'none';
    };
}

for (var i = 0; i < bars.length; i++) {
    bars[i].onmouseover = function() {
        this.style.boxShadow = '0 0 20px orange';
    };
    bars[i].onmouseout = function() {
        this.style.boxShadow = 'none';
    };
}