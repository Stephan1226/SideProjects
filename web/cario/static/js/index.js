const spotStatus = document.querySelector('#goToSpotStatus');

function goToSpotStatusFunction() {
    window.location.href = '/spot-status';
}
spotStatus.addEventListener(click, goToSpotStatusFunction);
