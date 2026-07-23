const file = document.getElementById("pdfFile");
const status = document.getElementById("status");
const start = document.getElementById("startParser");
const bar = document.getElementById("progressBar");

let selectedFile = null;

file.onchange = () => {

    selectedFile = file.files.length > 0 ? file.files[0] : null;

    start.disabled = !selectedFile;

    bar.style.width = selectedFile ? "25%" : "0%";

    if (selectedFile) {
        status.innerHTML = `Ausgewählt: ${selectedFile.name}`;
    } else {
        status.innerHTML = "Bereit.";
    }
};

start.onclick = async () => {

    if (!selectedFile) {
        return;
    }

    start.disabled = true;

    status.innerHTML = "Import läuft...";

    bar.style.width = "60%";

    try {

        const result = await dashboardApi.import_article_pdf(selectedFile);

        if (result.success) {

            status.innerHTML = `✅ ${result.count} Artikel importiert`;

            bar.style.width = "100%";

        } else {

            status.innerHTML = `❌ ${result.message ?? "Import fehlgeschlagen"}`;

            bar.style.width = "60%";
        }

    } catch (err) {

        console.error(err);

        status.innerHTML = "❌ Verbindung zum Server fehlgeschlagen";

        bar.style.width = "0%";

    } finally {

        start.disabled = false;

    }

};