(function () {
  const widthSwitchers = document.querySelectorAll('.hoa-width-switcher');

  if (!widthSwitchers.length) {
    return;
  }

  const root = document.documentElement;
  const FULL_WIDTH_VALUE = '100%';
  const defaultWidth = getComputedStyle(root)
    .getPropertyValue('--hextra-max-page-width')
    .trim();

  if (!defaultWidth) {
    return;
  }

  const setPressedState = (isFullWidth) => {
    widthSwitchers.forEach((switcher) => {
      switcher.setAttribute('aria-pressed', isFullWidth ? 'true' : 'false');
    });
  };

  const isFullWidth = () => {
    const current = (
      root.style.getPropertyValue('--hextra-max-page-width') ||
      getComputedStyle(root).getPropertyValue('--hextra-max-page-width')
    ).trim();

    return current === FULL_WIDTH_VALUE;
  };

  widthSwitchers.forEach((switcher) => {
    switcher.addEventListener('click', (e) => {
      e.preventDefault();

      const nextWidth = isFullWidth() ? defaultWidth : FULL_WIDTH_VALUE;
      root.style.setProperty('--hextra-max-page-width', nextWidth);
      setPressedState(nextWidth === FULL_WIDTH_VALUE);

    });

  setPressedState(isFullWidth());
  });
})();
