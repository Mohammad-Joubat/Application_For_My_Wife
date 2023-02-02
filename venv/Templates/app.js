<script>
  const times = document.querySelectorAll(".time");
  times.forEach(time => {
    time.addEventListener("click", function() {
      times.forEach(t => t.classList.remove("selected"));
      this.classList.add("selected");
    });
  });
</script>
