var stTime = 0;
var endTime = 0;
var timerStart;

var min;
var sec;
var milisec;

var startBtn = document.getElementById("btn-start");
var stopBtn = document.getElementById("btn-stop");
var resetBtn = document.getElementById("btn-reset");
var recordList = document.getElementById("recordBox");

const watchTime = document.querySelector(".watch-main__time");

startBtn.addEventListener("click", function () {
  if (!stTime) {
    stTime = Date.now();
  } else {
    stTime += Date.now() - endTime;
  }

  timerStart = setInterval(function () {
    var nowTime = new Date(Date.now() - stTime);

    min = addZero(nowTime.getMinutes());
    sec = addZero(nowTime.getSeconds());
    milisec = addZero(Math.floor(nowTime.getMilliseconds() / 10));

    document.getElementById("minutes").innerText = min;
    document.getElementById("seconds").innerText = sec;
    document.getElementById("milliseconds").innerText = milisec;
  }, 1);
});

stopBtn.addEventListener("click", function () {
  if (timerStart) {
    clearInterval(timerStart);
    endTime = Date.now();
  }
});

resetBtn.addEventListener("click", function () {
  stTime = 0;
  min = 0;
  sec = 0;
  milisec = 0;
  document.getElementById("minutes").innerText = "00";
  document.getElementById("seconds").innerText = "00";
  document.getElementById("milliseconds").innerText = "00";
  timerStart = null;
});

function addZero(num) {
  return num < 10 ? "0" + num : "" + num;
}

function record() {
  const lapsList = document.createElement("div");
  lapsList.className = "timeLog";
  lapsList.name = "check";
  lapsList.innerHTML = `<input type="checkbox"/> ${watchTime.innerText}`;
  document.querySelector("#recordBox").appendChild(labsList);
}
