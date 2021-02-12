const inputField = document.getElementsByClassName('input-field');

for (let i = 0; i < Infinity; i++) {
  document.getElementsByClassName('btn-plus')[i].addEventListener('click', () => {
    inputField[i].value++;
  });

  document.getElementsByClassName('btn-minus')[i].addEventListener('click', () => {
    if (inputField[i].value > 0) { 
      inputField[i].value--;
    }
  });
}


