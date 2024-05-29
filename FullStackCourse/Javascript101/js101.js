/*Make sure the js file is loaded at the end of the body or null value error will occur*/ 
const name1=document.getElementById("name");
const age=document.getElementById("age");
const dogYears=document.getElementById("dogyears");

name1.innerText = "Keshav Kannan";
age.innerText = 20;

function showDogYears(age){
    dogYears.innerText = Number(age)*7;
    return Number(age)*7;
}

dogYears.innerText = showDogYears(age.innerText);

const fakeInputs=document.querySelectorAll(".fake-input")
fakeInputs.forEach(node =>{
    node.classList.add("real-input")
})

