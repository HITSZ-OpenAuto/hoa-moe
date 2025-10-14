(function () {
  const widthSwitchers = document.querySelectorAll('.hoa-width-switcher');

  widthSwitchers.forEach((switcher) => {
    switcher.addEventListener('click', (e) => {
      e.preventDefault();

    });
  });
})();
