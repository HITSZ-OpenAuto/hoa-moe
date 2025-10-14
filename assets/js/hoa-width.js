(function () {
  const widthSwitchers = document.querySelectorAll('.hoa-width-switcher');

  const root = document.documentElement;
  const defaultWidth = getComputedStyle(root).getPropertyValue('--hextra-max-page-width').trim();

  const FULL_WIDTH = '100%';
  let isFullWidth = getComputedStyle(root).getPropertyValue('--hextra-max-page-width').trim() === FULL_WIDTH;

  const toggleWidth = () => {
    isFullWidth = !isFullWidth;
    root.style.setProperty('--hextra-max-page-width', isFullWidth ? FULL_WIDTH : defaultWidth);
  };

  widthSwitchers.forEach(switcher => switcher.addEventListener('click', e => {
    e.preventDefault();
    toggleWidth();
  }));
})();
