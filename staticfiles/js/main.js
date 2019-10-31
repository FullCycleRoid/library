function createParagraph(){
    let para = document.createElement('p');
    para.textContent = 'You clicked on the button';
    document.body.appendChild(para);
};

var buttons = document.querySelectorAll('button');


for (let i = 0, i < buttons.length , i++){
    buttons[i].addEventListener('click', createParagraph)
}
