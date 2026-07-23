window.dashboardApi = {

    async import_article_pdf(file) {

        const formData = new FormData();
        formData.append("pdf", file);

        const response = await fetch("/api/import", {
            method: "POST",
            body: formData
        });

        return await response.json();
    },

    async load_articles() {

        const response = await fetch("/api/articles");

        return await response.json();
    }

};