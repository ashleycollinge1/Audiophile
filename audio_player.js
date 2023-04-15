window.onload = () => {
    const audio = document.getElementById("audio-player");
    const play = document.getElementById("play");
    const pause = document.getElementById("pause");
  
    // associate functions with the 'onclick' events
    play.onclick = playAudio;
    pause.onclick = pauseAudio;
  
    function playAudio() {
      audio.play();
    }
  
    function pauseAudio() {
      audio.pause();
    }
  };