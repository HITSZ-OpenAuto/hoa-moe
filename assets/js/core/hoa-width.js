(function () {
  const widthSwitchers = document.querySelectorAll('.hoa-width-switcher');

  widthSwitchers.forEach((switcher) => {
    switcher.addEventListener('click', (e) => {
      e.preventDefault();

      switcher.dataset.state = switcher.dataset.state === 'open' ? 'closed' : 'open';

      toggleMenu(switcher);
    });
  });

  window.addEventListener("resize", () => widthSwitchers.forEach(resizeMenu))

  // Dismiss language switcher when clicking outside
  document.addEventListener('click', (e) => {
    if (e.target.closest('.hoa-width-switcher') === null) {
      widthSwitchers.forEach((switcher) => {
        switcher.dataset.state = 'closed';
        const optionsElement = switcher.nextElementSibling;
        optionsElement.classList.add('hx:hidden');
      });
    }
  });
})();
