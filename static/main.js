function showButtons(myButton,buttons){
    let allBut = document.getElementsByTagName('button')
    for (let i=0, but; but=allBut[i]; i++){
        but.style.color='white';
    }

    hideButtons();
    hideForms(['container-4','container-5']);
    myButton.style.color='green';

    for (but of buttons){
        document.getElementById(but).style.display = 'inline-block';
        //console.log(but)
    }
}

function hideButtons(){
    const buttons = document.querySelector('.container-3').children;
    
    for (i = 0; i < buttons.length; i++) {
      //  console.log(buttons.children[i])
        buttons.item(i).style.display = "none";
    }
}

function showForm(myForm, otherForms){
    hideForms(otherForms);
    document.querySelector('.'+myForm).style.display = 'block';
}

function hideForms(forms){
    for (form of forms){
        console.log(document.querySelector('.'+form));
        document.querySelector('.'+form).style.display = 'none';
        
        console.log('Hid: '+document.querySelector('.'+form).style.display)
    }
}

function displayApology(paramApology, paramPercent){
    let myApology = document.getElementById('apology_text');
    let myPercent = document.getElementById('percent_text');
    myApology.innerHTML = paramApology;
    myPercent.innerHTML = paramPercent.slice(2, 5) + "% of users found this helpful";
}


function feedbackGot(){
    let feedbackText = document.getElementById('header-3');
    let feedbackButtonY = document.getElementById('get_fb_y');
    let feedbackButtonN = document.getElementById('get_fb_n');
    feedbackText.innerHTML = "Thank you for your feedback.";
    feedbackButtonY.style.display = 'none';
    feedbackButtonN.style.display = 'none';
}

