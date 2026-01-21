fetch("/static/profile.json")
  .then(response => response.json())
  .then(data => {
    const container = document.getElementById("datenort");

    data.forEach(profile => {
      const profilDiv = document.createElement("div");
      profilDiv.className = "profil";

      profilDiv.innerHTML = `
        <img src="/static/${profile.image}" alt="${profile.alt}" class="profilbild">
        <div>
          <h3>${profile.name}</h3>
          <div>
            <p>${profile.description}</p>
          </div>
        </div>
      `;

      container.appendChild(profilDiv);
    });
  })
  .catch(error => console.error("Fehler beim Laden der Daten:", error));


document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("personForm").addEventListener("submit", e => {
    e.preventDefault();

    const formData = new FormData(e.target); 

    fetch("/add", {
      method: "POST",
      body: formData 
    })
      .then(res => res.json())
      .then(result => {
        console.log(result);
        alert("Daten zu Datei gespeichert");
        e.target.reset();

        setTimeout(() => {
          location.reload();
        }, 100); // 100 ms = 0.1 seconds
      })
      .catch(err => {
        console.error("Fehler beim senden der Daten:", err);
      });
  });
});

