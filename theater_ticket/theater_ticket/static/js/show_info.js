const container = document.querySelector('.container');
const seats = document.querySelectorAll('.row .seat:not(.occupied)');
const count = document.getElementById('count');
const total = document.getElementById('total');

// Update total and count
function updateSelectedCount() {
  const selectedSeats = document.querySelectorAll('.row .seat.selected');
  
  var total_value = 0
  for (let i = 0; i < selectedSeats.length; i++) {
    total_value = total_value + parseInt(selectedSeats[i].title)
    // console.log(selectedSeats[i].title)
  } 
  const selectedSeatsCount = selectedSeats.length;
  count.innerText = selectedSeatsCount;
  total.innerText = total_value
}

//Seat click event
container.addEventListener('click', e => {
  if (e.target.classList.contains('seat') &&
     !e.target.classList.contains('occupied')) {
    e.target.classList.toggle('selected');
  }
  updateSelectedCount();
});

function buyTicket(){
  const selectedSeats = document.querySelectorAll('.row .seat.selected');
  var url = 'http://127.0.0.1:8000/buy_ticket/?'
  for (let i = 0; i < selectedSeats.length; i++) {
    url = url + 'id=' + selectedSeats[i].id
    if (i<selectedSeats.length-1){
      url = url + '&'
    }
  }
  // alert(url) 
  window.location = url
}