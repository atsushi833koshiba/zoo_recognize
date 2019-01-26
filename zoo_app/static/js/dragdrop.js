document.addEventListener('DOMContentLoaded',(evt)=>{

    const droparea = document.getElementById('droparea');
    const listarea = document.getElementById('listarea');
    const fileInput = document.getElementById('fileInput');
    const filePath = document.getElementById('filePath');
    let outarea = document.getElementById('outarea');

    droparea.addEventListener('dragover', (evt) => {
        evt.stopPropagation();
        evt.preventDefault();
        evt.dataTransfer.dropEffect = 'copy';
        droparea.classList.add('dragover');
      });

      droparea.addEventListener('dragleave', (evt) => {
        droparea.classList.remove('dragover');
      });

      droparea.addEventListener('drop', (evt) =>{
        evt.preventDefault();
        droparea.classList.remove('dragover');
        console.log(evt.dataTransfer.files)
        fileInput.files = evt.dataTransfer.files;

        const images = Array.from(evt.dataTransfer.files);
        createListByFiles(images);
      });

      // クリック時にファイルアップロード用のエクスプローラーを表示する。
      droparea.addEventListener('click', (evt) => {
        fileInput.click();
      });

      // droparea.addEventListener('change', (evt) => {
      //   const files = Array.from(fileInput.files)
      //   fileName = files.slice(-1)[0].name
      //   createList(fileName)
      // });
})

const createList = (fileName) => {
    let ulElem = document.createElement('ul');
    let liElem = document.createElement('li');
    liElem.innerText = fileName;
    ulElem.appendChild(liElem);
    listarea.appendChild(ulElem);
}

const createListByFiles = (files)=> {

    let ulElem = document.createElement('ul');

    files.forEach(file => {
        let liElem = document.createElement('li');
        liElem.innerText = file.name
        ulElem.appendChild(liElem)

        // HTTPリクエスト

        // DOM生成
        // imageObj = new Image();

        // // File/BlobオブジェクトにアクセスできるURLを生成
        // url = URL.createObjectURL(file);
        // imageObj.src = url;
        // console.log(imageObj)


        // imageObj.addEventListener('load',(evt)=>{
        //     URL.revokeObjectURL(url);
        //     let card = createCard(imageObj,'CardTitle','AAAAAAAA');
        //     outarea.appendChild(card);
        // })

    })
    listarea.appendChild(ulElem);
}
