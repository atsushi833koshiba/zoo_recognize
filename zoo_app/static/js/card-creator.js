const createCard = (img,title,content) =>{
    
    console.log(img)

    let rowElem = document.createElement('div');
    rowElem.classList.add('row');

    let colElem = document.createElement('div');
    colElem.classList.add('col');
    colElem.classList.add('s12')
    colElem.classList.add('m7')

    let cardElem = document.createElement('div');
    cardElem.classList.add('card');

    let cardImgElem = document.createElement('div');
    cardImgElem.classList.add('card-img');

    let cardContentElem = document.createElement('div');
    cardContentElem.classList.add('card-content');

    let cartTitleElem = document.createElement('span');
    cartTitleElem.classList.add('card-title');
    cartTitleElem.innerHTML = title;

    let contentElem = document.createElement('p');
    contentElem.innerText = content;

    rowElem.appendChild(colElem);
    colElem.appendChild(cardElem);
    cardElem.appendChild(cardImgElem);
    cardElem.appendChild(cardContentElem);

    cardImgElem.appendChild(img);
    cardImgElem.appendChild(cartTitleElem);
    cardContentElem.appendChild(contentElem);

    console.log(rowElem)

    return rowElem
}