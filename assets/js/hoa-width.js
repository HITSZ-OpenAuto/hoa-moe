(function () {
  const switches = document.querySelectorAll(".hoa-width-switcher");
  const root = document.documentElement;
  const defaultWidth = "90rem";
  const fullWidth = "100%";
  const key = "hoa-preferred-width";

  const getPreferred = () => localStorage.getItem(key) === "full";
  const setPreferred = (isFull) => localStorage.setItem(key, isFull ? "full" : "default");
  const applyWidth = (isFull) => {
    const width = isFull ? fullWidth : defaultWidth;
    root.style.setProperty("--hextra-max-page-width", width);
    root.style.setProperty("--hextra-max-navbar-width", width);
    root.style.setProperty("--hextra-max-footer-width", width);
  };

  let isFull = getPreferred();
  applyWidth(isFull);

  const toggle = () => {
    isFull = !isFull;
    applyWidth(isFull);
    setPreferred(isFull);
  };

  switches.forEach((s) =>
    s.addEventListener("click", (e) => {
      e.preventDefault();
      toggle();
    })
  );
})();
