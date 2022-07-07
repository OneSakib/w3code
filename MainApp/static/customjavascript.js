//detail.py js
if ($('#row').length > 0) {

    document.getElementById('row').onscroll = function () {
        scrollFun();
    }
}

function myFunction() {
    if ($('.con-list').length > 0) {
        $('.con-list').toggle(500)
    }
}

conlist = document.getElementById('con-list');

function scrollFun() {
    let swidth = window.screen.width;
    if (swidth <= 700) {
        conlist.style.display = "none";
    }
}

$(window).on('resize', function (e) {
    var swidth = window.screen.width;
    if (swidth > 700) {
        var container = $("#con-list").show()
    }
})
$(document).mouseup(function (e) {
    var container = $("#con-list");
    var swidth = window.screen.width;
    var icon = $('#icon');
    if (swidth < 700) {
        // if the target of the click isn't the container nor a descendant of the container
        if (!container.is(e.target) && container.has(e.target).length === 0 && !icon.is(e.target) && icon.has(e.target).length === 0) {
            container.hide(500);
        }
    }
});


//base js
$('#nav-tut').click(function () {
    if ($('.collapsed').text() == '') {
        $('.fa-caret-down').addClass('fa-caret-up');
        $('.fa-caret-up').removeClass('fa-caret-down');
    } else {
        $('.fa-caret-up').addClass('fa-caret-down');
        $('.fa-caret-down').removeClass('fa-caret-up');
    }
})
//Get the button
let mybutton = document.getElementById("btn-back-to-top");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function () {
    scrollFunction();
};

function scrollFunction() {
    if (
        document.body.scrollTop > 100 ||
        document.documentElement.scrollTop > 100
    ) {
        mybutton.style.display = "block";
    } else {
        mybutton.style.display = "none";
    }
}

// When the user clicks on the button, scroll to the top of the document
mybutton.addEventListener("click", backToTop);

function backToTop() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}


// Copy to clipboard
const pretag = $('pre');
if (pretag.length > 0) {
    for (var i = 0; i < pretag.length; i++) {
        let spantag = document.createElement('span');
        spantag.classList = 'badge text-white bg-primary fs-6 copy'
        spantag.textContent = 'copy'
        spantag.style.position = 'absolute'
        spantag.style.top = '10px'
        spantag.style.right = '10px'
        spantag.style.zIndex = '1'
        spantag.style.cursor = 'pointer'
        spantag.id = 'span-' + i
        pretag[i].appendChild(spantag)
    }
    $('.copy').on('click', function () {
        let ele = $(this)
        ele.text('copied');
        let parentele = ele.parent()
        /* Copy the text inside the text field */
        navigator.clipboard.writeText(parentele.text().replace('copied', ''))
        console.log(parentele.text().replace('copied', ''))
    })
}

//Full screen
$("img:not(.logo-image,.image-modal-content)").attr('class', 'myImg');
const img_tag = $('img');
if (img_tag.length > 0) {
    $(document).ready(function () {
        $("img:not(.logo-image)").click(function () {
            //$(this).toggleClass('img_full');

        });
    });
}


//hide alert after some time
setTimeout(hideElement, 1000 * 30) //milliseconds until timeout//
function hideElement() {
    $('#alert-message').css('display', 'none');
}

// Get the imagge modal
var modal = document.getElementById("myModal");

// Get the image and insert it inside the modal - use its "alt" text as a caption
var modalImg = document.getElementById("img01");
$('.myImg').on('click', function (e) {
    modal.style.display = "block";
    modalImg.src = this.src;
})

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("image-close")[0];

// When the user clicks on <span> (x), close the modal
span.onclick = function () {
    modal.style.display = "none";
}