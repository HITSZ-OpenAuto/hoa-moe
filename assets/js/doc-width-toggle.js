(function () {
  const STORAGE_KEY = 'hoa-doc-width-preference';

  const button = document.getElementById('doc-width-toggle');
  const body = document.body;

  if (!button || !body) {
    return;
  }

  const defaultLabel = button.dataset.defaultText || '';
  const activeLabel = button.dataset.activeText || '';
  const labelEl = button.querySelector('[data-label]');
  const defaultIcon = button.querySelector('[data-icon-default]');
  const activeIcon = button.querySelector('[data-icon-active]');

  const safeStorage = (() => {
    try {
      const testKey = `${STORAGE_KEY}-test`;
      window.localStorage.setItem(testKey, '1');
      window.localStorage.removeItem(testKey);
      return window.localStorage;
    } catch (error) {
      return null;
    }
  })();

  const readPreference = () => {
    if (!safeStorage) {
      return 'default';
    }
    const saved = safeStorage.getItem(STORAGE_KEY);
    return saved === 'full' ? 'full' : 'default';
  };

  const persistPreference = (state) => {
    if (!safeStorage) {
      return;
    }
    if (state === 'default') {
      safeStorage.removeItem(STORAGE_KEY);
    } else {
      safeStorage.setItem(STORAGE_KEY, state);
    }
  };

  const applyState = (state) => {
    const isFull = state === 'full';
    body.classList.toggle('hoa-doc-width-full', isFull);
    const text = isFull ? activeLabel : defaultLabel;
    button.setAttribute('aria-pressed', String(isFull));
    if (text) {
      button.setAttribute('aria-label', text);
      button.setAttribute('title', text);
    }

    if (labelEl && text) {
      labelEl.textContent = text;
    }

    if (defaultIcon) {
      defaultIcon.classList.toggle('hx:hidden', isFull);
    }

    if (activeIcon) {
      activeIcon.classList.toggle('hx:hidden', !isFull);
    }
  };

  const toggle = () => {
    const nextState = body.classList.contains('hoa-doc-width-full') ? 'default' : 'full';
    applyState(nextState);
    persistPreference(nextState);
  };

  const initialState = readPreference();
  applyState(initialState);
  document.documentElement.classList.remove('hoa-doc-width-initial');

  button.addEventListener('click', toggle);
})();
