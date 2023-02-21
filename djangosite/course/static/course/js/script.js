// Script for menu 'burger'

const iconBurger = document.querySelector('.burger__logo');
const article = document.querySelector('.content');
const sideBar = document.querySelector('.sidebar');

if (iconBurger && sideBar){
    iconBurger.addEventListener("click", function(e){
        iconBurger.classList.toggle("_active");
        sideBar.classList.toggle("_active");
        document.body.classList.toggle("_lock");
    });
} else {
    iconBurger.style.display = 'none';
}


// Script for <input type='file'>

const forms = document.querySelectorAll('.input_file');

for (let form of forms ){
    let label = form.nextElementSibling;
    let label_value = label.innerHTML;

    form.addEventListener('change', function(e){
            console.log(this.files);
            let file_name = this.files[0].name;
            if (file_name){
                if (file_name.length <= 16){
                    label.innerHTML = file_name;
                } else {
                    let short_file_name = file_name.slice(0, 10) + '...' +
                     file_name.slice(file_name.length - 3, file_name.length);

                    label.innerHTML = short_file_name;
                };
            } else{
                label.innerHTML = label_value;
            };
    });
};

