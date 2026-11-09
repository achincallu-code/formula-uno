document.querySelectorAll("[data-password-toggle]").forEach((button) => {
  button.addEventListener("click", () => {
    const passwordInput = document.getElementById(button.dataset.passwordToggle);
    const shouldShow = passwordInput.type === "password";

    passwordInput.type = shouldShow ? "text" : "password";
    button.setAttribute("aria-pressed", String(shouldShow));
    button.setAttribute(
      "aria-label",
      shouldShow ? "Ocultar contraseña" : "Mostrar contraseña",
    );
  });
});
